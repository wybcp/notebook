之前在Sec-News中推荐了一个开源程序 <https://github.com/yandex/gixy> ，作用是来检测Nginx配置文件中存在的问题。正好Pwnhub上周的比赛也出现了一道题，包含由Nginx配置错误导致的漏洞。

所以我挑选我觉得比较有趣，而且很有可能犯错误的三个典型案例，来说说Nginx配置文件的安全。

另外，本文所涉及的三个案例，均已上线到Vulhub（ <https://github.com/phith0n/vulhub/tree/master/nginx/insecure-configuration> ），阅读本文的同时可以自己动手测试。

## [`$uri`导致的CRLF注入漏洞](https://www.leavesongs.com/PENETRATION/nginx-insecure-configuration.html#uricrlf)

下面两种情景十分常见：

1. 用户访问`http://example.com/aabbcc`，自动跳转到`https://example.com/aabbcc`
2. 用户访问`http://example.com/aabbcc`，自动跳转到`http://www.example.com/aabbcc`

比如我的博客，访问`http://www.leavesongs.com/other/tinger.html`，将会301跳转到`https://www.leavesongs.com/other/tinger.html`。随着现在https的普及，很多站点都强制使用https访问，这样的跳转非常常见。

第二个场景主要是为了统一用户访问的域名，更加有益于SEO优化。

在跳转的过程中，我们需要保证用户访问的页面不变，所以需要从Nginx获取用户请求的文件路径。查看Nginx文档，可以发现有三个表示uri的变量：

1. `$uri`
2. `$document_uri`
3. `$request_uri`

解释一下，1和2表示的是解码以后的请求路径，不带参数；3表示的是完整的URI（没有解码）。那么，如果运维配置了下列的代码：

```
location / {
    return 302 https://$host$uri;
}
```

因为`$uri`是解码以后的请求路径，所以可能就会包含换行符，也就造成了一个CRLF注入漏洞。（关于CRLF注入漏洞，可以参考我的老文章 <https://www.leavesongs.com/PENETRATION/Sina-CRLF-Injection.html> ）

这个CRLF注入漏洞可以导致会话固定漏洞、设置Cookie引发的CSRF漏洞或者XSS漏洞。其中，我们通过注入两个`\r\n`即可控制HTTP体进行XSS，但因为浏览器认为这是一个300跳转，所以并不会显示我们注入的内容。

这个情况下，我们可以利用一些技巧：比如使用CSP头来iframe的地址，这样浏览器就不会跳转，进而执行我们插入的HTML：

[![14967564064912.jpg](https://cdn.ioin.in/media/attachment/2017/06/06/e7991828-ed42-4f96-837a-a0d843a57f44.3241db8d285a.jpg)](https://cdn.ioin.in/media/attachment/2017/06/06/e7991828-ed42-4f96-837a-a0d843a57f44.jpg)

关于上述利用方法，可以参考我的另一篇文章《[Bottle HTTP 头注入漏洞探究](https://www.leavesongs.com/PENETRATION/bottle-crlf-cve-2016-9964.html)》。

如何修复这个CRLF漏洞？正确的做法应该是如下：

```
location / {
    return 302 https://$host$request_uri;
}
```

另外，由`$uri`导致的CRLF注入漏洞不仅可能出现在上述两个场景中，理论上，只要是可以设置HTTP头的场景都会出现这个问题。

## [目录穿越漏洞](https://www.leavesongs.com/PENETRATION/nginx-insecure-configuration.html#_1)

这个常见于Nginx做反向代理的情况，动态的部分被proxy_pass传递给后端端口，而静态文件需要Nginx来处理。

假设静态文件存储在/home/目录下，而该目录在url中名字为files，那么就需要用alias设置目录的别名：

```
location /files {
    alias /home/;
}
```

此时，访问`http://example.com/files/readme.txt`，就可以获取`/home/readme.txt`文件。

但我们注意到，url上`/files`没有加后缀`/`，而alias设置的`/home/`是有后缀`/`的，这个`/`就导致我们可以从`/home/`目录穿越到他的上层目录：

[![14967571806301.jpg](https://cdn.ioin.in/media/attachment/2017/06/06/7cbce5a7-a9c9-4a73-8900-4eed2c99aa0a.ff403ef68c8e.jpg)](https://cdn.ioin.in/media/attachment/2017/06/06/7cbce5a7-a9c9-4a73-8900-4eed2c99aa0a.jpg)

进而我们获得了一个任意文件下载漏洞。

这个有趣的漏洞出现在了Pwnhub上一期比赛《[寻找 SNH48](https://pwnhub.cn/gamedetail?id=15)》中，@Ricter师傅的题目。

如何解决这个漏洞？只需要保证location和alias的值都有后缀`/`或都没有这个后缀。

## [Http Header被覆盖的问题](https://www.leavesongs.com/PENETRATION/nginx-insecure-configuration.html#http-header)

众所周知，Nginx的配置文件分为Server、Location、If等一些配置块，并且存在包含关系，和编程语言比较类似。如果在外层配置的一些选项，是可以被继承到内层的。

但这里的继承也有一些特性，比如add_header，子块中配置后将会覆盖父块中的add_header添加的**所有**HTTP头，造成一些安全隐患。

如下列代码，Server块添加了CSP头：

```
server {
    ...
    add_header Content-Security-Policy "default-src 'self'";
    add_header X-Frame-Options DENY;

    location = /test1 {
        rewrite ^(.*)$ /xss.html break;
    }

    location = /test2 {
        add_header X-Content-Type-Options nosniff;
        rewrite ^(.*)$ /xss.html break;
    }
}
```

但/test2的location中又添加了X-Content-Type-Options头，导致父块中的add_header全部失效：

[![14967575824298.jpg](https://cdn.ioin.in/media/attachment/2017/06/06/242552f2-92e9-473b-b90d-d171754e9cd5.b8ebaf41145b.jpg)](https://cdn.ioin.in/media/attachment/2017/06/06/242552f2-92e9-473b-b90d-d171754e9cd5.jpg)

此时，test2的csp就完全失效了，我们成功触发XSS：

[![14967576277243.jpg](https://cdn.ioin.in/media/attachment/2017/06/06/5492fe8b-da77-40d4-a217-887badad5060.92dbea6e78fc.jpg)](https://cdn.ioin.in/media/attachment/2017/06/06/5492fe8b-da77-40d4-a217-887badad5060.jpg)

## [总结](https://www.leavesongs.com/PENETRATION/nginx-insecure-configuration.html#_2)

Nginx配置文件造成的漏洞绝不止这三种，比如之前特别火的解析漏洞（ <https://github.com/phith0n/vulhub/tree/master/nginx_parsing_vulnerability> ），也和Nginx的配置有一定关系。

解决这类漏洞，最根本的方法是仔细阅读官方文档，文档里说明了很多配置文件错误和正确的用法。最忌去百度网上的一些解决方法，很多错误就是一传十十传百，最后流传开来的。

另外，本文开头提到的工具gixy，我们也可以利用起来，网站上线前进行一下扫描，也许就能发现一些可能存在的问题。



## 原文

https://www.leavesongs.com/PENETRATION/nginx-insecure-configuration.html
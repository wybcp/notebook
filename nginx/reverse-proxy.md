# 反向代理（Reverse Proxy）

反向代理（Reverse Proxy）方式是指以代理服务器来接受 internet 上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给 internet 上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。

## https 反向代理配置

一些对安全性要求比较高的站点，可能会使用 HTTPS（一种使用 ssl 通信标准的安全 HTTP 协议）。

使用 nginx 配置 https 需要知道几点：

- HTTPS 的固定端口号是 443，不同于 HTTP 的 80 端口
- SSL 标准需要引入安全证书，所以在 nginx.conf 中你需要指定证书和它对应的 key

其他和 http 反向代理基本一样，只是在 Server 部分配置有些不同。

```nginx
#HTTP服务器
server {
    #监听443端口。443为知名端口号，主要用于HTTPS协议
    listen       443 ssl;

    #定义使用www.xx.com访问
    server_name  www.helloworld.com;

    #ssl证书文件位置(常见证书文件格式为：crt/pem)
    ssl_certificate      cert.pem;
    #ssl证书key位置
    ssl_certificate_key  cert.key;

    #ssl配置参数（选择性配置）
    ssl_session_cache    shared:SSL:1m;
    ssl_session_timeout  5m;
    #数字签名，此处使用MD5
    ssl_ciphers  HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers  on;

    location / {
        root   /root;
        index  index.html index.htm;
    }
}
```

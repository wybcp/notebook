# 离线应用

离线检测：navigator.onLine。

## 应用缓存

application cache，从浏览器的缓存中分出来的一块缓存区。使用一个描述文件(manifest file)：列出要下载和缓存的资源。

在`<html>`中的 manifest 属性中指定描述文件的路径：

```html
<html manifest="./offline.appcache"></html>
```

描述文件的扩展名以前用.manifest，现在推荐.appcache

### applicationCache 对象

这个对象有一个 status 属性，值为常量，表示缓存状态：

- 0：没有与页面相关的应用缓存
- 1：应用缓存未得到更新
- 2：正在下载描述文件并检查更新
- 3：应用缓存正在下载描述文件中指定的资源
- 4：应用缓存已经更新了资源，可以通过 swapCache()使用
- 5：应用缓存的描述文件不存在，页面无法再访问应用缓存

这个对象有以下事件，表示其状态的改变：

- checking：在浏览器为应用缓存查找更新时触发
- error：在检查更新或下载资源期间发生错误时触发
- noupdate：在检查描述文件发现文件无变化时触发
- downloading：在开始下载应用缓存资源时触发
- progress：在文件下载应用缓存的过程中持续不断地触发
- updateready：在页面新的应用缓存下载完毕且可以通过 swapCache() 使用时触发
- cached：在应用缓存完整可用时触发

一般来讲，这些事件会随着页面加载按上述顺序依次触发。

通过调用 update()方法可以手工干预，让应用缓存为检查更新而触发上述事件

```
applicationCache.update();
```

update()一经调用，应用缓存就会去检查描述文件是否更新（触发 checking 事件），然后继续执行后续操作。如果触发了 cached 事件，就说明应用缓存已经准备就绪。

## 数据存储

### Cookie

#### cookie 的构成：

- 名称：一个唯一确定 cookie 的名称，必须经过 URL 编码，不分大小写
- 值：储存在 cookie 中的字符串值
- 域：cookie 对于哪个域是有效的。所有向该域发送的请求中都会包含这个 cookie 信息。
- 路径：对于指定域中的那个路径，应该向服务器发送 cookie
- 失效时间：表示 cookie 何时应该被删除的时间戳。默认情况下，浏览器会话结束时即将所有的 cookie 删除。
- 安全标志：指定后，cookie 只有在使用 SSL 连接的时候才发送到服务器

只有名值对才被发送给服务器，其余的是服务器给浏览器的指示（何时发送）。

每个域的 cookie 总数是有限的（浏览器差异），尺寸也有限制，长度限制在 4096B。

#### document.cookie

document.cookie 返回当前页面可用的所有 cookie 的字符串，一系列由分号隔开的名值对儿，需要使用 decodeURICompoment()解码。

函数简化 cookie 操作：读取、写入、删除。

```js
var CookieUtil = {
  get: function(name) {
    var cookieName = encodeURIComponent(name) + "=",
      cookieStart = document.cookie.indexOf(cookieName),
      cookieValue = null,
      cookieEnd;

    if (cookieStart > -1) {
      cookieEnd = document.cookie.indexOf(";", cookieStart);
      if (cookieEnd == -1) {
        cookieEnd = document.cookie.length;
      }
      cookieValue = decodeURIComponent(
        document.cookie.substring(cookieStart + cookieName.length, cookieEnd)
      );
    }

    return cookieValue;
  },

  set: function(name, value, expires, path, domain, secure) {
    var cookieText = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    if (expires instanceof Date) {
      cookieText += "; expires=" + expires.toGMTString();
    }

    if (path) {
      cookieText += "; path=" + path;
    }

    if (domain) {
      cookieText += "; domain=" + domain;
    }

    if (secure) {
      cookieText += "; secure";
    }

    document.cookie = cookieText;
  },

  unset: function(name, path, domain, secure) {
    this.set(name, "", new Date(0), path, domain, secure);
  } //没有删除已有cookie的直接方法，通过设置失效时间为过去时间达到删除效果。
};
```

由于所有的 cookie 都会由浏览器作为请求头发送，所以在 cookie 中存储大量信息会影响到特定域的请求性能。cookie 信息越大，完成对服务器请求的时间也就越长，因此尽可能在 cookie 中少存储信息，以避免影响性能。 ####子 cookie

为了绕开浏览器的单域名下的 cookie 数限制，开发人员使用一种称为子 cookie(subcookie)的概念，子 cookie 是存放在单个 cookie 中的更小端的数据，即使用 cookie 值来存储多个名值对儿 。

格式如下： name=name1=value1&name2=value2&name3=value3&name4=value4&name5=value5

### Web 存储机制

主要目的：

- 提供一种在 cookie 之外的存储会话数据的途径；
- 提供一种存储大量可以跨会话存在的数据机制。

#### storage 类型

### IndexedDB

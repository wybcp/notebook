# CSRF

CSRF 是跨站请求伪造（Cross-site request forgery）

Express 团队的[csrf](https://github.com/pillarjs/csrf)模块和[csurf](https://github.com/pillarjs/csurf)模块的加密函数的用法

## CSRF 攻击原理

在他们的钓鱼站点，攻击者可以通过创建一个 AJAX 按钮或者表单来针对你的网站创建一个请求：

```html
<form action="https://my.site.com/me/something-destructive" method="POST">
  <button type="submit">Click here for free money!</button>
</form>
```

这是很危险的，因为攻击者可以使用其他 http 方法例如 `delete` 来获取结果。这在用户的 session 中有很多关于你的网站的详细信息时是相当危险的。

## 防范 CSRF 攻击

### 只使用 JSON api

使用 JavaScript 发起 AJAX 请求是限制跨域的。不能通过一个简单的`<form>`来发送`JSON`，所以，通过只接收 JSON，你可以降低发生上面那种情况的可能性。

### 禁用 CORS

第一种减轻 CSRF 攻击的方法是禁用 cross-origin requests(跨域请求)。

如果你希望允许跨域请求，那么请只允许 `OPTIONS, HEAD, GET` 方法，因为他们没有副作用。

不幸的是，这不会阻止上面的请求由于它没有使用 JavaScript(因此 CORS 不适用)。

### 检验 referrer 头部

不幸的是，检验 referrer 头部很麻烦，但是你可以阻止那些 referrer 头部不是来自你的页面的请求。

举个例子，你不能加载 session 如果这个请求的 referrer 头部不是你的服务器。

### GET 总是幂等的

确保你的`GET`请求不会修改你数据库中的相关数据。

### 避免使用 POST

因为`<form>`只能用`GET`或是`POST`,而不能使用别的方法，例如`PUT`, `PATCH`, `DELETE`，攻击者很难有方法攻击你的网站。

### 不要复写方法

许多应用程序使用[复写方法](https://github.com/expressjs/method-override)来在一个常规表单中使用`PUT`, `PATCH`, 和`DELETE`请求，这会使得原先不易受攻击的方法变得易受攻击。

### 不要兼容旧浏览器

旧的浏览器不支持 CORS 或是其他安全政策。

### CSRF Tokens

最终的解决办法是使用 CSRF tokens。

CSRF tokens 是如何工作的呢？

1. 服务器发送给客户端一个 token。
2. 客户端提交的表单中带着这个 token。
3. 如果这个 token 不合法，那么服务器拒绝这个请求。

攻击者需要通过某种手段获取你站点的 CSRF token，他们只能使用 JavaScript 来做。所以，如果你的站点不支持 CORS，那么他们就没有办法来获取 CSRF token，降低了威胁。

**确保 CSRF token 不能通过 AJAX 访问到!**
不要创建一个`/CSRF`路由来获取一个 token，尤其不要在这个路由上支持 CORS!

token 需要是不容易被猜到的，让它很难被攻击者尝试几次得到。

## BREACH 攻击

这也就是 salt(加盐)出现的原因。

Breach 攻击相当简单：如果服务器通过`HTTPS+gzip`多次发送相同或者相似的响应，攻击者就可以猜测响应的内容(使得 HTTPS 完全无用)。

解决办法？让每一个响应都有那么一点不同。

于是，CSRF tokens 依据每一个不同的请求还有不同的时间来生成。但是服务器需要知道客户端请求中带的 token 是否是合法的。
因此：

1. 一般认为安全加密的 CSRF tokens 是防护 CSRF 的关键
2. CSRF tokens 现在通常是一个秘钥或者 salt 的 hash

了解更多:

- [BREACH][1]
- [CRIME](http://en.wikipedia.org/wiki/CRIME)
- [Defending against the BREACH Attack](https://community.qualys.com/blogs/securitylabs/2013/08/07/defending-against-the-breach-attack)

[1]: http://en.wikipedia.org/wiki/BREACH_(security_exploit)

注意，CSRF 没有\_解决\_BREACH 攻击，但是这个模块通过随机化请求来为你减轻 BREACH 攻击。

## salt 不需要加密

**因为客户端知道 salt!!!**
服务器会发送 `<salt>;<token>` ，然后客户端会通过请求返回相同的值给服务器。服务器然后会检验 `<secret>+<salt>=<token>` 。
salt 必须跟 token 一起被发送给服务器，否则服务器不能验证这个 token。
这是最简单的加密方式。

## 创建 tokens 必须要快

**因为每当进来一个请求他们就会被创建!**
像`Math.random().toString(36).slice(2)`这么做也是性能足够好的!你不需要 OpenSSL 来为每一个请求创建一个密码安全的 token。

## 秘钥不需要是加密的，但需要是安全的

如果你正在使用一个数据库后端来存储 session，客户端是不会知道秘钥的，因为它被存储在数据库中。

如果你正在使用 cookie 来存储 session，那么秘钥就会被存储在 cookie 中发送给客户端。

因此， **确保 cookie sessions 使用 `httpOnly` 那样客户端就不能通过客户端 JavaScript 来读取到秘钥!**

## 当你不正确的使用 CSRF token

### 把它们加到 JSON AJAX 调用中

正如上面提到的，如果你不支持 CORS 并且你的 API 是传输的严格的 JSON，绝没可能在你的 AJAX 调用中加入 CSRF token。

### 通过 AJAX 暴露你的 CSRF token

不要创建一个`GET /csrf`路由,并且尤其不要在这个路由上支持 CORS。

不要发送 CSRF token 在 API 响应的 body 中。

## 结论

因为 web 正在向 JSON API 转移，并且浏览器变得更安全，有更多的安全策略，CSRF 正在变得不那么值得关注。阻止旧的浏览器访问你的站点，并尽可能的将你的 AP 变成 JSON API，然后你将不再需要 CSRF token。但是为了安全起见，你还是应该尽量允许他们尤其是当难以实现的时候。

## 参考

[理解 CSRF(跨站请求伪造)](https://github.com/pillarjs/understanding-csrf/blob/master/README_zh.md)

> 原文出处[Understanding CSRF](https://github.com/pillarjs/understanding-csrf)

# [jwt-go](https://github.com/dgrijalva/jwt-go)

使用 JWT 进行身份校验

## JWT

JWT 标准的 Token 有三个部分：

- header
- payload
- signature

中间用点分隔开，使用 Base64 编码

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuYW1lIjoid2FuZ2hhbyIsImFkbWluIjp0cnVlfQ.SwyHTEx_RQppr97g4J5lKXtabJecpejuef8AqKYMAJc

### Header

header 部分主要是两部分内容，一个是 Token 的类型，另一个是使用的算法，比如下面类型就是 JWT，使用的算法是 HS256。

    { "typ": "JWT", "alg": "HS256" }

用 Base64 的形式编码一下，所以就变成这样：

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

### Payload

Payload 里面是 Token 的具体内容，这些内容里面有一些是标准字段，你也可以添加其它需要的内容。下面是标准字段：

- iss：Issuer，发行者
- sub：Subject，主题
- aud：Audience，观众
- exp：Expiration time，过期时间
- nbf：Not before
- iat：Issued at，发行时间
- jti：JWT ID

使用 Base64 编码：

    eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuYW1lIjoid2FuZ2hhbyIsImFkbWluIjp0cnVlfQ

### Signature

有三个部分，先是用 Base64 编码的 header.payload ，再用加密算法加密一下，加密的时候要放进去一个 Secret ，这个相当于是一个密码，这个密码秘密地存储在服务端。

- header
- payload
- secret

  var encodedString = base64UrlEncode(header) + "." + base64UrlEncode(payload); HMACSHA256(encodedString, 'secret');

处理完成以后看起来像这样：

    SwyHTEx_RQppr97g4J5lKXtabJecpejuef8AqKYMAJc

最后这个在服务端生成并且要发送给客户端的 Token 看起来像这样：

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJuaW5naGFvLm5ldCIsImV4cCI6IjE0Mzg5NTU0NDUiLCJuYW1lIjoid2FuZ2hhbyIsImFkbWluIjp0cnVlfQ.SwyHTEx_RQppr97g4J5lKXtabJecpejuef8AqKYMAJc

客户端收到这个 Token 以后把它存储下来，下回向服务端发送请求的时候就带着这个 Token 。服务端收到这个 Token ，然后进行验证，通过以后就会返回给客户端想要的资源。

[基于 Token 的身份验证](https://blog.csdn.net/qq_28098067/article/details/52036493)

# 常用函数

[memory_get_usage()](http://php.net/manual/en/function.memory-get-usage.php) 返回 php 内存使用情况，单位字节。

## HTTP 状态码分类

| 分类 | 分类描述 | Description |
| --- | --- | --- |
| 1\*\* | 信息，服务器收到请求，需要请求者继续执行操作 | Informational - Request received, continuing process |
| 2\*\* | 成功，操作被成功接收并处理 | Success - The action was successfully received, understood, and accepted |
| 3\*\* | 重定向，需要进一步的操作以完成请求 | 3xx: Redirection - Further action must be taken in order to complete the request |
| 4\*\* | 客户端错误，请求包含语法错误或无法完成请求 | Client Error - The request contains bad syntax or cannot be fulfilled |
| 5\*\* | 服务器错误，服务器在处理请求的过程中发生了错误 | 5xx: Server Error - The server failed to fulfill an apparently valid request |

## HTTP 状态码列表

| Value | Description | Reference | 中文 |
| --- | --- | --- | --- |
| 100 | Continue | [[RFC7231, Section 6.2.1](http://www.iana.org/go/rfc7231)] | 继续。[客户端](http://www.dreamdu.com/webbuild/client_vs_server/)应继续其请求 |
| 101 | Switching Protocols | [[RFC7231, Section 6.2.2](http://www.iana.org/go/rfc7231)] | 切换协议。服务器根据客户端的请求  [`Upgrade`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Upgrade)  标头切换协议。只能切换到更高级的协议，例如，切换到 HTTP 的新版本协议 |
| 102 | Processing | [[RFC2518](http://www.iana.org/go/rfc2518)] | 服务器已收到并正在处理该请求，但没有响应可用 |
| 103 | Early Hints | [[RFC8297](http://www.iana.org/go/rfc8297)] |  |
| 104-199 | Unassigned |  |  |
| 200 | OK | [[RFC7231, Section 6.3.1](http://www.iana.org/go/rfc7231)] | 请求成功。一般用于 GET 与 POST 请求 |
| 201 | Created | [[RFC7231, Section 6.3.2](http://www.iana.org/go/rfc7231)] | 已创建。成功请求并创建了新的资源， 在 PUT 请求之后发送的响应。 |
| 202 | Accepted | [[RFC7231, Section 6.3.3](http://www.iana.org/go/rfc7231)] | 已接受。已经接受请求，但未处理完成 |
| 203 | Non-Authoritative Information | [[RFC7231, Section 6.3.4](http://www.iana.org/go/rfc7231)] | 非授权信息。请求成功。但返回的 meta 信息不在原始的服务器，而是一个副本 |
| 204 | No Content | [[RFC7231, Section 6.3.5](http://www.iana.org/go/rfc7231)] | 无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档 |
| 205 | Reset Content | [[RFC7231, Section 6.3.6](http://www.iana.org/go/rfc7231)] | 重置内容。服务器处理成功，用户终端（例如：浏览器）应重置文档视图。可通过此返回码清除浏览器的表单域 |
| 206 | Partial Content | [[RFC7233, Section 4.1](http://www.iana.org/go/rfc7233)] | 部分内容。服务器成功处理了部分 GET 请求， 类似于 FlashGet 或者迅雷这类的 HTTP 下载工具都是使用此类响应实现断点续传或者将一个大文档分解为多个下载段同时下载。该请求必须包含 Range 头信息来指示客户端希望得到的内容范围，并且可能包含 If-Range 来作为请求条件。 |
| 207 | Multi-Status | [[RFC4918](http://www.iana.org/go/rfc4918)] | 由 WebDAV(RFC 2518)扩展的状态码，代表之后的消息体将是一个 XML 消息，并且可能依照之前子请求数量的不同，包含一系列独立的响应代码。 |
| 208 | Already Reported | [[RFC5842](http://www.iana.org/go/rfc5842)] | 在 DAV 里面使用: propstat 响应元素以避免重复枚举多个绑定的内部成员到同一个集合。 |
| 209-225 | Unassigned |  |  |
| 226 | IM Used | [[RFC3229](http://www.iana.org/go/rfc3229)] | 服务器已经完成了对资源的 GET 请求，并且响应是对当前实例应用的一个或多个实例操作结果的表示。 |
| 227-299 | Unassigned |  |  |
| 300 | Multiple Choices | [[RFC7231, Section 6.4.1](http://www.iana.org/go/rfc7231)] | 多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择 |
| 301 | Moved Permanently | [[RFC7231, Section 6.4.2](http://www.iana.org/go/rfc7231)] | 永久移动。请求的资源已被永久的移动到新 URI，返回信息会包括新的 URI，浏览器会自动定向到新 URI。今后任何新的请求都应使用新的 URI 代替 |
| 302 | Found | [[RFC7231, Section 6.4.3](http://www.iana.org/go/rfc7231)] | 临时移动。与 301 类似。但资源只是临时被移动。客户端应继续使用原有 URI， 只有在 Cache-Control 或 Expires 中进行了指定的情况下，这个响应才是可缓存的。 |
| 303 | See Other | [[RFC7231, Section 6.4.4](http://www.iana.org/go/rfc7231)] | 查看其它地址。与 301 类似。使用 GET 和 POST 请求查看 |
| 304 | Not Modified | [[RFC7232, Section 4.1](http://www.iana.org/go/rfc7232)] | 未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源 |
| 305 | Use Proxy | [[RFC7231, Section 6.4.5](http://www.iana.org/go/rfc7231)] | 使用代理。所请求的资源必须通过代理访问 |
| 306 | (Unused) | [[RFC7231, Section 6.4.6](http://www.iana.org/go/rfc7231)] | 已经被废弃的 HTTP 状态码 |
| 307 | Temporary Redirect | [[RFC7231, Section 6.4.7](http://www.iana.org/go/rfc7231)] | 临时重定向。与 302 类似。使用 GET 请求重定向 |
| 308 | Permanent Redirect | [[RFC7538](http://www.iana.org/go/rfc7538)] | 这意味着资源现在永久位于由  `Location:` HTTP Response 标头指定的另一个 URI。 这与  `301 Moved Permanently HTTP`  响应代码具有相同的语义，但用户代理不能更改所使用的 HTTP 方法：如果在第一个请求中使用  `POST`，则必须在第二个请求中使用  `POST`。 |
| 309-399 | Unassigned |  |  |
| 400 | Bad Request | [[RFC7231, Section 6.5.1](http://www.iana.org/go/rfc7231)] | 客户端请求的语法错误，服务器无法理解 |
| 401 | Unauthorized | [[RFC7235, Section 3.1](http://www.iana.org/go/rfc7235)] | 请求要求用户的身份认证。 当前请求需要用户验证。该响应必须包含一个适用于被请求资源的 WWW-Authenticate 信息头用以询问用户信息。 |
| 402 | Payment Required | [[RFC7231, Section 6.5.2](http://www.iana.org/go/rfc7231)] | 保留，将来使用 |
| 403 | Forbidden | [[RFC7231, Section 6.5.3](http://www.iana.org/go/rfc7231)] | 服务器理解请求客户端的请求，但是拒绝执行此请求 |
| 404 | Not Found | [[RFC7231, Section 6.5.4](http://www.iana.org/go/rfc7231)] | 服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面 |
| 405 | Method Not Allowed | [[RFC7231, Section 6.5.5](http://www.iana.org/go/rfc7231)] | 客户端请求中的方法被禁止。 该响应必须返回一个 Allow 头信息用以表示出当前资源能够接受的请求方法的列表。 　　鉴于 PUT，DELETE 方法会对服务器上的资源进行写操作，因而绝大部分的网页服务器都不支持或者在默认配置下不允许上述请求方法，对于此类请求均会返回 405 错误。 |
| 406 | Not Acceptable | [[RFC7231, Section 6.5.6](http://www.iana.org/go/rfc7231)] | 服务器无法根据客户端请求的内容特性完成请求 |
| 407 | Proxy Authentication Required | [[RFC7235, Section 3.2](http://www.iana.org/go/rfc7235)] | 请求要求代理的身份认证，与 401 类似，但请求者应当使用代理进行授权。 代理服务器必须返回一个 Proxy-Authenticate 用以进行身份询问。客户端可以返回一个 Proxy-Authorization 信息头用以验证。 |
| 408 | Request Timeout | [[RFC7231, Section 6.5.7](http://www.iana.org/go/rfc7231)] | 服务器等待客户端发送的请求时间过长，超时 |
| 409 | Conflict | [[RFC7231, Section 6.5.8](http://www.iana.org/go/rfc7231)] | 服务器完成客户端的 PUT 请求是可能返回此代码，服务器处理请求时发生了冲突 |
| 410 | Gone | [[RFC7231, Section 6.5.9](http://www.iana.org/go/rfc7231)] | 客户端请求的资源已经不存在。410 不同于 404，如果资源以前有现在被永久删除了可使用 410 代码，网站设计人员可通过 301 代码指定资源的新位置 |
| 411 | Length Required | [[RFC7231, Section 6.5.10](http://www.iana.org/go/rfc7231)] | 服务器拒绝在没有定义  `Content-Length`  头的情况下接受请求。在添加了表明请求消息体长度的有效  `Content-Length`  头之后，客户端可以再次提交该请求。 |
| 412 | Precondition Failed | [[RFC7232, Section 4.2](http://www.iana.org/go/rfc7232)][[RFC8144, Section 3.2](http://www.iana.org/go/rfc8144)] | 客户端请求信息的先决条件错误 |
| 413 | Payload Too Large | [[RFC7231, Section 6.5.11](http://www.iana.org/go/rfc7231)] | 由于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。如果只是服务器暂时无法处理，则会包含一个 Retry-After 的响应信息 |
| 414 | URI Too Long | [[RFC7231, Section 6.5.12](http://www.iana.org/go/rfc7231)] | 请求的 URI 过长（URI 通常为网址），服务器无法处理。 比较少见，通常的情况包括：本应使用 POST 方法的表单提交变成了 GET 方法，导致查询字符串（Query String）过长。 |
| 415 | Unsupported Media Type | [[RFC7231, Section 6.5.13](http://www.iana.org/go/rfc7231)][[RFC7694, Section 3](http://www.iana.org/go/rfc7694)] | 服务器无法处理请求附带的媒体格式 |
| 416 | Range Not Satisfiable | [[RFC7233, Section 4.4](http://www.iana.org/go/rfc7233)] | 客户端请求的范围无效 |
| 417 | Expectation Failed | [[RFC7231, Section 6.5.14](http://www.iana.org/go/rfc7231)] | 服务器无法满足 Expect 的请求头信息 |
| 418-420 | Unassigned |  |  |
| 421 | Misdirected Request | [[RFC7540, Section 9.1.2](http://www.iana.org/go/rfc7540)] | 该请求针对的是无法产生响应的服务器。 这可以由服务器发送，该服务器未配置为针对包含在请求 URI 中的方案和权限的组合产生响应。 |
| 422 | Unprocessable Entity | [[RFC4918](http://www.iana.org/go/rfc4918)] | 请求格式良好，但由于语义错误而无法遵循。 |
| 423 | Locked | [[RFC4918](http://www.iana.org/go/rfc4918)] | 正在访问的资源被锁定。 |
| 424 | Failed Dependency | [[RFC4918](http://www.iana.org/go/rfc4918)] | 由于先前的请求失败，所以此次请求失败。 |
| 425 | Too Early | [[RFC-ietf-httpbis-replay-04](http://www.iana.org/go/draft-ietf-httpbis-replay-04)] |  |
| 426 | Upgrade Required | [[RFC7231, Section 6.5.15](http://www.iana.org/go/rfc7231)] | 服务器拒绝使用当前协议执行请求，但可能在客户机升级到其他协议后愿意这样做。 服务器在 426 响应中发送 Upgrade 头以指示所需的协议。 |
| 427 | Unassigned |  |  |
| 428 | Precondition Required | [[RFC6585](http://www.iana.org/go/rfc6585)] | 原始服务器要求该请求是有条件的。 旨在防止“丢失更新”问题，即客户端获取资源状态，修改该状态并将其返回服务器，同时第三方修改服务器上的状态，从而导致冲突。 |
| 429 | Too Many Requests | [[RFC6585](http://www.iana.org/go/rfc6585)] | 用户在给定的时间内发送了太多请求（“限制请求速率”）。 |
| 430 | Unassigned |  |  |
| 431 | Request Header Fields Too Large | [[RFC6585](http://www.iana.org/go/rfc6585)] | 服务器不愿意处理请求，因为它的 请求头字段太大（ Request Header Fields Too Large）。 请求可以在减小请求头字段的大小后重新提交。 |
| 432-450 | Unassigned |  |  |
| 451 | Unavailable For Legal Reasons | [[RFC7725](http://www.iana.org/go/rfc7725)] | 用户请求非法资源，例如：由政府审查的网页。 |
| 452-499 | Unassigned |  |  |
| 500 | Internal Server Error | [[RFC7231, Section 6.6.1](http://www.iana.org/go/rfc7231)] | 服务器内部错误，无法完成请求 |
| 501 | Not Implemented | [[RFC7231, Section 6.6.2](http://www.iana.org/go/rfc7231)] | 服务器不支持请求的功能，无法完成请求。 只有`GET`和`HEAD`是要求服务器支持的，它们必定不会返回此错误代码。 |
| 502 | Bad Gateway | [[RFC7231, Section 6.6.3](http://www.iana.org/go/rfc7231)] | 充当网关或代理的服务器，从远端服务器接收到了一个无效的请求 |
| 503 | Service Unavailable | [[RFC7231, Section 6.6.4](http://www.iana.org/go/rfc7231)] | 由于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的 Retry-After 头信息中 |
| 504 | Gateway Timeout | [[RFC7231, Section 6.6.5](http://www.iana.org/go/rfc7231)] | 充当网关或代理的服务器，未及时从远端服务器获取请求 |
| 505 | HTTP Version Not Supported | [[RFC7231, Section 6.6.6](http://www.iana.org/go/rfc7231)] | 服务器不支持请求的 HTTP 协议的版本，无法完成处理 |
| 506 | Variant Also Negotiates | [[RFC2295](http://www.iana.org/go/rfc2295)] | 服务器有一个内部配置错误：对请求的透明内容协商导致循环引用。 |
| 507 | Insufficient Storage | [[RFC4918](http://www.iana.org/go/rfc4918)] | 服务器有内部配置错误：所选的变体资源被配置为参与透明内容协商本身，因此不是协商过程中的适当端点。 |
| 508 | Loop Detected | [[RFC5842](http://www.iana.org/go/rfc5842)] | 服务器在处理请求时检测到无限循环。 |
| 509 | Unassigned |  |  |
| 510 | Not Extended | [[RFC2774](http://www.iana.org/go/rfc2774)] | 服务器需要对请求进一步扩展才能实现它。 |
| 511 | Network Authentication Required | [[RFC6585](http://www.iana.org/go/rfc6585)] | 511 状态码指示客户端需要进行身份验证才能获得网络访问权限。 |
| 512-599 | Unassigned |  |  |

[http-status-codes]: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
[http状态码]: http://www.runoob.com/http/http-status-codes.html
[http 响应代码]: https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status

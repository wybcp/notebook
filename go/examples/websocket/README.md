# WebSocket

- 浏览器支持 socket 编程，轻松维持服务端的长连接
- 基于 TCP 可靠协议
- 开发语言提供高度抽象的编程接口，开发成本低
- Websocket 通过 HTTP/1.1 协议的 101 状态码进行握手。

WebSocket 是一种在单个 TCP 连接上进行全双工通信的协议。WebSocket 通信协议于 2011 年被 IETF 定为标准 RFC 6455，并由 RFC7936 补充规范。WebSocket API 也被 W3C 定为标准。

协议共有 14 个部分，其中包括协议背景与介绍、握手、设计理念、术语约定、双端要求、掩码以及连接关闭等内容。

## 握手

`客户端 - 发起握手请求 - 服务器接到请求后返回信息 - 连接建立成功 - 消息互通`

### 握手 - 客户端

WebSocket 握手时使用的并不是 WebSocket 协议，而是 HTTP 协议，握手时发出的请求可以叫做升级请求。客户端在握手阶段通过：

- Upgrade: websocket
- Connection: Upgrade

  Connection 和 Upgrade 这两个头域告知服务端，要求将通信的协议转换为 websocket。

- Sec-WebSocket-Version：通信版本
- Sec-WebSocket-Protocol：协议约定，

WebSocket 使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在 WebSocket API 中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。

### 握手 - 服务端

客户端发出一个 HTTP 请求，表明想要握手，服务端需要对信息进行验证，确认以后才算握手成功（连接建立成功，可以双向通信），然后服务端会给客户端

    Status Code: 101 Web Socket Protocol Handshake Sec-WebSocket-Accept: T5ar3gbl3rZJcRmEmBT8vxKjdDo= Upgrade: websocket Connection: Upgrade

首先，服务端会给出状态码，101 状态码表示服务器已经理解了客户端的请求，并且回复 Connection 和 Upgrade 表示已经切换成 websocket 协议。Sec-WebSocket-Accept 则是经过服务器确认，并且加密过后的 Sec-WebSocket-Key。

## 数据交流

协议中规定传输时并不是直接使用 unicode 编码进行传输，而是使用帧(frame)，数据帧协议定义了带有操作码的帧类型，有效载荷长度，以及“扩展数据”和的指定位置应用程序数据”，它们共同定义“有效载荷数据”。某些位和操作码保留用于将来的扩展协议。

帧由以下几部分组成：FIN、RSV1、RSV2、RSV3、opcode、MASK、Payload length、Masking-key、Payload-Data。它们的含义和作用如下：

1. FIN: 占 1bit

   0：不是消息的最后一个分片
   1：是消息的最后一个分片

2. RSV1, RSV2, RSV3：各占 1bit

   一般情况下全为 0。当客户端、服务端协商采用 WebSocket 扩展时，这三个标志位可以非 0，且值的含义由扩展进行定义。如果出现非零的值，且并没有采用 WebSocket 扩展，连接出错。

3. Opcode: 4bit

   - %x0：表示一个延续帧。当 Opcode 为 0 时，表示本次数据传输采用了数据分片，当前收到的数据帧为其中一个数据分片；
   - %x1：表示这是一个文本帧（text frame）；
   - %x2：表示这是一个二进制帧（binary frame）；
   - %x3-7：保留的操作代码，用于后续定义的非控制帧；
   - %x8：表示连接断开；
   - %x9：表示这是一个心跳请求（ping）；
   - %xA：表示这是一个心跳响应（pong）；
   - %xB-F：保留的操作代码，用于后续定义的控制帧。

4. Mask: 1bit

   表示是否要对数据载荷进行掩码异或操作。

   - 0：否
   - 1：是

5. Payload length: 7bit or (7 + 16)bit or (7 + 64)bit

   表示数据载荷的长度。

   - 0~126：数据的长度等于该值；
   - 126：后续 2 个字节代表一个 16 位的无符号整数，该无符号整数的值为数据的长度；
   - 127：后续 8 个字节代表一个 64 位的无符号整数（最高位为 0），该无符号整数的值为数据的长度。

6. Masking-key: 0 or 4bytes

   当 Mask 为 1，则携带了 4 字节的 Masking-key；

   当 Mask 为 0，则没有 Masking-key。

   掩码算法：按位做循环异或运算，先对该位的索引取模来获得 Masking-key 中对应的值 x，然后对该位与 x 做异或，从而得到真实的 byte 数据。

   注意：掩码的作用并不是为了防止数据泄密，而是为了防止早期版本的协议中存在的代理缓存污染攻击（proxy cache poisoning attacks）等问题。

7. Payload Data: 载荷数据

   双端接收到数帧之后，就可以根据数据帧各个位置的值进行处理或信息提取。

从客户端向服务端发送数据时，需要对数据进行掩码操作；从服务端向客户端发送数据时，不需要对数据进行掩码操作。如果服务端接收到的数据没有进行过掩码操作，服务端需要断开连接。如果 Mask 是 1，那么在 Masking-key 中会定义一个掩码键（masking key），并用这个掩码键来对数据载荷进行反掩码。所有客户端发送到服务端的数据帧，Mask 都是 1。

## 保持连接

刚才提到 WebSocket 协议是双向通信的，那么一旦连接上，就不会断开了吗？

事实上确实是这样，但是服务端不可能让所有的连接都一直保持，所以服务端通常会在一个定期的时间给客户端发送一个 ping 帧，而客户端收到 Ping 帧后则回复一个 Pong 帧，如果客户端不响应，那么服务端就会主动断开连接。

opcode 帧为 0x09 则代表这是一个 Ping ，为 0x0A 则代表这是一个 Pong。

## 优点

开销少、时时性高、二进制支持完善、支持扩展、压缩更优。

- 较少的控制开销。在连接创建后，服务器和客户端之间交换数据时，用于协议控制的数据包头部相对较小。在不包含扩展的情况下，对于服务器到客户端的内容，此头部大小只有 2 至 10 字节（和数据包长度有关）；对于客户端到服务器的内容，此头部还需要加上额外的 4 字节的掩码。相对于 HTTP 请求每次都要携带完整的头部，此项开销显著减少了。

- 更强的实时性。由于协议是全双工的，所以服务器可以随时主动给客户端下发数据。相对于 HTTP 请求需要等待客户端发起请求服务端才能响应，延迟明显更少；即使是和 Comet 等类似的长轮询比较，其也能在短时间内更多次地传递数据。
  保持连接状态。与 HTTP 不同的是，Websocket 需要先创建连接，这就使得其成为一种有\* 状态的协议，之后通信时可以省略部分状态信息。而 HTTP 请求可能需要在每个请求都携带状态信息（如身份认证等）。

- 更好的二进制支持。Websocket 定义了二进制帧，相对 HTTP，可以更轻松地处理二进制内容。

- 可以支持扩展。Websocket 定义了扩展，用户可以扩展协议、实现部分自定义的子协议。如部分浏览器支持压缩等。

- 更好的压缩效果。相对于 HTTP 压缩，Websocket 在适当的扩展支持下，可以沿用之前内容的上下文，在传递类似的数据时，可以显著地提高压缩率。

## go

使用 websocket.Upgrade 完成协议握手，得到 websocket 的长连接。

## 日志监控

[grafana](https://github.com/grafana/grafana)前端面板，The tool for beautiful monitoring and metric analytics & dashboards for Graphite,

[influxdata](https://www.influxdata.com/)时间序列数据库。

## [Gorilla WebSocket](https://github.com/gorilla/websocket)

a Go implementation of the WebSocket protocol

## 参考

- [WebSocket 从入门到写出开源库](https://mp.weixin.qq.com/s/3x6hUCAyGymLYXRNHD5qRQ)

- [Socket 编程](https://astaxie.gitbooks.io/build-web-application-with-golang/content/zh/08.1.html)

# [HTTP2](https://tools.ietf.org/html/rfc7540)

- **新的二进制格式**（Binary Format），HTTP1.x 的解析是基于文本。基于文本协议的格式解析存在天然缺陷，文本的表现形式有多样性，要做到健壮性考虑的场景必然很多，二进制则不同，只认 0 和 1 的组合。基于这种考虑 HTTP2.0 的协议解析决定采用二进制格式，实现方便且健壮。
  - Frame，帧，HTTP/2 协议里通信的最小单位，每个帧有自己的格式，不同类型的帧负责传输不同的消息
  - Message, 消息，类似 Request/Response 消息，每个消息包含一个或多个帧
  - Stream，流，建立链接后的一个双向字节流，用来传输消息，每次传输的是一个或多个帧
- **多路复用**（MultiPlexing），即连接共享，即每一个 request 都是是用作连接共享机制的。一个 request 对应一个 id，这样一个连接上可以有多个 request，每个连接的 request 可以随机的混杂在一起，接收方可以根据 request 的 id 将 request 再归属到各自不同的服务端请求里面。**多路复用原理图**：
- **header 压缩，**如上文中所言，对前面提到过 HTTP1.x 的 header 带有大量信息，而且每次都要重复发送，HTTP2.0 使用 encoder 来减少需要传输的 header 大小，通讯双方各自 cache 一份 header fields 表，既避免了重复 header 的传输，又减小了需要传输的大小。
- **服务端推送**（server push），HTTP2.0 也具有 server push 功能。目前，有大多数网站已经启用 HTTP2.0，例如[YouTuBe](https://www.youtube.com/)，[淘宝网](http://www.taobao.com/)等网站

![HTTP2](http://tenny.qiniudn.com/diff332.png)

[HTTP/2 in GO(一)](https://mp.weixin.qq.com/s?__biz=MzU4ODgyMDI0Mg==&mid=2247485964&idx=1&sn=72e023c275ef6893132439ab69b21430&chksm=fdd7b071caa039678a3809ca49f93ac26bbb7fd4f278997c7a3dbb0501072e597fbbf5b4a603&scene=21#wechat_redirect)

[HTTP/2 in GO(二)](https://mp.weixin.qq.com/s/eBhWbwv7UDhMFSeZFEOiHQ)

# [gRPC](https://grpc.io/)

gRPC 是一个高性能、开源和通用的 RPC 框架，面向移动和 HTTP/2 设计

在`.proto`文件目录执行：
`protoc --go_out=plugins=grpc:. *.proto`

- metadata：定义了 grpc 所支持的元数据结构，包中方法可以对 MD 进行获取和处理
- credentials：实现了 grpc 所支持的各种认证凭据，封装了客户端对服务端进行身份验证所需要的所有状态，并做出各种断言
- codes：定义了 grpc 使用的标准错误码，可通用

## 多语言

- C++
- C#
- Dart
- Go
- Java
- Node.js
- Objective-C
- PHP
- Python
- Ruby

## 特点

1. HTTP/2
2. Protobuf
3. 客户端、服务端基于同一份 IDL
4. 移动网络的良好支持
5. 支持多语言

## gRPC 流

- Server-side streaming RPC：服务器端流式 RPC

  单向流，并代指 Server 为 Stream 而 Client 为普通 RPC 请求。客户端发起一次普通的 RPC 请求，服务端通过流式响应多次发送数据集，客户端 Recv 接收数据集。

- Client-side streaming RPC：客户端流式 RPC

  单向流，客户端通过流式发起多次 RPC 请求给服务端，服务端发起一次响应给客户端

- Bidirectional streaming RPC：双向流式 RPC

  双向流。由客户端以流式的方式发起请求，服务端同样以流式的方式响应请求
  首个请求一定是 Client 发起，但具体交互方式（谁先谁后、一次发多少、响应多少、什么时候关闭）根据程序编写的方式来确定（可以结合协程）

gRPC Streaming 是基于 HTTP/2 ，应用于大规模数据包、实时场景等。

## stream server

### SendMsg 方法

该方法涉及以下过程:

- 消息体（对象）序列化
- 压缩序列化后的消息体
- 对正在传输的消息体增加 5 个字节的 header
- 判断压缩+序列化后的消息体总字节长度是否大于预设的 maxSendMessageSize（预设值为 math.MaxInt32），若超出则提示错误
- 写入给流的数据集

### SendAndClose

当发现 io.EOF (流关闭) 后，需要将最终的响应结果发送给客户端，同时关闭正在另外一侧等待的 Recv

## stream clent

RecvMsg 会从流中读取完整的 gRPC 消息体，另外通过阅读源码可得知：

- RecvMsg 是阻塞等待的
- RecvMsg 当流成功/结束（调用了 Close）时，会返回 io.EOF
- RecvMsg 当流出现任何错误时，流会被中止，错误信息会包含 RPC 错误码。而在 RecvMsg 中可能出现如下错误：

      - io.EOF
      - io.ErrUnexpectedEOF
      - transport.ConnectionError
      - google.golang.org/grpc/codes

  同时需要注意，默认的 MaxReceiveMessageSize 值为 `1024*1024*4`，建议不要超出

## [制作证书](https://segmentfault.com/a/1190000013408485#articleHeader3)

## ca 证书

`tls.LoadX509KeyPair()`：从证书相关文件中读取和解析信息，得到证书公钥、密钥对

`x509.NewCertPool()`：创建一个新的、空的 CertPool

`certPool.AppendCertsFromPEM()`：尝试解析所传入的 PEM 编码的证书。如果解析成功会将其加到 CertPool 中，便于后面的使用

`credentials.NewTLS`：构建基于 TLS 的 TransportCredentials 选项

tls.Config：Config 结构用于配置 TLS 客户端或服务器,在 Server，共使用了三个 Config 配置项：

1. Certificates：设置证书链，允许包含一个或多个
2. ClientAuth：要求必须校验客户端的证书。可以根据实际情况选用以下参数：

   const (
   NoClientCert ClientAuthType = iota
   RequestClientCert
   RequireAnyClientCert
   VerifyClientCertIfGiven
   RequireAndVerifyClientCert
   )

3. ClientCAs：设置根证书的集合，校验方式使用 ClientAuth 中设定的模式

## 拦截器（interceptor）

用于在每个 RPC 方法的前或后做某些事情。

- 普通方法：一元拦截器（grpc.UnaryInterceptor）
- 流方法：流拦截器（grpc.StreamInterceptor）

### 实现多个拦截器

gRPC 本身只能设置一个拦截器，采用开源项目 [go-grpc-middleware](https://github.com/grpc-ecosystem/go-grpc-middleware)实现多个拦截器

## HTTP 接口

关键一点，gRPC 的协议是基于 HTTP/2 的，因此应用程序能够在单个 TCP 端口上提供 HTTP/1.1 和 gRPC 接口服务（两种不同的流量）

## 自定义认证的接口

```go
type PerRPCCredentials interface {
    GetRequestMetadata(ctx context.Context, uri ...string) (map[string]string, error)
    RequireTransportSecurity() bool
}
```

在 gRPC 中默认定义了 PerRPCCredentials，是 gRPC 默认提供用于自定义认证的接口，它的作用是将所需的安全认证信息添加到每个 RPC 方法的上下文中。其包含 2 个方法：

- GetRequestMetadata：获取当前请求认证所需的元数据（metadata）
- RequireTransportSecurity：是否需要基于 TLS 认证进行安全传输

## [Deadlines](https://grpc.io/blog/deadlines)

Deadlines 意指截止时间，在 gRPC 中强调 TL;DR（Too long, Don't read）并建议始终设定截止日期。

为什么要设置？

    当未设置 Deadlines 时，将采用默认的 DEADLINE_EXCEEDED（这个时间非常大），如果产生了阻塞等待，就会造成大量正在进行的请求都会被保留，并且所有请求都有可能达到最大超时，这会使服务面临资源耗尽的风险，例如内存，这会增加服务的延迟，或者在最坏的情况下可能导致整个进程崩溃

`context.WithDeadline`：会返回最终上下文截止时间。第一个形参为父上下文，第二个形参为调整的截止时间。若父级时间早于子级时间，则以父级时间为准，否则以子级时间为最终截止时间

`context.WithTimeout`：很常见的另外一个方法，是便捷操作。实际上是对于 WithDeadline 的封装

## OpenTracing

OpenTracing 通过提供平台无关、厂商无关的 API，使得开发人员能够方便的添加（或更换）追踪系统的实现

- Trace:一个 trace 代表了一个事务或者流程在（分布式）系统中的执行过程
- Span:一个 span 代表在分布式系统中完成的单个工作单元。也包含其他 span 的 “引用”，这允许将多个 spans 组合成一个完整的 Trace,每个 span 根据 OpenTracing 规范封装以下内容：

      - 操作名称
      - 开始时间和结束时间
      - key:value span Tags
      - key:value span Logs
      - SpanContext

- Tags:Span tags（跨度标签）可以理解为用户自定义的 Span 注释。便于查询、过滤和理解跟踪数据
- Logs:Span logs（跨度日志）可以记录 Span 内特定时间或事件的日志信息。主要用于捕获特定 Span 的日志信息以及应用程序本身的其他调试或信息输出
- SpanContext:SpanContext 代表跨越进程边界，传递到子级 Span 的状态。常在追踪示意图中创建上下文时使用
- Baggage Items:Baggage Items 可以理解为 trace 全局运行中额外传输的数据集合

## [Zipkin](https://github.com/openzipkin/zipkin)

Zipkin 是分布式追踪系统。它的作用是收集解决微服务架构中的延迟问题所需的时序数据。它管理这些数据的收集和查找

Zipkin 的设计基于 Google Dapper 论文。

初始化 Zipkin，包含收集器、记录器、跟踪器。再利用拦截器在 Server 端实现 SpanContext、Payload 的双向读取和管理

- zipkin.NewHTTPCollector：创建一个 Zipkin HTTP 后端收集器
- zipkin.NewRecorder：创建一个基于 Zipkin 收集器的记录器
- zipkin.NewTracer：创建一个 OpenTracing 跟踪器（兼容 Zipkin Tracer）
- otgrpc.OpenTracingClientInterceptor：返回 grpc.UnaryServerInterceptor，不同点在于该拦截器会在 gRPC Metadata 中查找 OpenTracing SpanContext。如果找到则为该服务的 Span Context 的子节点
- otgrpc.LogPayloads：设置并返回 Option。作用是让 OpenTracing 在双向方向上记录应用程序的有效载荷（payload）

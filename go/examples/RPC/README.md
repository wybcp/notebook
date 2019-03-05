# RPC

RPC 是远程过程调用的缩写（Remote Procedure Call），通俗地说就是调用远处的一个函数。因为 RPC 涉及的函数可能非常之远，远到它们之间说着完全不同的语言，语言就成了两边的沟通障碍。而 Protobuf 因为支持多种不同的语言（甚至不支持的语言也可以扩展支持），其本身特性也非常方便描述服务的接口（也就是方法列表），因此非常适合作为 RPC 世界的接口交流语言。

Go 语言的 RPC 规则：方法只能有两个可序列化的参数，其中第二个参数是指针类型，并且返回一个 error 类型，同时必须是公开的方法。

远程过程调用是一个分布式计算的客户端-服务器（Client/Server）的例子。远程过程调用总是由客户端对服务器发出一个执行若干过程请求，并用客户端提供的参数。执行结果将返回给客户端。

产品级的 RPC 框架除了点对点的 RPC 协议的具体实现外，还应包括服务的发现与注销、提供服务的多台 Server 的负载均衡、服务的高可用等更多的功能。 目前的 RPC 框架大致有两种不同的侧重方向，一种偏重于服务治理，另一种偏重于跨语言调用。

RPC 的消息传输可以通过 TCP、UDP 或者 HTTP 等，所以有时候我们称之为 RPC over TCP、 RPC over HTTP。

## RPC 调用过程

服务的调用过程为：

1. client 调用 client stub，这是一次本地过程调用
1. client stub 将参数打包成一个消息，然后发送这个消息。打包过程也叫做 marshalling
1. client 所在的系统将消息发送给 server
1. server 的的系统将收到的包传给 server stub
1. server stub 解包得到参数。 解包也被称作 unmarshalling
1. 最后 server stub 调用服务过程。返回结果按照相反的步骤传给 client

## [gRPC](gRPC.md)

gRPC 是 Google 开发的高性能、通用的开源 RPC 框架，其由 Google 主要面向移动应用开发并基于 HTTP/2 协议标准而设计，基于 ProtoBuf(Protocol Buffers)序列化协议开发，且支持众多开发语言。它的目标的跨语言开发，支持多种语言，服务治理方面需要自己去实现，所以要实现一个综合的产品级的分布式 RPC 平台还需要扩展开发。

## [Protobuf](protobuf.md)

Protocol Buffers 是一种与语言、平台无关，可扩展的序列化结构化数据的方法。

## [Go RPC 开发指南-RPCX 框架](https://books.studygolang.com/go-rpc-programming-guide/)

[带入 gRPC](https://github.com/EDDYCJY/blog)

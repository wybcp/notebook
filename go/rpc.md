# RPC

RPC 是远程过程调用的缩写（Remote Procedure Call），通俗地说就是调用远处的一个函数。因为 RPC 涉及的函数可能非常之远，远到它们之间说着完全不同的语言，语言就成了两边的沟通障碍。而 Protobuf 因为支持多种不同的语言（甚至不支持的语言也可以扩展支持），其本身特性也非常方便描述服务的接口（也就是方法列表），因此非常适合作为 RPC 世界的接口交流语言。

Go 语言的 RPC 规则：方法只能有两个可序列化的参数，其中第二个参数是指针类型，并且返回一个 error 类型，同时必须是公开的方法。

## [Go RPC 开发指南](https://books.studygolang.com/go-rpc-programming-guide/)
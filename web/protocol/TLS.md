# TLS

[**传输层安全性协议**](https://zh.wikipedia.org/wiki/%E5%82%B3%E8%BC%B8%E5%B1%A4%E5%AE%89%E5%85%A8%E6%80%A7%E5%8D%94%E5%AE%9A)(Transport Layer Security，简称 **TLS**)是一种[安全协议](https://zh.wikipedia.org/wiki/%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE)，目的是为互联网通信，提供安全及数据完整性保障。

SSL包含记录层（Record Layer）和传输层，记录层协议确定传输层数据的封装格式。传输层安全协议使用[X.509](https://zh.wikipedia.org/wiki/X.509)认证，之后利用非对称加密演算来对通信方做身份认证，之后交换对称密钥作为会谈密钥（[Session key](https://zh.wikipedia.org/wiki/Session_key)）。这个会谈密钥是用来将通信两方交换的数据做加密，保证两个应用间通信的保密性和可靠性，使客户与服务器应用之间的通信不被攻击者窃听。

## TLS 1.3

TLS 1.3 已经被 IESG  正式批准为[建议标准](https://datatracker.ietf.org/doc/draft-ietf-tls-tls13/)了,版本为 Draft-28。

TLS 1.3 最大优势是：安全性增强、访问速度更快。

## TLS 1.3 与 TLS 1.2对比

## 测试工具

https://www.ssllabs.com/ssltest/
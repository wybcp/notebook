# HTTPS

## HTTPS 与 HTTP 的一些区别

1. HTTPS 协议需要到 CA 申请证书
2. HTTP 协议运行在 TCP 之上，所有传输的内容都是明文，HTTPS 运行在 SSL/TLS 之上，SSL/TLS 运行在 TCP 之上，所有传输的内容都经过加密的。
3. HTTP 和 HTTPS 使用的是完全不同的连接方式，用的端口也不一样，前者是 80，后者是 443。
4. HTTPS 可以有效的防止运营商劫持，解决了防劫持的一个大问题。

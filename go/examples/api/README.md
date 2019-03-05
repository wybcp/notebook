# [基于 Go 语言构建企业级的 RESTful API 服务](https://juejin.im/book/5b0778756fb9a07aa632301e)

掘金上面的 go api 项目，基于 REST + JSON

## 启动健康自检

在启动 HTTP 端口前 go 一个 pingServer 协程，启动 HTTP 端口后，该协程不断地 ping 一个路径，如果失败次数超过一定次数，则终止 HTTP 服务器进程。通过自检可以最大程度地保证启动后的 API 服务器处于健康状态。

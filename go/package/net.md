# net

使用这些包可以更简单地用网络收发信息，还可以建立更底层的网络连接，编写服务器程序。

## net/http

[Go 语言经典库使用分析（七）| 高性能可扩展 HTTP 路由 httprouter](https://www.flysnow.org/2019/01/07/golang-classic-libs-httprouter.html)

### 缺点

- 不能单独的对请求方法(POST,GET 等)注册特定的处理函数
- 不支持 Path 变量参数
- 不能自动对 Path 进行校准
- 性能一般
- 扩展性不足

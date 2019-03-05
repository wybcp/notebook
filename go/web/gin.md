# [gin](https://gin-gonic.github.io/gin/)

Gin 插件式轻量级框架，具有如下优点：高性能、扩展性强、稳定性强、相对而言比较简洁

- [Golang 微框架 Gin 简介](https://www.jianshu.com/p/a31e4ee25305)
- [golang123 是使用 vue、nuxt、node.js 和 golang 开发的知识分享系统 https://www.golang123.com/](https://github.com/shen100/golang123)
- [轻量级 Web 框架 Gin 结构分析](https://juejin.im/post/5c7c923cf265da2dce1f5fe8)

## gin.Engine

Engine 是 Gin 框架最重要的数据结构，它是框架的入口。通过 Engine 对象来定义服务路由信息、组装插件、运行服务。

Engine 对象很简单，因为底层的 HTTP 服务器使用的是 Go 语言内置的 http server，Engine 的本质只是对内置的 HTTP 服务器的包装，让它使用起来更加便捷。

### gin.Default()

gin.Default() 函数会生成一个默认的 Engine 对象，里面包含了 2 个默认的常用插件，分别是 Logger 和 Recovery，Logger 用于输出请求日志，Recovery 确保单个请求发生 panic 时记录异常堆栈日志，输出统一的错误响应。

```go
// Default returns an Engine instance with the Logger and Recovery middleware already attached.
func Default() *Engine {
	debugPrintWARNINGDefault()
	engine := New()
	engine.Use(Logger(), Recovery())
	return engine
}

```

## 路由

GetHeader()：获取 HTTP 头

### 路由方法

IRouter 接口

```go
// IRoutes defines all router handle interface.
	Handle(string, string, ...HandlerFunc) IRoutes
	Any(string, ...HandlerFunc) IRoutes
	GET(string, ...HandlerFunc) IRoutes
	POST(string, ...HandlerFunc) IRoutes
	DELETE(string, ...HandlerFunc) IRoutes
	PATCH(string, ...HandlerFunc) IRoutes
	PUT(string, ...HandlerFunc) IRoutes
	OPTIONS(string, ...HandlerFunc) IRoutes
	HEAD(string, ...HandlerFunc) IRoutes

	StaticFile(string, string) IRoutes
	Static(string, string) IRoutes
	StaticFS(string, http.FileSystem) IRoutes
```

### 路由参数

- 冒号`:`加上一个参数名组成路由参数。可以使用 c.Params 的方法读取其值。
- `*`号处理参数

## gin.Context

保存了请求的上下文信息，它是所有请求处理器的入口参数。

gin 进行了封装，把 request 和 response 都封装到 gin.Context 的上下文环境。

Context 对象提供了非常丰富的方法用于获取当前请求的上下文信息，如果你需要获取请求中的 URL 参数、Cookie、Header 都可以通过 Context 对象来获取。

### query string

`/welcome?firstname=Jane&lastname=Doe`

对于参数的处理，经常会出现参数不存在的情况。

- `c.DefaultQuery`方法读取参数，其中当参数不存在的时候，提供一个默认值。空值也是值，DefaultQuery 只作用于 key 不存在的时候，提供默认值。
- `c.Query` 方法读取正常参数，当参数不存在的时候，返回空字串：

### HandlersChain

Gin 提供了插件，只有函数链的尾部是业务处理，前面的部分都是插件函数。在 Gin 中插件和业务处理函数形式是一样的，都是 func(\*Context)。当我们定义路由时，Gin 会将插件函数和业务处理函数合并在一起形成一个链条结构。

Gin 还支持 Abort() 方法中断请求链的执行，它的原理是将 Context.index 调整到一个比较大的数字，这样 Next() 方法中的调用循环就会立即结束。需要注意的 Abort() 方法并不是通过 panic 的方式中断执行流，执行 Abort() 方法之后，当前函数内后面的代码逻辑还会继续执行。

## 插件 中间件

RouterGroup 提供了 Use() 方法来注册插件

## [binding](https://github.com/gin-gonic/gin/blob/master/binding/binding.go#L48) 映射绑定

[model-binding-and-validation](https://github.com/gin-gonic/gin#model-binding-and-validation)

If `GET` method , only `Form` binding engine (`query`) used.

你可以使用直接指定 BindJSON 处理 json 请求格式

    //使用默认的bind ，get方法只处理 form 格式
    //if err := c.Bind(&r); err != nil {
    //使用默认的BindJSON ，get方法keyi处理 json 格式

If `POST`, first checks the `content-type` for `JSON` or `XML`, then uses `Form` (`form-data`).
// See more at https://github.com/gin-gonic/gin/blob/master/binding/binding.go#L48

Context.ShouldBind 是比较柔和的校验方法，它只负责校验，并将校验结果以返回值的形式传递给上层，遇到校验不通过时，会返回一个错误对象告知调用者校验失败的原因。Context 还有另外一个比较暴力的校验方法 Context.Bind，它和 ShouldBind 的调用形式一摸一样，区别是当校验错误发生时，它会调用 Abort() 方法中断调用链的执行，向客户端返回一个 HTTP 400 Bad Request 错误。

## 返回

gin.H 是 map[string]interface{} 的一个快捷名称

## 自带的 log

将 log 记录到文件

```go
// Disable Console Color, you don't need console color when writing the logs to file.
gin.DisableConsoleColor()

// Logging to a file.
f, _ := os.Create("gin.log")
gin.DefaultWriter = io.MultiWriter(f)

// Use the following code if you need to write the logs to file and console at the same time.
// gin.DefaultWriter = io.MultiWriter(f, os.Stdout)
```

定制日志格式

```go
router := gin.New()

// LoggerWithFormatter middleware will write the logs to gin.DefaultWriter
// By default gin.DefaultWriter = os.Stdout
router.Use(gin.LoggerWithFormatter(func(param gin.LogFormatterParams) string {

	// your custom format
	return fmt.Sprintf("%s - [%s] \"%s %s %s %d %s \"%s\" %s\"\n",
			param.ClientIP,
			param.TimeStamp.Format(time.RFC1123),
			param.Method,
			param.Path,
			param.Request.Proto,
			param.StatusCode,
			param.Latency,
			param.Request.UserAgent(),
			param.ErrorMessage,
	)
}))
```

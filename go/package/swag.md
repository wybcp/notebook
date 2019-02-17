# [swag](https://github.com/swaggo/swag)

Swagger 是一个强大的 API 文档构建工具，可以自动为 RESTful API 生成 Swagger 格式的文档，可以在浏览器中查看 API 文档，也可以通过调用接口来返回 API 文档（JSON 格式）。Swagger 通常会展示如下信息：

- HTTP 方法（GET、POST、PUT、DELETE 等）
- URL 路径
- HTTP 消息体（消息体中的参数名和类型）
- 参数位置
- 参数是否必选
- 返回的参数（参数名和类型）
- 请求和返回的媒体类型
- 可以通过 API 文档描述的参数来构建请求，测试 API。

## 安装

```sh
go get -u github.com/swaggo/swag/cmd/swag
```

gin-swagger

```sh
go get -u github.com/swaggo/gin-swagger

go get -u github.com/swaggo/gin-swagger/swaggerFiles
```

[gin example](https://github.com/EDDYCJY/blog/blob/master/golang/gin/2018-03-18-Gin%E5%AE%9E%E8%B7%B5-%E8%BF%9E%E8%BD%BD%E5%85%AB-%E4%B8%BA%E5%AE%83%E5%8A%A0%E4%B8%8ASwagger.md)

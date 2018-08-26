# go

Go 是一门编译型，具有静态类型和类 C 语言语法的语言，并且有垃圾回收（GC）机制。编译快。强类型，

## godoc

本地获取文档：

```bash
godoc -http=:6060
```

然后浏览器中访问 `http://localhost:6060`

## [go tour](https://tour.go-zh.org/welcome/3)

用 [go get](https://go-zh.org/cmd/go/) 命令来安装[gotour](https://go-zh.org/x/tour/): `go get github.com/Go-zh/tour/gotour` 最后运行产生的 `gotour` 可执行文件。 如果要运行本教程的英文版，首先请[下载并安装 Go](https://golang.org/dl/)，接着从命令行启动教程： `go tool tour`

## 目录

- [常量](const.md)
- [defer 延迟](defer.md)
- [函数](func.md)
- [go 程](goroutine.md)
- [流程控制](loop-control.md)
- [包](package.md)
- [指针](pointer.md)
- [切片](slice.md)
- [结构体](struct.md)
- [变量](var.md)

## 参考

- [Go 指南](https://tour.go-zh.org/list)

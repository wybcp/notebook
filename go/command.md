# [常见命令](https://golang.google.cn/cmd/go/)

## [build](https://golang.org/pkg/go/build/)

- 运行`go build`命令时加入标记`-x`，这样可以看到`go build`命令具体都执行了哪些操作。另外也可以加入标记`-n`，这样可以只查看具体操作而不执行它们。
- 运行`go build`命令时加入标记`-v`，这样可以看到`go build`命令编译的代码包的名称。它在与`-a`标记搭配使用时很有用。

## [get](https://golang.org/doc/articles/go_command.html#tmp_3)

命令`go get`会自动从一些主流公用代码仓库（比如 GitHub）下载目标代码包，并把它们安装到环境变量`GOPATH`包含的第 1 工作区的相应目录中。如果存在环境变量`GOBIN`，那么仅包含命令源码文件的代码包会被安装到`GOBIN`指向的那个目录。

## run

编译并运行。

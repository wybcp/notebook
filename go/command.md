# [常见命令](https://golang.google.cn/cmd/go/)

## [build](https://golang.org/pkg/go/build/)

- 运行`go build`命令时加入标记`-x`，这样可以看到`go build`命令具体都执行了哪些操作。另外也可以加入标记`-n`，这样可以只查看具体操作而不执行它们。
- 运行`go build`命令时加入标记`-v`，这样可以看到`go build`命令编译的代码包的名称。它在与`-a`标记搭配使用时很有用。

### 跨平台编译

使用 `go env` 查看编译环境，注意里面两个重要的环境变量 GOOS 和 GOARCH：

- `GOOS` 指的是目标操作系统，一共支持 10 种操作系统；
- `GOARCH` 指的是目标处理器的架构，一共支持 9 中处理器的架构

GOOS 和 GOARCH 组合起来，支持生成的可执行程序种类很多，具体组合参考<https://golang.org/doc/install/source#environment>。

    $GOOS    $GOARCH
    android    arm
    darwin    386
    darwin    amd64
    darwin    arm
    darwin	arm64
    dragonfly	amd64
    freebsd	386
    freebsd	amd64
    freebsd	arm
    linux	386
    linux	amd64
    linux	arm
    linux	arm64
    linux	ppc64
    linux	ppc64le
    linux	mips
    linux	mipsle
    linux	mips64
    linux	mips64le
    linux	s390x
    netbsd	386
    netbsd	amd64
    netbsd	arm
    openbsd	386
    openbsd	amd64
    openbsd	arm
    plan9	386
    plan9	amd64
    solaris	amd64
    windows	386
    windows	amd64

生成不同平台架构的可执行程序，改变这两个环境变量，比如要生成 linux 64 位的程序，命令如下：

```sh
GOOS=linux GOARCH=amd64 go build flysnow.org/hello
```

## [get](https://golang.org/doc/articles/go_command.html#tmp_3)

命令`go get`会自动从一些主流公用代码仓库（比如 GitHub）下载目标代码包，并把它们安装到环境变量`GOPATH`包含的第 1 工作区的相应目录中。如果存在环境变量`GOBIN`，那么仅包含命令源码文件的代码包会被安装到`GOBIN`指向的那个目录。

更新全部包

```sh
go get -u all
```

## run

编译并运行。

[Go 语言中自动选择 json 解析库条件编译 tags](https://www.flysnow.org/2017/11/05/go-auto-choice-json-libs.html)

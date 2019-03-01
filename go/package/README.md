# 包

按照约定，包名与导入路径的最后一个元素一致。

## [导入](https://tour.go-zh.org/basics/2)

此代码用圆括号组合了导入，这是“分组”形式的导入语句。

当然你也可以编写多个导入语句，例如：

```go
import "fmt"
import "math"
```

不过使用分组导入语句是更好的形式。

### import 的基本原理

如果一个 main 导入其他包，包将被顺序导入。

如果导入的包中，然后初始化 B 包中的常量与变量，最后如果 B 中有`init()`，会自动执行`init()`；

所有包到入完成之后才会对 main 中常量和变量进行初始化，然后执行 main 中的`init()`（如果存在），最后执行 main 函数；

### import 别名

别名操作的含义是：将导入的包命名为另一个容易记忆的别名`import str "string"`

### 点（`.`）操作

点（`.`）操作的含义是：点（`.`）标识的包导入后，调用该包中函数时可以省略前缀包名；`import . "string"` ###下划线（`_`）操作
下划线（`_`）操作的含义是：导入该包，但不导入整个包，而是执行该包中的 init 函数，因此无法通过包名来调用包中其他的函数。使用下划线（`_`）操作往往是为了注册包里的引擎，让外部可以方便地使用；`import _ "string"`

## 可见性

Go 用了一个简单的规则去定义什么类型和函数可以包外可见。如果类型或者函数名称以一个大写字母开始，它就具有了包外可见性。如果以一个小写字母开始，它就不可以。

在 Go 中，如果一个名字以大写字母开头，那么它就是已导出的。

## 包管理

`go` 命令有一个 `get` 子命令，用于获取第三方库。`go get` 支持除了这个例子中的各种协议，我们可以从 Github 中获取一个库。

在 shell 中输入命令：

```go
go get github.com/mattn/go-sqlite3
```

`go get` 获取远端的文件并把它们存储在你的工作区间中。去看看你的 `$GOPATH/src` 目录，你会发现除了我们创建的 `shopping` 项目之外，还有一个 `github.com` 目录，在里面，你会看到一个包含了 `go-sqlite3`目录的 `mattn` 目录。

我们刚才只是讨论了如何导入我们工作区间的包。为了导入新安装的 `go-sqlite3` 包，我们要这样导入：

```go
import (
  "github.com/mattn/go-sqlite3"
)
```

我知道这看起来像一个 URL，实际上，它只是希望导入在 `$GOPATH/src/github.com/mattn/go-sqlite3` 找到的 `go-sqlite3` 包。

## 常见的包

- [fmt](fmt.md)
- [runtime](runtime.md) go 系统运行时的操作相关

## 著名三方包

- [delve 调试工具](delve.md)
- [Pholcus（幽灵蛛）爬出工具](pholcus.md)
- [logrus 日志系统](logrus.md)
- [go-spew 打印数据的结构](go-spew.md)
- [Web 中间件](negroni.md)
- [生成二维码](go-qrcode.md)
- [gometalinter 静态代码检查](gometalinter.md)本身不做代码检查，而是集成了各种 linter
- [httprouter高性能路由](httprouter.md)

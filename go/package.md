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
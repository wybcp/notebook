# [Modules](https://github.com/golang/go/wiki/Modules)

Go modules 是 Go team 在解决包依赖管理方面的一次勇敢尝试

可以使用 go list 工具查看依赖:

```bash
go list -m all
```

`go mod why -m golang.org/x/sys`解释为什么需要包和模块

`go mod graph` 把模块之间的依赖图显示出来

在使用模块的时候， GOPATH 是无意义的，不过它还是会把下载的依赖储存在 `GOPATH/src/mod` 中，也会把 `go install` 的结果放在 `GOPATH/bin`

`$ go clean -modcache`清空mod 缓存

[Go 包管理解决之道 —— Modules 初试](https://windmt.com/2018/11/08/first-look-go-modules/)

[golang go 包管理工具 go mod 的详细介绍 --- 赶紧拥抱 go mod 吧，go path 的那套东西已经 out 了。](https://www.jianshu.com/p/98082de78a0c)

[go 语言包管理简史](https://tonybai.com/2019/09/21/brief-history-of-go-package-management/)

[Go module 再回顾](https://colobu.com/2019/09/23/review-go-module-again/)

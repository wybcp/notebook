# runtime

## untime.Gosched()

untime.Gosched()用于让出 CPU 时间片。

## [ReadMemStats](https://golang.org/pkg/runtime/#MemStats)

关于内存分配的情况

## [pprof](https://github.com/google/pprof)

PProf 是一个 Go 程序性能分析工具，可以分析 CPU、内存等性能。Go 在语言层面上集成了 profile 采样工具，只需在代码中简单地引入 runtime/ppro 或者 net/http/pprof 包即可获取程序的 profile 文件，并通过该文件来进行性能分析。

### [runtime/pprof](https://golang.org/pkg/runtime/pprof/)

<https://juejin.im/book/5b0778756fb9a07aa632301e/section/5b18630ee51d4506cd4fd834>

查看性能并生成函数调用图
`go test -cpuprofile cpu.prof -memprofile mem.prof -bench .`
例子：

`go test -bench=".*" -cpuprofile=cpu.profile ./util`

[Profiling Go Programs](https://blog.golang.org/profiling-go-programs)
[go tool pprof](https://github.com/hyper0x/go_command_tutorial/blob/master/0.12.md)

### [net/http/pprof](https://golang.org/pkg/net/http/pprof/)

net/http/pprof 中只是使用 runtime/pprof 包来进行封装了一下，并在 HTTP 端口上暴露出来。

## 参考

[Go 调优技术](https://studygolang.com/articles/12008)

# 测试源码

名称以`_test.go`为后缀。其中至少有一个函数的名称以 Test 或 Benchmark 为前缀。该函数接受一个类型为
`*testing.T`或`*testing.B`的参数

```golang
func TestFind(t *testing.T){
    //省略若干条语句
    }
func BenchmarkFind(b *testing.B){
    //省略若干条语句
    }
```

在对应目录下执行命令 `go test -test.bench=".*"`

- `b.ResetTimer()`：重置时间和内存分配计数器，避免忽略设置过程中消耗的时间。
- `b.StartTimer()`：This function is called automatically before a benchmark starts, but it can also be used to resume timing after a call to StopTimer.如果每次循环迭代都有一些开销比较大的设置逻辑，使用这两个函数
- `b.StopTimer()`：This can be used to pause the timer while performing complex initialization
- `b.ReportAllocs()`：,内存分配统计，等价于`-test.benchmem`

  在 `b.StopTimer()` 和 `b.StartTimer()` 之间可以做一些准备工作，这样这些时间不影响我们测试函数本身的性能。

```go
func BenchmarkGenShortId(b *testing.B) {
	for i := 0; i < b.N; i++ {
		GenShortId()
	}
}

func BenchmarkGenShortIdTimeConsuming(b *testing.B) {
	// 在 b.StopTimer() 和 b.StartTimer() 之间可以做一些准备工作，这样这些时间不影响我们测试函数本身的性能。
	b.StopTimer() // 调用该函数停止压力测试的时间计数

	shortID, err := GenShortId()
	if shortID == "" || err != nil {
		b.Error(err)
	}

	b.StartTimer() // 重新开始时间

	for i := 0; i < b.N; i++ {
		GenShortId()
	}
}

```

[High Performance Go Workshop](https://www.yuque.com/ksco/uiondt/napwx1)

## 测试覆盖率

由单元测试的代码，触发运行到的被测试代码的代码行数占所有代码行数的比例，被称为测试覆盖率，代码覆盖率不一定完全精准，但是可以作为参考，可以帮我们测量和我们预计的覆盖率之间的差距

`go test -coverprofile=cover.out`：在测试文件目录下运行测试并统计测试覆盖率

`go tool cover -func=cover.out`：分析覆盖率文件，可以看出哪些函数没有测试，哪些函数内部的分支没有测试完全，cover 工具会通过执行代码的行数与总行数的比例表示出覆盖率

[Go 语言实战笔记（二十一）| Go 单元测试](https://www.flysnow.org/2017/05/16/go-in-action-go-unit-test.html)
[Go 语言实战笔记（二十二）| Go 基准测试](https://www.flysnow.org/2017/05/21/go-in-action-go-benchmark-test.html)

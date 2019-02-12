# bufio

用来帮助处理 I/O 缓存。

`bufio`包，它使处理输入和输出方便又高效。`Scanner`类型是该包最有用的特性之一，它读取输入并将其拆成行或单词；通常是处理行形式的输入最简单的方法。

程序使用短变量声明创建`bufio.Scanner`类型的变量`input`。

```go
input := bufio.NewScanner(os.Stdin)
```

该变量从程序的标准输入中读取内容。每次调用`input.Scan()`，即读入下一行，并移除行末的换行符；读取的内容可以调用`input.Text()`得到。`Scan`函数在读到一行时返回`true`，不再有输入时返回`false`

## bufio.Writer

bufio.Writer 默认使用 4096 长度字节的缓存，可以使用 NewWriterSize 方法来设定该值

bufio.Writer 仅在缓存充满或者显式调用 Flush 方法时处理(发送)数据。

通过使用 Reset 方法，Writer 可以用于不同的目的对象。重复使用 Writer 缓存减少了内存的分配。而且减少了额外的垃圾回收工作

多次进行小量的写操作会影响程序性能。每一次写操作最终都会体现为系统层调用，频繁进行该操作将有可能对 CPU 造成伤害。而且很多硬件设备更适合处理块对齐的数据，例如硬盘。为了减少进行多次写操作所需的开支，golang 提供了 bufio.Writer。数据将不再直接写入目的地(实现了 io.Writer 接口)，而是先写入缓存，当缓存写满后再统一写入目的地。

## bufio.Scanner

## 参考

- [Go 语言 bufio 包介绍](https://studygolang.com/articles/11824)
- [深入理解 Go 标准库之 bufio.Scanner](https://studygolang.com/articles/11905)

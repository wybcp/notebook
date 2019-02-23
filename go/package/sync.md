# [sync](https://golang.org/pkg/sync/)

sync 包里提供了一种互斥型的锁，可以让我们自己灵活的控制哪些代码，同时只能有一个 goroutine 访问，被 sync 互斥锁控制的这段代码范围，被称之为临界区，临界区的代码，同一时间，只能又一个 goroutine 访问。

## [sync/atomic](https://golang.org/pkg/sync/atomic/)

atomic 可以解决资源竞争问题，但都是比较简单的，支持的数据类型有限。

## 参考

- [Golang 的 sync.WaitGroup 陷阱](http://lessisbetter.site/2018/10/29/Golang-trap-of-waitgroup/)如何确保 Add 函数一定在 Wait 函数前执行呢？在分配协程前就执行 Add 函数，然后再执行 Wait 函数，以此确保。
- [Go 语言实战笔记（十七）| Go 读写锁](https://www.flysnow.org/2017/05/03/go-in-action-go-read-write-lock.html)

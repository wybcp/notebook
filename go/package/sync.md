# sync

## 参考

-[Golang 的 sync.WaitGroup 陷阱](http://lessisbetter.site/2018/10/29/Golang-trap-of-waitgroup/)如何确保 Add 函数一定在 Wait 函数前执行呢？在分配协程前就执行 Add 函数，然后再执行 Wait 函数，以此确保。

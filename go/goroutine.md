# Go 程

Go 程（goroutine）是由 Go 运行时管理的轻量级线程。

`go f(x, y, z)`会启动一个新的 Go 程并执行`f(x, y, z)`

`f`, `x`, `y` 和 `z` 的求值发生在当前的 Go 程中，而 `f` 的执行发生在新的 Go 程中。

Go 程在相同的地址空间中运行，因此在访问共享的内存时必须进行同步。[`sync`](https://go-zh.org/pkg/sync/) 包提供了这种能力，不过在 Go 中并不经常用到，因为还有其它的办法。

为了保护子协程的安全，通常我们会在协程的入口函数开头增加 recover() 语句来恢复协程内部发生的异常，阻断它传播到主协程导致程序崩溃。recover 语句必须写在 defer 语句里面。

```go
go func() {
  defer func() {
    if err := recover(); err != nil {
      // log error
    }
  }()
  // do something
}()
```

## 设置线程数

默认情况下，Go 运行时会将线程数会被设置为机器 CPU 逻辑核心数。同时它内置的 runtime 包提供了 `GOMAXPROCS(n int)` 函数允许我们动态调整线程数，该函数会返回修改前的线程数，如果参数 n <=0 ，就不会产生修改效果，等价于读操作。

```go
package main

import "fmt"
import "runtime"

func main() {
    // 读取默认的线程数
    fmt.Println(runtime.GOMAXPROCS(0))
    // 设置线程数为 10
    runtime.GOMAXPROCS(10)
    // 读取当前的线程数
    fmt.Println(runtime.GOMAXPROCS(0))
}

--------
4
10
```

获取当前的协程数量可以使用 runtime 包提供的 `NumGoroutine()` 方法

```go
package main

import "fmt"
import "time"
import "runtime"

func main() {
    fmt.Println(runtime.NumGoroutine())
    for i:=0;i<10;i++ {
        go func(){
            for {
                time.Sleep(time.Second)
            }
        }()
    }
    fmt.Println(runtime.NumGoroutine())
}

------
1
11
```

## 信道

信道是带有类型的管道，你可以通过它用信道操作符 `<-` 来发送或者接收值。

```go
ch <- v    // 将 v 发送至信道 ch。
v := <-ch  // 从 ch 接收值并赋予 v。
```

（“箭头”就是数据流的方向。）

和映射与切片一样，信道在使用前必须创建：

```go
ch := make(chan int)
```

默认情况下，发送和接收操作在另一端准备好之前都会阻塞。这使得 Go 程可以在没有显式的锁或竞态变量的情况下进行同步。

以下示例对切片中的数进行求和，将任务分配给两个 Go 程。一旦两个 Go 程完成了它们的计算，它就能算出最终的结果。

### 带缓冲的信道

信道可以是 _带缓冲的_。将缓冲长度作为第二个参数提供给 `make` 来初始化一个带缓冲的信道：

```go
ch := make(chan int, 100)
```

仅当信道的缓冲区填满后，向其发送数据时才会阻塞。当缓冲区为空时，接受方会阻塞。

### range 和 close

发送者可通过 `close` 关闭一个信道来表示没有需要发送的值了。接收者可以通过为接收表达式分配第二个参数来测试信道是否被关闭：若没有值可以接收且信道已被关闭，那么在执行完

```go
v, ok := <-ch
```

之后 `ok` 会被设置为 `false`。

循环 `for i := range c` 会不断从信道接收值，直到它被关闭。

_注意：_ 只有发送者才能关闭信道，而接收者不能。向一个已经关闭的信道发送数据会引发程序恐慌（panic）。

_还要注意：_ 信道与文件不同，通常情况下无需关闭它们。只有在必须告诉接收者不再有值需要发送的时候才有必要关闭，例如终止一个 `range` 循环。

## 协程的应用

在日常互联网应用中，Go 语言的协程主要应用在 HTTP API 应用、消息推送系统、聊天系统等。

在 HTTP API 应用中，每一个 HTTP 请求，服务器都会单独开辟一个协程来处理。在这个请求处理过程中，要进行很多 IO 调用，比如访问数据库、访问缓存、调用外部系统等，协程会休眠，IO 处理完成后协程又会再次被调度运行。待请求的响应回复完毕后，链接断开，这个协程的寿命也就到此结束。

在消息推送系统中，客户端的链接寿命很长，大部分时间这个链接都是空闲状态，客户端会每隔几十秒周期性使用心跳来告知服务器你不要断开我。在服务器端，每一个来自客户端链接的维持都需要单独一个协程。因为消息推送系统维持的链接普遍很闲，单台服务器往往可以轻松撑起百万链接，这些维持链接的协程只有在推送消息或者心跳消息到来时才会变成就绪态被调度运行。

聊天系统也是长链接系统，它内部来往的消息要比消息推送系统频繁很多，限于 CPU 和 网卡的压力，它能撑住的连接数要比推送系统少很多。不过原理是类似的，都是一个链接由一个协程长期维持，连接断开协程也就消亡。

## select 功能

在多个通道上进行读或写操作，让函数可以处理多个事情，但 1 次只处理 1 个。以下特性也都必须熟记于心：

- 每次执行 select，都会只执行其中 1 个 case 或者执行 default 语句。
- 当没有 case 或者 default 可以执行时，select 则阻塞，等待直到有 1 个 case 可以执行。
- 当有多个 case 可以执行时，则随机选择 1 个 case 执行。
- case 后面跟的必须是读或者写通道的操作，否则编译出错。

[Golang 并发模型：轻松入门 select](http://lessisbetter.site/2018/12/13/golang-slect/)

[Golang 并发模型：select 进阶](http://lessisbetter.site/2018/12/17/golang-selete-advance/)

[Golang 并发模型：轻松入门协程池](http://lessisbetter.site/2018/12/20/golang-simple-goroutine-pool/)

## [使用 race 检测数据竞争](http://lessisbetter.site/2018/11/17/Golang-detecting-date-racing/)

[Golang 并发模型：并发协程的优雅退出](http://lessisbetter.site/2018/12/02/golang-exit-goroutine-in-3-ways/)

- 发送协程主动关闭通道，接收协程不关闭通道。技巧：把接收方的通道入参声明为只读，如果接收协程关闭只读协程，编译时就会报错。
- 协程处理 1 个通道，并且是读时，协程优先使用 for-range，因为 range 可以关闭通道的关闭自动退出协程。
- `,ok`可以处理多个读通道关闭，需要关闭当前使用 for-select 的协程。
  显式关闭通道 stopCh 可以处理主动通知协程退出的场景。

[Golang 并发：再也不愁选 channel 还是选锁](http://lessisbetter.site/2019/01/14/golang-channel-and-mutex/)

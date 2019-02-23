# 通道

    Don’t communicate by sharing memory; share memory by communicating. （不要通过共享内存来通信，而应该通过通信来共享内存。）

Go 语言的主要创造者之一的 Rob Pike 的至理名言，体现了 Go 语言最重要的编程理念。

通道类型的值本身就是并发安全的。

在初始化通道的时候，make 函数除了必须接收这样的类型字面量作为参数，还可以接收一个 int 类型的参数。

后者是可选的，用于表示该通道的容量。所谓通道的容量，就是指通道最多可以缓存多少个元素值，它是不能小于 0 的。

- 当容量为 0 时，为非缓冲通道，是不带缓冲的通道。
- 当容量大于 0 时，为缓冲通道，是带有缓冲的通道。

非缓冲通道和缓冲通道有着不同的数据传递方式。

一个通道相当于一个先进先出（FIFO）的队列。

若在关闭 Channel 后继续从中接收数据，接收者就会收到该 Channel 返回的零值。

```go
type hchan struct {
  qcount uint  // 通道有效元素个数
  dataqsize uint   // 通道容量，循环数组总长度
  buf unsafe.Pointer // 数组地址
  elemsize uint16 // 内部元素的大小
  closed uint32 // 是否已关闭 0或者1
  elemtype *_type // 内部元素类型信息
  sendx uint // 循环数组的写偏移量
  recvx uint // 循环数组的读偏移量
  recvq waitq // 阻塞在读操作上的协程队列
  sendq waitq // 阻塞在写操作上的协程队列

  lock mutex // 全局锁
}
```

channel 中的一个元素最大可高达 64 KiB

## [单向通道](https://time.geekbang.org/column/article/14664)

只能发不能收，或者只能收不能发的通道。

主要的用途就是约束其他代码的行为。

在调用函数的单通道参数时候，只需要把一个元素类型匹配的双向通道传给它，o 语言在这种情况下会自动地把双向通道转换为函数所需的单向通道。

## select

select 语句只能与通道联用，它一般由若干个分支组成。每次执行这种语句的时候，一般只有一个分支中的代码会被运行。

select 语句的分支分为两种，一种叫做候选分支，另一种叫做默认分支。候选分支总是以关键字 case 开头，后跟一个 case 表达式和一个冒号，然后我们可以从下一行开始写入当分支被选中时需要执行的语句。

默认分支其实就是 default case，因为，当且仅当没有候选分支被选中时它才会被执行，所以它以关键字 default 开头并直接后跟一个冒号。同样的，我们可以在 default:的下一行写入要执行的语句。

由于 select 语句是专为通道而设计的，所以每个 case 表达式中都只能包含操作通道的表达式，比如接收表达式。

## 关闭通道

确保通道写安全的最好方式是由负责写通道的协程自己来关闭通道，读通道的协程不要去关闭通道。多写单读的场合该怎么办呢？

使用到内置 sync 包提供的 WaitGroup 对象，它使用计数来等待指定事件完成。

```go
package main

import "fmt"
import "time"
import "sync"

func send(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done() // 计数值减一
	i := 0
	for i < 4 {
		i++
		ch <- i
	}
}

func recv(ch chan int) {
	for v := range ch {
		fmt.Println(v)
	}
}

func main() {
	var ch = make(chan int, 4)
	var wg = new(sync.WaitGroup)
	wg.Add(2)       // 增加计数值
	go send(ch, wg) // 写
	go send(ch, wg) // 写
	go recv(ch)
	// Wait() 阻塞等待所有的写通道协程结束
	// 待计数值变成零，Wait() 才会返回
	wg.Wait()
	// 关闭通道
	close(ch)
	time.Sleep(time.Second)
}

---------
1
2
3
4
1
2
3
4
```

读取一个已经关闭的通道会立即返回通道类型的「零值」（通道数据已读取完毕之后），而写一个已经关闭的通道会抛异常。如果通道里的元素是整型的，读操作是不能通过返回值来确定通道是否关闭的。

在已关闭的通道上的读取行为比较特殊：

- 如果还有元素没有被取出，那么读取操作会照常进行。
- 如果队列已空并且已被关闭，读取不会阻塞。
- 在为空并且已经关闭的通道上读取时会返回通道中元素类型的 “零值”。

```go
item, valid := <- queue
// 在这里, "valid" 取值:
// true => "item" 有效
// false => "queue" 已经关闭, "item" 只是一个 “零值”
```

使用

```go
for {
    item, valid := <- queue
    if !valid {
        break
    }
    // 处理 item
}
// 到这里，所有被放入到 queue 中的元素都已经处理完毕，
// 并且 queue 也已经关闭
```

## 应用场景

用在数据流动的地方：

- 消息传递、消息过滤
- 信号广播
- 事件订阅与广播
- 请求、响应转发
- 任务分发 [Go语言实战笔记（十五）| Go 并发示例-Runner](https://www.flysnow.org/2017/04/29/go-in-action-go-runner.html)
- 结果汇总
- 并发控制
- 同步与异步

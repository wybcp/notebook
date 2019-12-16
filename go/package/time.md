# time

```go
func example() {
	p := fmt.Println
	// 从获取当前时间开始
	now := time.Now()
	// 时间戳
	secs := now.Unix()
	nanos := now.UnixNano()
	p(now)
	// 你可以提供年，月，日等来创建一个时间。当然时间
	// 总是会和地区联系在一起，也就是时区
	then := time.Date(2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)
	// 你可以获取时间的各个组成部分
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())
	// 输出当天是周几，Monday-Sunday中的一个 p(then.Weekday())
	// 下面的几个方法判断两个时间的顺序，精确到秒 p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))
	// Sub方法返回两个时间的间隔(Duration)
	diff := now.Sub(then)
	p(diff)
	// 可以以不同的单位来计算间隔的大小
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())
	// 你可以使用Add方法来为时间增加一个间隔 // 使用负号表示时间向前推移一个时间间隔 p(then.Add(diff))
	p(then.Add(-diff))
}
```

## Go 超时

超时对那些连接外部资源的程序来说是很重要的，否则就需要限定执行时间。在 Go 里面实现超时很简单。 我们可以使用 channel 和 select 很容易地做到。

```go
package main

import "time"
import "fmt"

func main() {
	// 在这个例子中，假设我们执行了一个外部调用，2秒之后将结果写入c1
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(time.Second * 2)
		c1 <- "result 1"
	}()
	// 这里使用select来实现超时，`res := <-c1`等待通道结果，
	// `<- Time.After`则在等待1秒后返回一个值，因为select首先
	// 执行那些不再阻塞的case，所以这里会执行超时程序，如果
	// `res := <-c1`超过1秒没有执行的话
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(time.Second * 1):
		fmt.Println("timeout 1")
	}

	// 如果我们将超时时间设为3秒，这个时候`res := <-c2`将在
	// 超时case之前执行，从而能够输出写入通道c2的值
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(time.Second * 3):
		fmt.Println("timeout 2")
	}
}
```

## Go 打点器

### Timer

Timer 是让你等待一段时间然后去做一件事情，这件事情只会做一次。

### Ticker

Ticker 是让你按照一定的时间间隔循环往复地做一件事情，除非你手动停止它。

```go
func ticker() {
	// Ticker使用和Timer相似的机制，同样是使用一个通道来发送数据。
	// 这里我们使用range函数来遍历通道数据，这些数据每隔500毫秒被
	// 发送一次，这样我们就可以接收到
	ticker := time.NewTicker(time.Millisecond * 500)
	go func() {
		for t := range ticker.C {
			fmt.Println("Tick at ", t)
		}
	}()
	// Ticker和Timer一样可以被停止。一旦Ticker停止后，通道将不再
	// 接收数据，这里我们将在1500毫秒之后停止
	time.Sleep(time.Millisecond * 1500)
	ticker.Stop()
	fmt.Println("Ticker stopped")
}
```

## [timezone 时区](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

```go
func change(){
	//按照时区解析时间时间
time.ParseInLocation(layout, value string, loc *Location)
// 将当前时间转化为目标timezone的时间
time.Now().In(timezone)
// time.local 系统时区
}
```

输出 golang 支持的 timezone

```go
package main

import (
    "fmt"
    "io/ioutil"
    "strings"
)

var zoneDirs = []string{
    // Update path according to your OS
    "/usr/share/zoneinfo/",
    "/usr/share/lib/zoneinfo/",
    "/usr/lib/locale/TZ/",
}

var zoneDir string

func main() {
    for _, zoneDir = range zoneDirs {
        ReadFile("")
    }
}

func ReadFile(path string) {
    files, _ := ioutil.ReadDir(zoneDir + path)
    for _, f := range files {
        if f.Name() != strings.ToUpper(f.Name()[:1]) + f.Name()[1:] {
            continue
        }
        if f.IsDir() {
            ReadFile(path + "/" + f.Name())
        } else {
            fmt.Println((path + "/" + f.Name())[1:])
        }
    }
}
```

## [monday](https://github.com/goodsign/monday)

Monday is a minimalistic l10n, i18n package for translation of month and day of week names in time.Date objects.

解析不同国家的月份和星期。

```golang
  time.ParseInLocation(yourLayout, yourString, yourLocation)
  time.Parse(yourLayout, yourString)
  // Change LocaleEnUS to the locale you want to use for translation
  monday.ParseInLocation(yourLayout, yourString, yourLocation, monday.LocaleEnUS)
  monday.Parse(yourLayout, yourString, monday.LocaleEnUS)
```

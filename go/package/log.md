# log

## 定制

日志包 log 提供了可定制化的配制，可以自己定制日志的抬头信息。

### 定制抬头信息

```go
func init() {
	log.SetFlags(log.LstdFlags | log.Llongfile)
}
// 可选项
// Ldate         = 1 << iota     // the date in the local time zone: 2009/01/23
// Ltime                         // the time in the local time zone: 01:23:23
// Lmicroseconds                 // microsecond resolution: 01:23:23.123123.  assumes Ltime.
// Llongfile                     // full file name and line number: /a/b/c/d.go:23
// Lshortfile                    // final file name element and line number: d.go:23. overrides Llongfile
// LUTC                          // if Ldate or Ltime is set, use UTC rather than the local time zone
// LstdFlags     = Ldate | Ltime // initial values for the standard logger
```

### 定制前缀

`log.SetPrefix("【test】")`

## Println

```go
func Println(v ...interface{}) {
	std.Output(2, fmt.Sprintln(v...))
}
```

## Fatal

Fatal 相当于先调用 Print 打印日志，然后再调用 os.Exit(1)退出程序。

```go
func Fatalln(v ...interface{}) {
	std.Output(2, fmt.Sprintln(v...))
	os.Exit(1)
}
```

## Panic

表示先使用 Print 记录日志，然后调用 panic()函数抛出一个 panic，这时候除非使用 recover()函数，否则程序就会打印错误堆栈信息，然后程序终止。

```go
func Panicln(v ...interface{}) {
	s := fmt.Sprintln(v...)
	std.Output(2, s)
	panic(s)
}
```

[Go 语言实战笔记（18）](https://www.flysnow.org/2017/05/06/go-in-action-go-log.html)

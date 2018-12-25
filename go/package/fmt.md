# `fmt`

含有格式化输出、接收输入的函数。

- `Println`是其中一个基础函数，可以打印以空格间隔的一个或多个值，并在最后添加一个换行符，从而输出一整行。（ln`指`line）

- `fmt.Printf`函数对一些表达式产生格式化输出。该函数的首个参数是个格式字符串，指定后续参数被如何格式化。各个参数的格式取决于“转换字符”（conversion character），形式为百分号后跟一个字母（f`指`format）

通用的格式 %v（对应 “值”）

当打印结构体时，改进的格式 `%+v` 会为结构体的每个字段添上字段名，而另一种格式 `%#v` 将完全按照 Go 的语法打印值。

```go
type T struct {
    a int
    b float64
    c string
}
t := &T{ 7, -2.35, "abc\tdef" }
fmt.Printf("%v\n", t)
fmt.Printf("%+v\n", t)
fmt.Printf("%#v\n", t)
fmt.Printf("%#v\n", timeZone)
// &{7 -2.35 abc   def}
// &{a:7 b:-2.35 c:abc     def}
// &main.T{a:7, b:-2.35, c:"abc\tdef"}
// map[string] int{"CST":-21600, "PST":-28800, "EST":-18000, "UTC":0, "MST":-25200}
```

`%T`，它会打印某个值的类型.

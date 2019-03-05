# [reflect](https://golang.org/pkg/reflect/)

在 Go 的反射定义中，任何接口都会由两部分组成的，一个是接口的具体类型，一个是具体类型对应的值。

- [Goalng 下的反射模块 reflect 学习使用](https://www.jianshu.com/p/42c19f88df6c)
- [Go 语言实战笔记（二十四）| Go 反射](https://www.flysnow.org/2017/06/13/go-in-action-go-reflect.html)

## x.(T)这样的语法

这样的语法只适应于 x 是 interface 类型

函数

```go
func main() {
    v:="aaaaaa"
    // s,ok:=v.(string)
    // fmt.Printf("%s:%b\n",s,ok)
    // 不行

    check(v)
}
func checkit(v interface{}){
    s,ok:=v.(string)
    fmt.Printf("%s:%b\n",s,ok)
}
```

相当于把参数转换成了 interface 类型了

通过反射处理

```go
func main(){
    str := "aaaaaa"
	var t = reflect.TypeOf(str)

	switch t.Kind() {
	case reflect.String:
		fmt.Println("str is string")
	case reflect.Float64:
		fmt.Println("str is float64")
	}

}
```

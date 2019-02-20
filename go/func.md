# 函数

`_` ，空白标识符，特殊在于实际上返回值并没有赋值。

如果参数有相同的类型，函数声明用这样一个简洁的用法：

```go
func add(a, b int) int {

}
```

每一次函数调用都必须按照声明顺序为所有参数提供实参（参数值）。在函数调用时，Go 语言没有默认参数值

没有函数体的函数声明，这表示该函数不是以 Go 实现的。

如果一个函数将所有的返回值都显示的变量名，那么该函数的 return 语句可以省略操作数。这称之为 bare return。当一个函数有多处 return 语句以及许多返回值时，bare return 可以减少代码的重复，但是使得代码难以被理解。不宜过度使用 bare return。

## 闭包

闭包对捕获的外部变量并不是传值方式访问，而是以引用的方式访问。

闭包的这种引用方式访问外部变量的行为可能会导致一些隐含的问题：

```go
func main() {
    for i := 0; i < 3; i++ {
        defer func(){ println(i) } ()
    }
}
// Output:
// 3
// 3
// 3
```

因为是闭包，在 for 迭代语句中，每个 defer 语句延迟执行的函数引用的都是同一个 i 迭代变量，在循环结束后这个变量的值为 3，因此最终输出的都是 3。
修复的思路是在每轮迭代中为每个 defer 函数生成独有的变量。可以用下面两种方式：

```go
func main() {
    for i := 0; i < 3; i++ {
        i := i // 定义一个循环体内局部变量i
        defer func(){ println(i) } ()
    }
}

func main() {
    for i := 0; i < 3; i++ {
        // 通过函数传入i
        // defer 语句会马上对调用参数求值
        defer func(i int){ println(i) } (i)
    }
}
```

一般来说,在 for 循环内部执行 defer 语句并不是一个好的习惯，不建议使用。

Go 语言中，如果以切片为参数调用函数时，有时候会给人一种参数采用了传引用的方式的假象：因为在被调用函数内部可以修改传入的切片的元素。其实，任何可以通过函数参数修改调用参数的情形，都是因为函数参数中显式或隐式传入了指针参数。函数参数传值的规范更准确说是只针对数据结构中固定的部分传值，例如字符串或切片对应结构体中的指针和字符串长度结构体传值，但是并不包含指针间接指向的内容。

### 使用闭包调试

当您在分析和调试复杂的程序时，无数个函数在不同的代码文件中相互调用，如果这时候能够准确地知道哪个文件中的具体哪个函数正在执行，对于调试是十分有帮助的。您可以使用 runtime 或 log 包中的特殊函数来实现这样的功能。包 runtime 中的函数 Caller() 提供了相应的信息，因此可以在需要的时候实现一个 where() 闭包函数来打印函数执行的位置：

```go
where := func() {
    _, file, line, _ := runtime.Caller(1)
    log.Printf("%s:%d", file, line)
}
where()
// some code
where()
// some more code
where()
```

您也可以设置 log 包中的 flag 参数来实现：

```go
func where(){
    log.SetFlags(log.Llongfile)
    log.Print("")
}
```

## [方法](https://chai2010.gitbooks.io/advanced-go-programming-book/content/ch1-basic/ch1-04-func-method-interface.html)

方法是由函数演变而来，只是将函数的第一个对象参数移动到了函数名前面。通过叫方法表达式的特性可以将方法还原为普通类型的函数：

```go
// 不依赖具体的文件对象
// func CloseFile(f *File) error
var CloseFile = (*File).Close
```

## 计算函数执行时间

使用 time 包中的 Now() 和 Sub 函数：

```go
start := time.Now()
longCalculation()
end := time.Now()
delta := end.Sub(start)
fmt.Printf("longCalculation took this amount of time: %s\n", delta)
```

## [可变参数函数](https://studygolang.com/articles/11965)

## method

一个方法只是一个函数，它有一个特殊的接收者（receiver）类型，该接收者放在 func 关键字和函数名之间。接收者可以是结构体类型或非结构体类型。可以在方法内部访问接收者。
一般语法为：

```go
func (t receiver_type) methodName(parameter list) {}
```

- 参数 receiver 类型可以是 T 或 `*T`。以指针为接收者也是可以的。

    两者的区别在于， 以`*T` 为接收者时，方法内部对其的修改对于外部有效，而以 T 作为接受者时，对于外部无效。
- Go 不允许同名函数，但是同名方法可以定义在不同的类型上

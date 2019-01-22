# os

`os`包以跨平台的方式，提供了一些与操作系统交互的函数和变量。

## 命令行参数

程序的命令行参数可从 os 包的 Args 变量获取；os 包外部使用 os.Args 访问该变量。

os.Args 变量是一个字符串（string）的*切片*（slice）。现在先把切片 s 当作数组元素序列, 序列的长度动态变化, 用`s[i]`访问单个元素，用`s[m:n]`获取子序列(译注：和 python 里的语法差不多)。序列的元素数目为 len(s)。和大多数编程语言类似，区间索引时，Go 言里也采用左闭右开形式, 即，区间包括第一个索引元素，不包括最后一个, 因为这样可以简化逻辑。（译注：比如 a = [1, 2, 3, 4, 5], a[0:3] = [1, 2, 3]，不包含最后一个元素）。比如 s[m:n]这个切片，0 ≤ m ≤ n ≤ len(s)，包含 n-m 个元素。

os.Args 的第一个元素，os.Args[0], 是命令本身的名字；其它的元素则是程序启动时传给它的参数。

使用 `os.Exit()` 可以给定一个状态，然后立刻退出程序运行。

## 环境变量

环境变量是一种很普遍的将配置信息传递给 Unix 程序的机制。

```go
func env() {
	// 为了设置一个key/value对，使用`os.Setenv`
	// 为了获取一个key的value，使用`os.Getenv`
	// 如果所提供的key在环境变量中没有对应的value，
	// 那么返回空字符串
	os.Setenv("foo", "1")
	fmt.Println("foo:", os.Getenv("foo"))
    fmt.Println("foo 1:", os.Getenv("foo1"))
    for i, e := range os.Environ() {
		pair := strings.Split(e, "=")
		fmt.Println(e)
		fmt.Println(pair)
		fmt.Println(i)
	}
}
```

## 进程触发

从 Go 程序里面触发一个其他的非 Go 进程来执行。

```go
func execExample() {
	// `exec.Command` 函数创建了一个代表外部进程的对象
	dateCmd := exec.Command("date")
	// `Output`是另一个运行命令时用来处理信息的函数，这个
	// 函数等待命令结束，然后收集命令输出。
	dateOut, err := dateCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println(string(dateOut))
	// stdin输入数据的命令，
	// 数据输入传给外部进程的stdin，然后从它输出到stdout
	// 的运行结果收集信息
	grepCmd := exec.Command("grep", "hello")
	// 显式地获取input/output管道，启动进程，
	// 向进程写入数据，然后读取输出结果，最后等待进程结束
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := ioutil.ReadAll(grepOut)
	grepCmd.Wait()
	fmt.Println(string(grepBytes))
}

```

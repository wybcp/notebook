# 面试题

## 设置 GOPATH 有什么意义？

环境变量 GOPATH 的值可以是一个目录的路径，也可以包含多个目录路径，每个目录都代表 Go 语言的一个工作区（workspace）。这些工作区用于放置 Go 语言的源码文件（source file），以及安装（install）后的归档文件（archive file，也就是以“.a”为扩展名的文件）和可执行文件（executable file）。

## Go 语言的类型推断可以带来哪些好处？

Go 语言的类型推断可以明显提升程序的灵活性，使得代码重构变得更加容易，同时又不会给代码的维护带来额外负担，更不会损失程序的运行效率（编译期间完成类型确认），更不会损失程序的运行效率。

## [使用 new()和 make()](https://go.fdos.me/16.4.html)

- 切片、映射和通道，使用 make，返回的类型就是这三个类型本身，而不是他们的指针类型，因为这三种类型就是引用类型
- 数组、结构体和所有的值类型，使用 new ，返回的是类型的指针，指向分配类型的内存地址。

二者都是内存的分配（堆上），但是 make 只用于 slice、map 以及 channel 的初始化（非零值）；而 new 用于类型的内存分配，并且内存置为零。

## [Awesome Go Interview Questions and Answers](https://goquiz.github.io/)

## [Go 语言参数传递是传值还是传引用](https://www.flysnow.org/2018/02/24/golang-function-parameters-passed-by-value.html)

Go 语言中所有的传参都是值传递（传值），都是一个副本，一个拷贝。因为拷贝的内容有时候是非引用类型（int、string、struct 等这些），这样就在函数中就无法修改原内容数据；有的是引用类型（指针、map、slice、chan 等这些），这样就可以修改原内容数据。

## [1、2、3 三个线程，让他们依次打印自己的编号](https://zhuanlan.zhihu.com/p/57969652?utm_source=wechat_session&utm_medium=social&utm_oi=29305031622656)

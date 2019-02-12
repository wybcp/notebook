# 面试题

## 设置 GOPATH 有什么意义？

环境变量 GOPATH 的值可以是一个目录的路径，也可以包含多个目录路径，每个目录都代表 Go 语言的一个工作区（workspace）。这些工作区用于放置 Go 语言的源码文件（source file），以及安装（install）后的归档文件（archive file，也就是以“.a”为扩展名的文件）和可执行文件（executable file）。

## Go 语言的类型推断可以带来哪些好处？

Go 语言的类型推断可以明显提升程序的灵活性，使得代码重构变得更加容易，同时又不会给代码的维护带来额外负担，更不会损失程序的运行效率（编译期间完成类型确认），更不会损失程序的运行效率。

## [使用 new()和 make()](https://go.fdos.me/16.4.html)

- 切片、映射和通道，使用 make
- 数组、结构体和所有的值类型，使用 new

## [Awesome Go Interview Questions and Answers](https://goquiz.github.io/)
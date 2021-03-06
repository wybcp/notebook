# defer

尽管 Go 有一个垃圾回收器，一些资源仍然需要我们显示地释放他们。Go 给出的解决方案是使用 `defer` 关键字。

无论什么情况，在函数返回之后，`defer` 将被执行。这使您可以在初始化的位置附近释放资源并处理多个返回点。

推迟的函数调用会被压入一个栈中。当外层函数返回时，被推迟的函数会按照后进先出的顺序调用。

## 参考

- [Golang defer 的陷阱](http://lessisbetter.site/2018/11/10/Golang-trap-of-defer/)

  defer 及 defer 函数的执行顺序分 2 步：

  1. 执行 defer，计算函数的入参的值，并传递给函数，但不执行函数，而是将函数压入栈。
  2. 函数 return 语句后，或 panic 后，执行压入栈的函数，函数中变量的值，此时会被计算。

# 斐波纳契数列

计算斐波纳契数列（Fibonacci）的第 N 个数：

```Go
func fib(n int) int {
    x, y := 0, 1
    for i := 0; i < n; i++ {
        x, y = y, x+y
    }
    return x
}
```

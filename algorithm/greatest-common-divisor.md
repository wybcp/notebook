# 最大公约数

计算两个整数值的的最大公约数（GCD）（译注：GCD 不是那个敏感字，而是 greatest common divisor 的缩写，欧几里德的 GCD 是最早的非平凡算法）：

```Go
func gcd(x, y int) int {
    for y != 0 {
        x, y = y, x%y
    }
    return x
}
```

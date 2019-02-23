# [辗转相除法](https://zh.wikipedia.org/wiki/%E8%BC%BE%E8%BD%89%E7%9B%B8%E9%99%A4%E6%B3%95)

辗转相除法，又称欧几里得算法（英语：Euclidean algorithm），是求最大公约数的算法。

```golang
package main

import "fmt"

func main() {
	fmt.Println(gcdx(867,1122))
	fmt.Println(gcd(867,1122))
}

/*
*辗转相除法：最大公约数
*递归写法，进入运算是x和y都不为0
 */
func gcd(x, y int) int {
	tmp := x % y
	if tmp > 0 {
		return gcd(y, tmp)
	} else {
		return y
	}
}

/*
*辗转相除法：最大公约数
*非递归写法
 */
func gcdx(x, y int) int {
	for {
		tmp := x % y
		if tmp > 0 {
			x = y
			y = tmp
		} else {
			return y
		}
	}
}
```

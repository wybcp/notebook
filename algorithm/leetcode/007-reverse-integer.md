# [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

整数反转

```go

func reverse(x int) int {
	reversed := 0
	for {
		r := x % 10
		reversed += r

		x /= 10
		if x == 0 {
			break
		}
		reversed *= 10
	}

	if reversed > int(math.Exp2(31.0)) || reversed < int(-math.Exp2(31.0)) {
		return 0
	}

	return reversed
}
```

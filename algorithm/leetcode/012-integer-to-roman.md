# [integer-to-roman](https://leetcode-cn.com/problems/integer-to-roman)

整数转罗马数字

```go
func intToRoman(num int) string {
	var roman string
	var count int
	if num < 1 || num > 3999 {
		return roman
	}
	romans := [][]string{
		{"I", "V", "X"},
		{"X", "L", "C"},
		{"C", "D", "M"},
		{"M", "M", "M"},
	}

	for num > 0 {
		mod := num % 10
		num /= 10

		roman = helper(mod, romans[count]) + roman
		count++
	}

	return roman
}
func helper(x int, units []string) (roman string) {
	for x > 0 {
		switch {
		case x == 9:
			roman += units[0] + units[2]
			x -= 9
		case x >= 5:
			roman += units[1]
			x -= 5
		case x == 4:
			roman += units[0] + units[1]
			x -= 4
		default:
			roman += units[0]
			x--
		}
	}
	return roman
}
```

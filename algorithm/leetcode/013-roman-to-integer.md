# [roman-to-integer](https://leetcode-cn.com/problems/roman-to-integer)

罗马数字转整数

```go
func romanToInt(s string) int {
	var num int
	if len(s) == 0 {
		return num
	}
	romans := map[string]int{"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

	for i := 0; i < len(s);{
		if i < len(s)-1 && romans[s[i:i+1]] < romans[s[i+1:i+2]] {
			num = num + romans[s[i+1:i+2]] - romans[s[i:i+1]]
			i = i + 2
		} else {
			num += romans[s[i:i+1]]
			i++
		}
	}
	return num
}
```

字符串转化为字节处理，更快

```go
func romanToInt(s string) int {
    var num int
	if len(s) == 0 {
		return num
	}
	romans := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	sByte:=[]byte(s)
	for i := 0; i < len(sByte); {
		if i < len(sByte)-1 && romans[sByte[i]] < romans[sByte[i+1]] {
			num += romans[sByte[i+1]] - romans[sByte[i]]
			i += 2
		} else {
			num += romans[sByte[i]]
			i++
		}
	}
	return num
}
```

# [letter-combinations-of-a-phone-number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

```go
func letterCombinations(digits string) []string {
	res := make([]string, 0)
	digitWordsMap := map[string]string{
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz",
	}
	for _, digit := range digits {
		words := digitWordsMap[string(digit)]
		tmp := make([]string, 0)

		for _, word := range words {
			if len(res) > 0 {
				//生成新的slice
				for _, item := range res {
					tmp = append(tmp, item+string(word))
				}
			} else {
				//第一个字母
				tmp = append(tmp, string(word))
			}
		}
		//赋值
		res = tmp
	}
	return res
}
```

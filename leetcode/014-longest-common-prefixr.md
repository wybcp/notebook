# [longest-common-prefix](https://leetcode.com/problems/longest-common-prefix)

最长公共前缀

```go
func longestCommonPrefix(strs []string) string {
	var prefix string
	if len(strs) == 0 {
		return prefix
	}

	prefix = strs[0]
	for i := 1; i < len(strs); i++ {
		if len(prefix)==0 {
			break
		}
		for strings.HasPrefix(strs[i], prefix) == false {
			prefix = string([]rune(prefix)[:len(prefix)-1])
		}
	}

	return prefix
}
```

# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

当重复字符出现的时候，更新新的子字符串开始索引，保存每次的子字符串的最大长度

```go
func lengthOfLongestSubstring(s string) int {
	lastOccurred := make(map[rune]int) //记录字符最后出现的位置
	// 最大子字符串开始的索引
	maxStart := 0
	// 比较的子字符串的开始的索引
	start := 0
	//  最大子字符串的长度
	maxLength := 0

	for i, ch := range []rune(s) {
		//字符非第一次出现，开始新的子字符串
		if lastI, ok := lastOccurred[ch]; ok && lastI >= start {
			start = lastI + 1
		}
		// 子字符串的长度对比
		if i-start+1 > maxLength {
			maxStart = start
			maxLength = i - start + 1
		}
		// 记录最新的索引
		lastOccurred[ch] = i
	}
	fmt.Println(s[maxStart:maxStart+maxLength])

	// fmt.Printf("Longest Substring Without Repeating Characters:%d", maxLength)
	return maxLength
}

```

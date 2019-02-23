# [3sum-closest](https://leetcode-cn.com/problems/3sum-closest)

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

```go
func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	length := len(nums)
	bestTarget := nums[0] + nums[1] + nums[2] // initial value
	if length == 3 {
		return bestTarget
	}
	for i := 0; i < length-2; i++ {
		newTarget := target - nums[i]
		left, right := i+1, length-1
		for left < right{
			if abs(bestTarget-target) > abs(nums[left]+nums[right]+nums[i]-target) {
				bestTarget = nums[left]+nums[right] + nums[i]
			}
			if bestTarget == target {
				return target
			}
			if nums[left]+nums[right] < newTarget {
				left++
			} else {
				right--
			}
		}
	}
	return bestTarget
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}
```

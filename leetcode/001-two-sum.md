# [Two Sum](https://leetcode.com/problems/two-sum/description/)

## python

Runtime:980ms

```python
def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for k, v in enumerate(nums):
        if target - v in nums[k + 1:]:
            return [k, nums[k + 1:].index(target - v) + k + 1]
```

Runtime:36ms

```python
def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for k, v in enumerate(nums):
        if v in buff_dict:
            return [buff_dict[v], k]
        else:
            buff_dict[target - v] = k
```

## go

Runtime:4ms

```golang
func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for i, v := range nums {
        if j, ok := m[target - v]; ok {
            return []int{j, i}
        } else {
            m[v] = i
        }
    }
    return []int{-1, -1}
}
```

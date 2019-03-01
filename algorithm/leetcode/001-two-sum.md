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

## [go](https://www.flysnow.org/2018/10/14/golang-leetcode-two-sum.html)

从这测试和性能分析来看，不存在最优的算法，只存在最合适的。

如果你的数组元素比较少，那么暴力算法是更适合你的。 如果数组元素非常多，那么采用哈希算法就是一个比较好的选择了。

所以，根据我们自己系统的实际情况，来选择合适的算法，比如动态判断数组的大小，采用不同的算法，达到最大的性能。

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

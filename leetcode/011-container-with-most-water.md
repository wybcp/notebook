# [container-with-most-water](https://leetcode.com/problems/container-with-most-water/)

盛最多水的容器

双指针法

这种方法背后的思路在于，两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。

我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。 此外，我们会使用变量 maxareamaxarea 来持续存储到目前为止所获得的最大面积。 在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxareamaxarea，并将指向较短线段的指针向较长线段那端移动一步。

```go
func maxArea(height []int) int {
	l := 0
	lMax := 0
	r := len(height) - 1
	rMax := len(height) - 1
	mArea := (len(height) - 1) * min(height[l], height[r])

	for i := 0; i < len(height); i++ {
		if l < r {
			if height[l] < height[r] {
				l = l + 1
			} else {
				r = r - 1
			}
			if mArea < (r-l)*min(height[l], height[r]) {
				mArea = (r - l) * min(height[l], height[r])
				lMax = l
				rMax = r
			}
		} else {
			fmt.Println("进行次数：", i)
			break
		}
	}
	fmt.Println("左边的序号：", lMax, "；左边的值：", height[lMax])
	fmt.Println("右边的序号：", rMax, "；右边的值：", height[rMax])
	fmt.Println("最大面积：",mArea)

	return mArea
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
```

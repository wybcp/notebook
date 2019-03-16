# [动态规划 Dynamic Programming](https://time.geekbang.org/column/article/72414)

动态规划比较适合用来求解最优问题，比如求最大值、最小值等等。它可以非常显著地降低时间复杂度，提高代码的执行效率。

## 使用动态规划的标准

动态规划适合解决的问题的模型

一般是用动态规划来解决最优问题。而解决问题的过程，需要经历多个决策阶段。每个决策阶段都对应着一组状态。然后寻找一组决策序列，经过这组决策序列，能够产生最终期望求解的最优值。

三个特征：

1. 最优子结构

    问题的最优解包含子问题的最优解。即可以通过子问题的最优解，推导出问题的最优解。

2. 无后效性

   无后效性有两层含义，第一层含义是，在推导后面阶段的状态的时候，只关心前面阶段的状态值，不关心这个状态是怎么一步一步推导出来的。第二层含义是，某阶段状态一旦确定，就不受之后阶段的决策影响。无后效性是一个非常“宽松”的要求。只要满足前面提到的动态规划问题模型，其实基本上都会满足无后效性。

3. 重复子问题

   不同的决策序列，到达某个相同的阶段时，可能会产生重复的状态。

## 背包问题

```go
package main

import (
	"fmt"
)

func main() {
	a := []int{2, 2, 4, 6, 3}
	knapsack(a, 5, 15)
}

// 2，2，4，6，3   9
// weight: 物品重量，n:5 物品个数，w: 9 背包可承载重量
// 有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，并且不可分割。
// 现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
func knapsack(weight []int, n int, w int) int {
	states := make([][]bool, n)
	for i := range states {
		states[i] = make([]bool, w+1)
	}
	// fmt.Println(states)
	// 第一行的数据要特殊处理，可以利用哨兵优化
	states[0][0] = true
	states[0][weight[0]] = true

	for i := 1; i < n; i++ {
		for j := 0; j <= w; j++ {
			// 不添加物品，只更新下一层状态
			if states[i-1][j] {
				states[i][j] = states[i-1][j]
			}
		}
		// 把第 i 个物品放入背包
		for j := 0; j <= w-weight[i]; j++ {
			if states[i-1][j] {
				states[i][j+weight[i]] = true
			}
		}

	}
	for i := w; i >= 0; i-- { // 输出结果
		if states[n-1][i]{
			fmt.Println(i)
			return i
		}
	}
	return -1
}
```

增加价值参量

```go
//weight 2，2，4，6，3
//value 10, 3, 1, 6, 2
// weight: 物品重量，value:物品的价值，n:5 物品个数，w: 9 背包可承载重量
// 有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，并且不可分割。
// 现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总价值最大？
func knapsack3(weight []int, value []int, n int, w int) int {
	states := make([][]int, n)
	for i := range states {
		states[i] = make([]int, w+1)
	}
	// 第一行的数据要特殊处理，可以利用哨兵优化
	states[0][0] = 0
	states[0][weight[0]] = value[0]
	for i := 1; i < n; i++ {
		for j := 0; j <= w; j++ {
			// 不添加物品，只更新下一层状态
			if states[i-1][j] > 0 {
				states[i][j] = states[i-1][j]
			}
		}
		// 把第 i 个物品放入背包
		for j := 0; j <= w-weight[i]; j++ {
			if states[i-1][j] > 0 && states[i][j+weight[i]] < value[i]+states[i-1][j] {
				states[i][j+weight[i]] = value[i] + states[i-1][j]
			}
		}
	}
	maxValue := 0
	for i := w; i >= 0; i-- { // 输出结果
		if states[n-1][i] > maxValue {
			maxValue = states[n-1][i]
		}
	}
	return maxValue
}
```

# 排序

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println(strs)

	ints := []int{7, 89, 1, 5, 56}
	sort.Ints(ints)
	fmt.Println(ints)

	// 我们还可以检测切片是否已经排序好
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}
```

# 切片

切片是轻量的包含并表示数组的一部分的结构。

有四种方式初始化一个切片：

```go
names := []string{"leto", "jessica", "paul"}//当你事先知道数组中的值的时候
checks := make([]bool, 10)//写入切片具体的索引
var names []string//指向空的切片，用于当元素数量未知时与 append 连接。
scores := make([]int, 0, 20)//让我们声明一个初始的容量。如果我们大概知道元素的数量将是很有用的。
```

Go 不支持负数索引。如果我们想要切片中除了最后一个元素的所有值，可以这样写：

```go
scores := []int{1, 2, 3, 4, 5}
scores = scores[:len(scores)-1]
```

切片通过两个下标来界定，即一个上界和一个下界，二者以冒号分隔：

```go
a[low : high]
```

它会选择一个半开区间，包括第一个元素，但排除最后一个元素。

切片的零值是 `nil`。

nil 切片的长度和容量为 0 且没有底层数组。

一个slice由三个部分构成：指针、长度和容量。

- 指针指向第一个slice元素对应的底层数组元素的地址，要注意的是slice的第一个元素并不一定就是数组的第一个元素。
- 长度对应slice中元素的数目；长度不能超过容量。

## 切片的长度与容量

切片拥有 **长度** 和 **容量**。

切片的长度就是它所包含的元素个数。

切片的容量是从它的第一个元素开始数，到其底层数组元素末尾的个数。

切片 `s` 的长度和容量可通过表达式 `len(s)` 和 `cap(s)` 来获取。

2x 算法来增加数组长度。

```go
s := []int{2, 3, 5, 7, 11, 13}
printSlice(s)
//len=6 cap=6 [2 3 5 7 11 13]
func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
```

## 向切片追加元素

为切片追加新的元素是种常用的操作，为此 Go 提供了内建的 `append` 函数。内建函数的[文档](https://go-zh.org/pkg/builtin/#append)对此函数有详细的介绍。

```go
func append(s []T, vs ...T) []T
```

`append` 的第一个参数 `s` 是一个元素类型为 `T` 的切片，其余类型为 `T` 的值将会追加到该切片的末尾。

`append` 的结果是一个包含原切片所有元素加上新添加元素的切片。

## Range

`for` 循环的 `range` 形式可遍历切片或映射。

当使用 `for` 循环遍历切片时，每次迭代都会返回两个值。第一个值为当前元素的下标，第二个值为该下标所对应元素的一份副本。

## 比较

不能使用==操作符来判断两个slice是否含有全部相等元素。不过标准库提供了高度优化的bytes.Equal函数来判断两个字节型slice是否相等（[]byte），但是对于其他类型的slice，我们必须自己展开每个元素进行比较：

```Go
func equal(x, y []string) bool {
    if len(x) != len(y) {
        return false
    }
    for i := range x {
        if x[i] != y[i] {
            return false
        }
    }
    return true
}
```
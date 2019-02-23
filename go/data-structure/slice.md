# 切片

切片是轻量的包含并表示数组的一部分的结构。

## 创建

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

第 3 个用来限定新切片的容量，其用法为 slice[i:j:k]。

```go
slice := []int{1, 2, 3, 4, 5}
//长度为2-1=1，容量为3-1=2
newSlice := slice[1:2:3]
spew.Dump(slice,newSlice)
// ([]int) (len=5 cap=5) {
//  (int) 1,
//  (int) 2,
//  (int) 3,
//  (int) 4,
//  (int) 5
// }
// ([]int) (len=1 cap=2) {
//  (int) 2
// }
```

这样我们就创建了一个长度为 2-1=1，容量为 3-1=2 的新切片,不过第三个索引，不能超过原切片的最大索引值 5。

## 切片的结构

一个 slice 由三个部分构成：指针、长度和容量。

```go
type slice struct {
   array unsafe.Pointer
   len   int
   cap   int
}
```

- 指针指向第一个 slice 元素对应的底层数组元素的地址，要注意的是 slice 的第一个元素并不一定就是数组的第一个元素。
- len 长度对应 slice 中元素的数目；长度不能超过 cap 容量。

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

当原切片的长度（以下简称原长度）大于或等于 1024 时，Go 语言将会以原容量的 1.25 倍作为新容量的基准（以下新容量基准）。

切片的长度可以自动地随着其中元素数量的增长而增长，但不会随着元素数量的减少而减小。

`slice[i:j:k]`

- 长度: j – i
- 容量: k – i

## 零切片

表示底层数组的二进制内容都是零。

```go
var s = make([]int, 10)
fmt.Println(s)
------------
[0 0 0 0 0 0 0 0 0 0]
```

如果是一个指针类型的切片，那么底层数组的内容就全是 nil

```go
var s = make([]*int, 10)
fmt.Println(s)
------------
[<nil> <nil> <nil> <nil> <nil> <nil> <nil> <nil> <nil> <nil>]
```

## 空切片

在创建切片时，还有两个非常特殊的情况需要考虑，那就是容量和长度都是零的切片，叫着「空切片」，这个不同于前面说的「零值切片」。

```go
package main

import "fmt"

func main() {
    // nil 切片
    var s1 []int
    // 空切片
    var s2 []int = []int{}
    var s3 []int = make([]int, 0)
    fmt.Println(s1, s2, s3)
    fmt.Println(len(s1), len(s2), len(s3))
    fmt.Println(cap(s1), cap(s2), cap(s3))
}

-----------
[] [] []
0 0 0
0 0 0
```

上面三种形式创建的切片都是「空切片」，不过在内部结构上这三种形式是有差异的，第一种不叫「空切片」，而是叫着「 nil 切片」。

切片的零值是 `nil`。

nil 切片的长度和容量为 0 且没有底层数组。

## 向切片追加元素

为切片追加新的元素是种常用的操作，为此 Go 提供了内建的 `append` 函数。内建函数的[文档](https://go-zh.org/pkg/builtin/#append)对此函数有详细的介绍。

```go
func append(s []T, vs ...T) []T
```

`append` 的第一个参数 `s` 是一个元素类型为 `T` 的切片，其余类型为 `T` 的值将会追加到该切片的末尾。

`append` 的结果是一个包含原切片所有元素加上新添加元素的切片。

如果在创建切片时设置切片的容量和长度一样，就可以强制让新切片的第一个 append 操作创建新的底层数组，与原有的底层数组分离。新切片与原有的底层数组分离后，可以安全地进行后续修改。

- 可变参数

```go
//内置的append也是一个可变参数的函数，可以同时追加好几个值。
newSlice=append(newSlice,10,20,30)
```

- `...`操作符

```go
//通过...操作符，把一个切片追加到另一个切片里。
slice := []int{1, 2, 3, 4, 5}
newSlice := slice[1:2:3]
newSlice=append(newSlice,slice...)
spew.Dump(newSlice)
// ([]int) (len=6 cap=6) {
//  (int) 2,
//  (int) 1,
//  (int) 2,
//  (int) 3,
//  (int) 4,
//  (int) 5
// }
```

## 切片的赋值

切片的赋值是一次浅拷贝操作，拷贝的是切片变量的三个域，你可以将切片变量看成长度为 3 的 int 型数组，数组的赋值就是浅拷贝。拷贝前后两个变量共享底层数组，对一个切片的修改会影响另一个切片的内容，这点需要特别注意。

### 开头添加元素（不建议）

```go
var a=[]int{1,2,3}
// 在开头添加一个元素
a=append([]int{0},a...)
// 在开头添加一个切片
a=append([]int{-3,-2,-1},a...)
fmt.Println(a)
```

导致内存的重新分配且导致已有的元素全部复制一遍，性能较差。

### 中间插入元素

Go 语言还内置了一个 copy 函数，用来进行切片的深拷贝。
`func copy(dst, src []T) int`
copy 函数不会因为原切片和目标切片的长度问题而额外分配底层数组的内存，它只负责拷贝数组的内容，从原切片拷贝到目标切片，拷贝的量是原切片和目标切片长度的较小值 —— min(len(src), len(dst))，函数返回的是拷贝的实际长度。

```go
package main

import "fmt"

func main() {
 var s = make([]int, 5, 8)
 for i:=0;i<len(s);i++ {
  s[i] = i+1
 }
 fmt.Println(s)
 var d = make([]int, 2, 6)
 var n = copy(d, s)
 fmt.Println(n, d)
}
-----------
[1 2 3 4 5]
2 [1 2]
```

```go
// 在第i的位置插入x
i:=3
x:=9
a=append(a[:i],append([]int{x},a[i:]...)...)
//这种方式会创建一个临时切片，可以采用copy的方式避免
// 切片扩展一个空间
a=append(a,0)
// a[i:]后移一个位置
copy(a[i+1:],a[i:])
a[i]=x
//中间插入多个元素
xSlice:=[]int{2,8,33}
a=append(a,xSlice...)
copy(a[i+len(xSlice):],a[i:])
copy(a[i:],xSlice)
```

切片的高效操作在于降低内存分配的次数，尽量保证 append 操作不超过 cap 的容量。

切片每一次追加后都会形成新的切片变量，如果底层数组没有扩容，那么追加前后的两个切片变量共享底层数组，如果底层数组扩容了，那么追加前后的底层数组是分离的不共享的。如果底层数组是共享的，一个切片的内容变化就会影响到另一个切片，这点需要特别注意。

## Range

`for` 循环的 `range` 形式可遍历切片或映射。

当使用 `for` 循环遍历切片时，每次迭代都会返回两个值。第一个值为当前元素的下标，第二个值为该下标所对应元素的一份副本。

## 比较

不能使用==操作符来判断两个 slice 是否含有全部相等元素。不过标准库提供了高度优化的 bytes.Equal 函数来判断两个字节型 slice 是否相等（[]byte），但是对于其他类型的 slice，我们必须自己展开每个元素进行比较：

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

## 参考

[深入理解 Go Slice](https://github.com/EDDYCJY/blog/blob/master/golang/pkg/2018-12-11-%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3Go-Slice.md)

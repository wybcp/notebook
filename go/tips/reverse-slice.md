# 反转 slice

因为 slice 值包含指向第一个 slice 元素的指针，因此向函数传递 slice 将允许在函数内部修改底层数组的元素。换句话说，复制一个 slice 只是对底层的数组创建了一个新的 slice 别名。下面的 reverse 函数在原内存空间将[]int 类型的 slice 反转，而且它可以用于任意长度的 slice。

```go
// reverse reverses a slice of ints in place.
func reverse(s []int) {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
}
```

应用：

```go
a := [...]int{0, 1, 2, 3, 4, 5}
reverse(a[:])
fmt.Println(a) // "[5 4 3 2 1 0]"
```

## slice 元素循环向左旋转 n 个元素的方法

一种将 slice 元素循环向左旋转 n 个元素的方法是三次调用 reverse 反转函数，第一次是反转开头的 n 个元素，然后是反转剩下的元素，最后是反转整个 slice 的元素。（如果是向右循环旋转，则将第三个函数调用移到第一个调用位置就可以了。）

```go
s := []int{0, 1, 2, 3, 4, 5}
// Rotate s left by two positions.
reverse(s[:2])
reverse(s[2:])
reverse(s)
fmt.Println(s) // "[2 3 4 5 0 1]"
```

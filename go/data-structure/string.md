# [字符串](https://golang.org/pkg/strings/)

字符串是不可修改的

一个原生的字符串面值形式是`...`，使用反引号代替双引号。

## 结构

字节数组和头部字段（长度信息和指向底层字节数组的指针，结构非常类似于切片，区别是头部少了一个容量字段）。

## 按字节遍历

字符串可以通过下标来访问内部字节数组具体位置上的字节，字节是 byte 类型

```go
package main

import "fmt"

func main() {
    var s = "嘻哈china"
    for i:=0;i<len(s);i++ {
        fmt.Printf("%x ", s[i])
    }

}

-----------
e5 98 bb e5 93 88 63 68 69 6e 61
```

## 按字符 rune 遍历

```go
package main

import "fmt"

func main() {
    var s = "嘻哈china"
    for codepoint, runeValue := range s {
        fmt.Printf("%d %d ", codepoint, int32(runeValue))
    }
}

-----------
0 22075 3 21704 6 99 7 104 8 105 9 110 10 97
```

对字符串进行 range 遍历，每次迭代出两个变量 codepoint 和 runeValue。codepoint 表示字符起始位置，runeValue 表示对应的 unicode 编码（类型是 rune）。

## 字节切片和字符串的相互转换

在使用 Go 语言进行网络编程时，经常需要将来自网络的字节流转换成内存字符串，同时也需要将内存字符串转换成网络字节流。Go 语言直接内置了字节切片和字符串的相互转换语法。

```go
package main

import "fmt"

func main() {
    var s1 = "hello world"
    var b = []byte(s1)  // 字符串转字节切片
    var s2 = string(b)  // 字节切片转字符串
    fmt.Println(b)
    fmt.Println(s2)
}

--------
[104 101 108 108 111 32 119 111 114 108 100]
hello world
```

从节省内存的角度出发，底层字节数组会被拷贝。如果内容很大，那么转换操作是需要一定成本的。

那为什么需要拷贝呢？因为字节切片的底层数组内容是可以修改的，而字符串的底层字节数组是只读的，如果共享了，就会导致字符串的只读属性不再成立

## 字符函数

包 unicode 包含了一些针对测试字符的非常有用的函数（其中 ch 代表字符）：

判断是否为字母：unicode.IsLetter(ch)
判断是否为数字：unicode.IsDigit(ch)
判断是否为空白符号：unicode.IsSpace(ch)

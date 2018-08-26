# 变量

- 初始化一个变量时，请使用：`var NAME TYPE`；
- 给变量申明及赋值时，请使用： `NAME := VALUE` ；
- 给之前已经申明过的变量赋值时，请使用： `NAME = VALUE`

`var` 语句可以出现在包或函数级别。

## 基本类型

Go 的基本类型有

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // uint8 的别名

rune // int32 的别名
    // 表示一个 Unicode 码点

float32 float64

complex64 complex128
```

同导入语句一样，变量声明也可以“分组”成一个语法块。

`int`, `uint` 和 `uintptr` 在 32 位系统上通常为 32 位宽，在 64 位系统上则为 64 位宽。 当你需要一个整数值时应使用 `int` 类型，除非你有特殊的理由使用固定大小或无符号的整数类型。

## 零值

没有明确初始值的变量声明会被赋予它们的 **零值**。

零值是：

- 数值类型为 `0`，

- 布尔类型为 `false`，

- 字符串为 `""`（空字符串）。

## 类型转换

表达式 `T(v)` 将值 `v` 转换为类型 `T`。

Go 在不同类型的项之间赋值时需要显式转换。

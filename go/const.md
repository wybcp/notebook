# 常量

常量的声明与变量类似，只不过是使用 `const` 关键字。

常量可以是字符、字符串、布尔值或数值。

常量不能用 `:=` 语法声明。

常量声明和变量声明一般都会出现在包级别。

## [iota](https://golang.org/ref/spec#Iota)

遇到const关键字才会重置0

const()中每新增一个常量，iota会自动加1
# [The Go Programming Language Specification](https://golang.org/ref/spec)

Go 编程语言规范

## 注释

### C-style `/* */` block comments

包说明：介绍包以及相关信息（introduce the package and provide information relevant to the package as a whole）。

### `C++-style` `//` line comments

## 命名

MixedCaps or mixedCaps

- 包名规则：小写单词
- 变量 owner，getter：Owner；setter：SetOwner
- interface：one-method interfaces are named by the method name plus an -er suffix or similar modification to construct an agent noun: Reader, Writer, Formatter, CloseNotifier etc.

## new

分配内存并只分配 0 存储空间，返回地址`*T`。a pointer to a newly allocated zero value of type T.

## make

只用于创建 slices, maps, and channels，返回一个初始化的type T (not *T)。因为这三种类型的数据在使用前必须初始化

# [The Go Programming Language Specification](https://golang.org/ref/spec)

Go 编程语言规范

## 注释

### C-style `/* */` block comments

包说明：介绍包以及相关信息（introduce the package and provide information relevant to the package as a whole）。

每一个包应该有相关注释，在 package 语句之前的块注释将被默认认为是这个包的文档说明，其中应该提供一些相关信息并对整体功能做简要的介绍。一个包可以分散在多个文件中，但是只需要在其中一个进行注释说明即可。

### `C++-style` `//` line comments

注释（称为文档注释）出现在函数前面，例如函数 Abcd，则要以 "Abcd..." 作为开头。

## 命名

MixedCaps or mixedCaps

- 包名规则：小写单词
- 变量 owner，getter：Owner；setter：SetOwner
- interface：one-method interfaces are named by the method name plus an -er suffix or similar modification to construct an agent noun: Reader, Writer, Formatter, CloseNotifier etc.

文件名均由小写字母组成，如果文件名由多个部分组成，则使用下划线`_`对它们进行分隔。

返回某个对象的函数或方法的名称一般都是使用名词，没有 Get... 之类的字符，如果是用于修改某个对象，则使用 SetName。有必须要的话可以使用大小写混合的方式，如 MixedCaps 或 mixedCaps，而不是使用下划线来分割多个名称。

## new

分配内存并只分配 0 存储空间，返回地址`*T`。a pointer to a newly allocated zero value of type T.

## make

只用于创建 slices, maps, and channels，返回一个初始化的 `type T (not *T)`。因为这三种类型的数据在使用前必须初始化

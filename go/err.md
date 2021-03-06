# 错误

Go 语言库的实现习惯: 即使在包内部使用了 panic，但是在导出函数时会被转化为明确的错误值。

在 main 函数开头：

```go
defer func() {
        if p := recover(); p != nil {
            err = fmt.Errorf("internal error: %v", p)
        }
  }()
```

## 错误处理

在 Go 语言中，错误处理也有一套独特的编码风格。

检查某个子函数是否失败后，我们通常将处理失败的逻辑代码放在处理成功的代码之前。如果某个错误会导致函数返回，那么成功时的逻辑代码不应放在`else`语句块中，而应直接放在函数体中。

```go
f, err := os.Open("filename.ext")
if err != nil {
    // 失败的情形, 马上返回错误
    panic("ERROR occurred: " + err.Error())
}

// 正常的处理流程
```

Go 语言中大部分函数的代码结构几乎相同，首先是一系列的初始检查，用于防止错误发生，之后是函数的实际逻辑。

# [Base64](https://zh.wikipedia.org/wiki/Base64)

Base64 是一种基于 64 个可打印字符来表示二进制数据的表示方法。

在全世界通用的可见字符（62+2）组成 64 个字符

- `a~z` 26 个
- `A~Z` 26 个
- `0~9` 10 个
- `+`
- `/`

在全世界通用语言中，单字符占用的最大字节数为 3 个字节（中文是 2 个字节，英文是 1 个字节），一个字节占 8 位，也就是按二进制来表示最低位 00000000、最高位 11111111，转化为十进制，也就是 0 ～ 255 之间。

3 个字节有 24 个比特，对应于 4 个 Base64 单元，即 3 个字节可由 4 个可打印字符来表示。

##　编码的

第一步：找到中文在操作系统的字符编码表中对应十进制代码

第二步：把十进制值转换为二进制

第三步：对二进制进行重组

第四步：每一组的值再转换为十进制，去 base64 编码表找到其对应的字符，重新编码

[base64 编码原理之示例分析编码的全过程](https://mp.weixin.qq.com/s/IAcu5xNjKEq4Zwh6uRkgBA)
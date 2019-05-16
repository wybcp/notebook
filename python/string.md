# [String Methods](https://docs.python.org/3.6/library/stdtypes.html#string-methods)

| 函数 | 作用 |
| --- | --- |
| str.capitalize() | 字符串首字母大写 |
| str.casefold() | 字符串小写化，Unicode 的时候用 casefold，通用 |
| str.lower() | 字符串小写化， 只对 ASCII 也就是 'A-Z'有效，汉语 & 英语有效 |
| str.center(width[, fillchar]) | 给定宽度显示字符串 |
| str.count(sub[, start[, end]]) | sub 子字符串出现的次数 |
| str.encode(encoding="utf-8", errors="strict") | 字符串给定编码方式 |
| str.endswith(suffix[, start[, end]]) | 是否子字符串结尾 |
| str.expandtabs(tabsize=8) |  |
| str.format_map(mapping) |  |
| str.index(sub[, start[, end]]) | 返回子字符串的索引，未找到异常 ValueError |
| str.isalnum() | 返回 True，如果字符串只包含字母和数字，并且非空; |
| str.isalpha() | 返回 True，如果字符串只包含字母，并且非空 |
| str.isdecimal() | 返回 True，如果字符串只包含数字字符，并且非空; |
| str.isdigit() |  |
| str.isidentifier() |  |
| str.islower() |  |
| str.isnumeric() |  |
| str.isprintable() |  |
| str.isspace() | 返回 True，如果字符串只包含空格、制表符和换行，并且非空; |
| str.istitle() |  |
| str.isupper() |  |
| str.join(iterable) |  |
| str.ljust(width[, fillchar]) | 左对齐 |
| str.lstrip([chars]) | 删除前导空格，可以设置删除的字符 |
| str.partition(sep) |  |
| str.replace(old, new[, count]) | 替换 |
| str.rfind(sub[, start[, end]]) |  |
| str.rindex(sub[, start[, end]]) |  |
| str.rjust(width[, fillchar]) | 右对齐 |
| str.rpartition(sep) |  |
| str.rsplit(sep=None, maxsplit=-1) |  |
| str.rstrip([chars]) | 删除尾部空格 |
| str.strip([chars]) |  |
| str.title() | 字符串每个单词首字母大写 |
| str.upper() | 字符串转化为大写 |
| str.zfill(width) |  |
| Str.find(sub) | 返回第一次找到子字符串的位置 |

## format

将每个参数值替换至格式所在的位置

```python
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

## print

print 总是会以一个不可见的“新一行”字符（\n）结尾，因此重复调用 print 将会在相互独立的一行中分别打印。为防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾：

```python
print('a', end='')
print('b', end='')
```

如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加 r 或 R 来指定一个原始（Raw）字符串

## 多个界定符分割字符串

string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：

```bash
>>> line = 'asdf fjdk; afed, fjek,asdf, foo'
>>> import re
>>> re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```

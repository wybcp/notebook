# [String Methods](https://docs.python.org/3.6/library/stdtypes.html#string-methods)

| 函数                                          | 作用                                                        |
| --------------------------------------------- | ----------------------------------------------------------- |
| str.capitalize()                              | 字符串首字母大写                                            |
| str.casefold()                                | 字符串小写化，Unicode 的时候用 casefold，通用               |
| str.lower()                                   | 字符串小写化， 只对 ASCII 也就是 'A-Z'有效，汉语 & 英语有效 |
| str.center(width[, fillchar])                 | 给定宽度显示字符串                                          |
| str.count(sub[, start[, end]])                | sub 子字符串出现的次数                                      |
| str.encode(encoding="utf-8", errors="strict") | 字符串给定编码方式                                          |
| str.endswith(suffix[, start[, end]])          | 是否子字符串结尾                                            |
| str.expandtabs(tabsize=8)                     |                                                             |
| str.format_map(mapping)                       |                                                             |
| str.index(sub[, start[, end]])                | 返回子字符串的索引，未找到异常 ValueError                   |
| str.isalnum()                                 |                                                             |
| str.isalpha()                                 |                                                             |
| str.isdecimal()                               |                                                             |
| str.isdigit()                                 |                                                             |
| str.isidentifier()                            |                                                             |
| str.islower()                                 |                                                             |
| str.isnumeric()                               |                                                             |
| str.isprintable()                             |                                                             |
| str.isspace()                                 |                                                             |
| str.istitle()                                 |                                                             |
| str.isupper()                                 |                                                             |
| str.join(iterable)                            |                                                             |
| str.ljust(width[, fillchar])                  | 左对齐                                                      |
| str.lstrip([chars])                           | 删除前导空格                                                |
| str.partition(sep)                            |                                                             |
| str.replace(old, new[, count])                | 替换                                                        |
| str.rfind(sub[, start[, end]])                |                                                             |
| str.rindex(sub[, start[, end]])               |                                                             |
| str.rjust(width[, fillchar])                  | 右对齐                                                      |
| str.rpartition(sep)                           |                                                             |
| str.rsplit(sep=None, maxsplit=-1)             |                                                             |
| str.rstrip([chars])                           | 删除尾部空格                                                |
| str.strip([chars])                            |                                                             |
| str.title()                                   | 字符串每个单词首字母大写                                    |
| str.upper()                                   | 字符串转化为大写                                            |
| str.zfill(width)                              |                                                             |
| Str.find(sub)                                 | 返回第一次找到子字符串的位置                                |

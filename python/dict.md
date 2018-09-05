## 创建dict
The dict() constructor builds dictionaries directly from sequences of key-value pairs:
```
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```
dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

>>>

```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
```
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```
## 快速合并两个字典
https://mp.weixin.qq.com/s/ouyETfLFXDt0PPqSAuGQPw
```
x = {'a':1, 'b': 2} 
y = {'b':10, 'c': 11}
```
### ChainMap

```
from collections import ChainMap

z = ChainMap(x, y)
print(z)
# 字典的常用操作不变
print(list(z.values()))
print(list(z.keys()))
```
ChainMap类只是在内部创建了一个容纳这些字典的列表,并重新定义了一些常见的字典操作来遍历这个列表，并没有真正的创建字典。

如果字典中有相同的键，默认使用第一个字典中的键值。

改变z中键的值，合并前字典中的值也会改变。

### python版本是3.5以上

```
z = {**x, **y} 
print(z)
```



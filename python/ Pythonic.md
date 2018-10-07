# [Pythonic](http://lovesoo.org/tag/pythonic)

[Python](http://lovesoo.org/tag/python)最大的优点之一就是语法简洁，好的代码就像伪代码一样，干净、整洁、一目了然。要写出 [Pythonic](http://lovesoo.org/tag/pythonic)（优雅的、地道的、整洁的）代码，需要多看多学大牛们写的代码，github 上有很多非常优秀的源代码值得阅读，比如：requests、flask、tornado，下面列举一些常见的[Pythonic](http://lovesoo.org/tag/pythonic)写法。

1. 程序必须先让人读懂，然后才能让计算机执行。
   “Programs must be written for people to read, and only incidentally for machines to execute.”

1. 交换赋值

```python
##不推荐
temp = a
a = b
b = a
##推荐
a, b = b, a
# # 先生成一个元组(tuple)对象，然后unpack
```

1. Unpacking

```python
##不推荐
l = ['David', 'Pythonista', '+1-514-555-1234']
first_name = l[0]
last_name = l[1]
phone_number = l[2]

##推荐
l = ['David', 'Pythonista', '+1-514-555-1234']
first_name, last_name, phone_number = l
# Python 3 Only
first, *middle, last = another_list
```

1. 使用操作符 in

```python
##不推荐
if fruit == "apple" or fruit == "orange" or fruit == "berry":
    # 多次判断

##推荐
if fruit in ["apple", "orange", "berry"]:
    # 使用 in 更加简洁
```

1. 字符串操作

```python
##不推荐
colors = ['red', 'blue', 'green', 'yellow']

result = ''
for s in colors:
    result += s  #  每次赋值都丢弃以前的字符串对象, 生成一个新对象

##推荐
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)  #  没有额外的内存分配
```

1. 字典键值列表

```python
##不推荐
if my_dict.has_key(key):
    # ...do something with d[key]

##推荐
if key in my_dict:
    # ...do something with d[key]
```

1. 字典键值判断

```python
##不推荐
if my_dict.has_key(key):
    # ...do something with d[key]

##推荐
if key in my_dict:
    # ...do something with d[key]
```

1. 字典 get 和 setdefault 方法

```python
##不推荐
navs = {}
for (portfolio, equity, position) in data:
    if portfolio not in navs:
            navs[portfolio] = 0
    navs[portfolio] += position * prices[equity]
##推荐
navs = {}
for (portfolio, equity, position) in data:
    # 使用 get 方法
    navs[portfolio] = navs.get(portfolio, 0) + position * prices[equity]
    # 或者使用 setdefault 方法
    navs.setdefault(portfolio, 0)
    navs[portfolio] += position * prices[equity]
```

1. 判断真伪

```python
##不推荐
if x == True:
    # ....
if len(items) != 0:
    # ...
if items != []:
    # ...

##推荐
if x:
    # ....
if items:
    # ...
```

1. 遍历列表以及索引

```python
##不推荐
items = 'zero one two three'.split()
# method 1
i = 0
for item in items:
    print i, item
    i += 1
# method 2
for i in range(len(items)):
    print i, items[i]

##推荐
items = 'zero one two three'.split()
for i, item in enumerate(items):
    print i, item
```

1. 列表推导

```python
##不推荐
new_list = []
for item in a_list:
    if condition(item):
        new_list.append(fn(item))

##推荐
new_list = [fn(item) for item in a_list if condition(item)]
```

1. 列表推导-嵌套

```python
##不推荐
for sub_list in nested_list:
    if list_condition(sub_list):
        for item in sub_list:
            if item_condition(item):
                # do something...
##推荐
gen = (item for sl in nested_list if list_condition(sl) \
            for item in sl if item_condition(item))
for item in gen:
    # do something...
```

1. 循环嵌套

```python
##不推荐
for x in x_list:
    for y in y_list:
        for z in z_list:
            # do something for x &amp;amp; y

##推荐
from itertools import product
for x, y, z in product(x_list, y_list, z_list):
    # do something for x, y, z
```

1. 尽量使用生成器代替列表

```python
##不推荐
def my_range(n):
    i = 0
    result = []
    while i &amp;lt; n:
        result.append(fn(i))
        i += 1
    return result  #  返回列表

##推荐
def my_range(n):
    i = 0
    result = []
    while i &amp;lt; n:
        yield fn(i)  #  使用生成器代替列表
        i += 1
*尽量用生成器代替列表，除非必须用到列表特有的函数。
```

1. 中间结果尽量使用 imap/ifilter 代替 map/filter

```python
##不推荐
reduce(rf, filter(ff, map(mf, a_list)))

##推荐
from itertools import ifilter, imap
reduce(rf, ifilter(ff, imap(mf, a_list)))
*lazy evaluation 会带来更高的内存使用效率，特别是当处理大数据操作的时候。
```

1. 使用 any/all 函数

```python
##不推荐
found = False
for item in a_list:
    if condition(item):
        found = True
        break
if found:
    # do something if found...

##推荐
if any(condition(item) for item in a_list):
    # do something if found...
```

1. 属性(property)

```python
##不推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def setHour(self, hour):
        if 25 &amp;gt; hour &amp;gt; 0: self.__hour = hour
        else: raise BadHourException
    def getHour(self):
        return self.__hour

##推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def __setHour(self, hour):
        if 25 &amp;gt; hour &amp;gt; 0: self.__hour = hour
        else: raise BadHourException
    def __getHour(self):
        return self.__hour
    hour = property(__getHour, __setHour)
```

1. 使用 with 处理文件打开

```python
##不推荐
f = open("some_file.txt")
try:
    data = f.read()
    # 其他文件操作..
finally:
    f.close()

##推荐
with open("some_file.txt") as f:
    data = f.read()
    # 其他文件操作...
```

1. 使用 with 忽视异常(仅限[Python](http://lovesoo.org/tag/python) 3)

```python
##不推荐
try:
    os.remove("somefile.txt")
except OSError:
    pass

##推荐
from contextlib import ignored  # Python 3 only

with ignored(OSError):
    os.remove("somefile.txt")
```

1. 使用 with 处理加锁

```python
##不推荐
import threading
lock = threading.Lock()

lock.acquire()
try:
    # 互斥操作...
finally:
    lock.release()

##推荐
import threading
lock = threading.Lock()

with lock:
    # 互斥操作...
```

## 参考

1. Idiomatic Python: <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>
2. PEP 8: Style Guide for Python Code: <http://www.python.org/dev/peps/pep-0008/>
3. 译文：<http://lovesoo.org/pythonic-python-programming.html>

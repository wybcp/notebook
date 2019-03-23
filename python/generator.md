# 生成器（Generators）

生成器是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。

```python
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
```

## 可迭代对象(Iterable)

Python 中任意的对象，只要它定义了可以返回一个迭代器的`__iter__`方法，或者定义了可以支持下标索引的`__getitem__`方法，那么它就是一个可迭代对象。

str 是一个可迭代对象，而不是一个迭代器。这意味着它支持迭代，但我们不能直接对其进行迭代操作。内置函数`iter()`，它将根据一个可迭代对象返回一个迭代器对象。

## 迭代器(Iterator)

任意对象，只要定义了`__next__`方法，它就是一个迭代器。

### 跳过可迭代对象的开始部分

遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。

`itertools` 模块中有一些函数可以完成这个任务。首先介绍的是 `itertools.dropwhile()` 函数。使用时，你给它传递一个函数对象和一个可迭代对象。 它会返回一个迭代器对象，丢弃原有序列中直到函数返回 Flase 之前的所有元素，然后返回后面所有元素。

```bash
>>> from itertools import dropwhile
>>> with open('/etc/passwd') as f:
...     for line in dropwhile(lambda line: line.startswith('#'), f):
...         print(line, end='')
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

函数 `dropwhile()` 避免写出下面这种冗余代码：

```python
with open('/etc/passwd') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)
```

这样写确实可以跳过开始部分的注释行，但是同样也会跳过文件中其他所有的注释行。

## 排列组合

迭代遍历一个集合中元素的所有可能的排列或组合

itertools 模块提供了三个函数来解决这类问题。

### `itertools.permutations()`

接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。

```bash
>>> items = ['a', 'b', 'c']
>>> from itertools import permutations
>>> for p in permutations(items):
...     print(p)
...
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
```

指定长度的所有排列，传递一个可选的长度参数。

```bash
>>> for p in permutations(items, 2):
...     print(p)
...
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
```

### `itertools.combinations()`

得到输入集合中元素的所有的组合。比如：

```bash
>>> from itertools import combinations
>>> for c in combinations(items, 3):
...     print(c)
...
('a', 'b', 'c')

>>> for c in combinations(items, 2):
...     print(c)
...
('a', 'b')
('a', 'c')
('b', 'c')

>>> for c in combinations(items, 1):
...     print(c)
...
('a',)
('b',)
('c',)
```

### `itertools.combinations_with_replacement()`

允许同一个元素被选择多次，

```bash
>>> for c in combinations_with_replacement(items, 3):
...     print(c)
...
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
>>>
```

## 同时迭代多个序列

同时迭代多个序列，每次分别从一个序列中取一个元素。

使用 `zip()` 函数：

```bash
>>> xpts = [1, 5, 4, 2, 10, 7]
>>> ypts = [101, 78, 37, 15, 62, 99]
>>> for x, y in zip(xpts, ypts):
...     print(x,y)
...
1 101
5 78
4 37
2 15
10 62
7 99
>>>
```

`zip(a, b)` 会生成一个可返回元组 `(x, y)` 的迭代器，其中 x 来自 a，y 来自 b。 一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。

使用 `itertools.zip_longest()` 函数，迭代长度跟参数中最长序列长度一致：

```bash
>>> from itertools import zip_longest
>>> for i in zip_longest(a,b):
...     print(i)
...
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
```

`zip()` 会创建一个迭代器来作为结果返回。如果你需要将结对的值存储在列表中，要使用 `list()` 函数：

```bash
>>> zip(a, b)
<zip object at 0x1007001b8>
>>> list(zip(a, b))
[(1, 10), (2, 11), (3, 12)]
>>>
```

## 不同集合上元素的迭代

在多个对象执行相同的操作，但是这些对象在不同的容器中。

`itertools.chain()` 方法可以用来简化这个任务。它接受一个可迭代对象列表作为输入，并返回一个迭代器，有效的屏蔽掉在多个容器中迭代细节，比先将序列合并再迭代要高效的多。

```bash
>>> from itertools import chain
>>> a = [1, 2, 3, 4]
>>> b = ['x', 'y', 'z']
>>> for x in chain(a, b):
... print(x)
...
1
2
3
4
x
y
z
```

## 展开嵌套的序列

将一个多层嵌套的序列展开成一个单层列表

写一个包含 `yield from` 语句的递归生成器来轻松解决这个问题。

```python
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
```

`isinstance(x, Iterable)` 检查某个元素是否是可迭代的。 `yield from` 返回所有子例程的值。

额外的参数 `ignore_types` 和检测语句 `isinstance(x, ignore_types)` 用来将字符串和字节排除在可迭代对象外，防止将它们再展开成单个的字符。

语句 `yield from` 在你想在生成器中调用其他生成器作为子例程的时候非常有用。

# 字典

## 创建 dict

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

```python
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

字典推导式：

```bash
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

键值对创建字典：

```bash
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

## 快速合并两个字典

```python
from collections import ChainMap
x = {'a':1, 'b': 2}
y = {'b':10, 'c': 11}
z = ChainMap(x, y)
print(z)
# 字典的常用操作不变
print(list(z.values()))
print(list(z.keys()))
```

ChainMap 类只是在内部创建了一个容纳这些字典的列表,并重新定义了一些常见的字典操作来遍历这个列表，并没有真正的创建字典。

如果字典中有相同的键，默认使用第一个字典中的键值。

改变 z 中键的值，合并前字典中的值也会改变。

### python 版本是 3.5 以上

```python
z = {**x, **y}
print(z)
```

## `OrderedDict`

`collections` 模块中的 `OrderedDict` 类。 在迭代操作的时候它会保持元素被插入时的顺序：

```python
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
```

`OrderedDict` 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候，它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。

注意：一个 `OrderedDict` 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。

## 字典计算操作

为了对字典值执行计算操作，通常需要使用 `zip()` 函数先将键和值反转过来：

```python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
```

zip() 函数创建的是一个只能访问一次的迭代器。当多个键值对拥有相同的值的时候，键会决定返回结果。

可以使用 zip() 和 sorted() 函数来排列字典数据：

```python
prices_sorted = sorted(zip(prices.values(), prices.keys()))
```

## 查找两字典的相同点

字典键的集合操作。

```python
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
```

## 通过某个关键字排序一个字典列表

通过使用 `operator` 模块的 `itemgetter` 函数，可以非常容易的排序这样的数据结构。

```python
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
```

itemgetter() 有时候也可以用 lambda 表达式代替，比如：

```python
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
```

使用 itemgetter() 方式会运行的稍微快点。因此，如果你对性能要求比较高的话就使用 itemgetter() 方式。

## 通过某个字段将记录分组

首先需要按照指定的字段(这里就是 date )排序， 然后调用 itertools.groupby() 函数：

```python
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
```

groupby() 函数扫描整个序列并且查找连续相同值（或者根据指定 key 函数返回值相同）的元素序列。在每次迭代的时候，它会返回一个值和一个迭代器对象，这个迭代器对象可以生成元素值全部等于上面那个值的组中所有对象。

一个非常重要的准备步骤是要根据指定的字段将数据排序。因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。
# list 列表

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标。

```python
enumerate(sequence, [start=0])
```

- sequence  一个序列、迭代器或其他支持迭代对象。
- start 下标起始位置。

## 翻转

```python
a = [1, 2, 3, 4]
a[::-1] # 不推荐。好吧，自从学了切片我一直用的这个
list(reversed(a))   # 不推荐
a.reverse() #推荐
```

速度最快，使用内置函数。

## 删除部分 values

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# now remove them
letters[2:5] = []
# or
del letters[2:5]
letters
Out[6]: ['a', 'b', 'f', 'g']
```

## 删除单一值

值：

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Remove the first item from the list whose value is x. It is an error if there is no such item.
letters.remove('b')
```

索引：

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# If no index is specified, a.pop() removes and returns the last item in the list.
letters.pop(1)
```

## 返回索引值

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Raises a ValueError if there is no such item.def index(self, value, start=None, stop=None)
letters.index('b',3)
```

## 复制

### =复制的是内存地址

```python
x=[1,2,3]
y=x
y[2]=4
print('x list is :',x)
print('y list is :',y)
```

output:

```python
x list is : [1, 2, 4]
y list is : [1, 2, 4]
```

### 单独复制

```python
x=[1,2,3]
# y=list(x)
y=x[:]
y[2]=4
print('x list is :',x)
print('y list is :',y)
```

output:

```python
x list is : [1, 2, 3]
y list is : [1, 2, 4]
```

## Queues

first-in, first-out

```bash
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

## 列表推导式

```bash
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#build-in function
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## [create 2D array](https://love-python.blogspot.tw/2018/04/create-2d-array-using-list-in-python.html)

```python
m=3
n=4
aa=[[0]*m]*n
# <class 'list'>: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
aa[0][0]=1
# <class 'list'>: [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
ara = [[0] * m for i in range(n)]
ara[0][0]=1
# <class 'list'>: [[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

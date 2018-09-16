# 容器(Collections)

## defaultdict

`defaultdict`，与`dict`类型不同，不需要检查**key**是否存在：

```python
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
```

## counter

Counter 是一个计数器，它可以帮助我们针对某项数据进行计数。

```python
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

## 输出:
## Counter({
##     'Yasoob': 2,
##     'Ali': 2,
##     'Arham': 1,
##     'Ahmed': 1
##  })
```

## deque

deque 提供了一个双端队列，你可以从头/尾两端添加或删除元素。

```python
from collections import deque
d = deque()
```

你可以从两端取出(pop)数据：

```python
d = deque(range(5))
print(len(d))

## 输出: 5

d.popleft()

## 输出: 0

d.pop()

## 输出: 4

print(d)

## 输出: deque([1, 2, 3])
```

限制列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去(pop)。

```python
d = deque(maxlen=30)
```

现在当你插入 30 条数据时，最左边一端的数据将从队列中删除。

从任一端扩展这个队列中的数据：

```python
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)

## 输出: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

## namedtuple

一个元组是一个不可变的列表，你可以存储一个数据的序列，它和命名元组(`namedtuples`)非常像，但有几个关键的不同。

为了获取元组中的数据，你需要使用整数作为索引：

```python
man = ('Ali', 30)
print(man[0])

## 输出: Ali
```

把元组变成一个针对简单任务的容器。字典(`dict`)一样访问`namedtuples`，但`namedtuples`是不可变的。

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)

## 输出: Animal(name='perry', age=31, type='cat')

print(perry.name)

## 输出: 'perry'
```

**namedtuple 的每个实例没有对象字典**，所以它们很轻量，与普通的元组比，并不需要更多的内存。

## enum.Enum (Python 3.4+)

枚举对象，它属于`enum`模块，存在于 Python 3.4 以上版本中。

Enums(枚举类型)基本上是一种组织各种东西的方式。

```python
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2   # (译者注：幼小的狗狗)

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)
```

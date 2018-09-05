# dataclasses

Python3.7 加入了一个新的 module：dataclasses。可以简单的理解成“支持默认值、可以修改的 tuple”（ “mutable namedtuples with defaults”）。其实没什么特别的，就是你定义一个很普通的类，`@dataclass` 装饰器可以帮你生成 `__repr__` `__init__` 等等方法，就不用自己写一遍了。但是此装饰器返回的依然是一个 class，这意味着并没有带来任何不便，你依然可以使用继承、metaclass、docstring、定义方法等。

先展示一个 PEP 中举的例子，下面的这段代码（Python3.7）：

```python
@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

`@dataclass` 会自动生成

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0) -> None:
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
def __repr__(self):
    return f'InventoryItem(name={self.name!r}, unit_price={self.unit_price!r}, quantity_on_hand={self.quantity_on_hand!r})'
def __eq__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) == (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __ne__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) != (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __lt__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) < (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __le__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) <= (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __gt__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) > (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __ge__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) >= (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
```

## 引入 dataclass 的理念

Python 想简单的定义一种容器，支持通过的对象属性进行访问。在这方面已经有很多尝试了：

1. 标准库的 `collections.namedtuple`
2. 标准库的 `typing.NamedTuple`
3. 著名的 [attr 库](https://github.com/python-attrs/attrs)
4. 各种 [Snippet，问题和回答](https://www.python.org/dev/peps/pep-0557/#id19)等

那么为什么还需要 dataclass 呢？主要的好处有：

1. 没有使用 BaseClass 或者 metaclass，不会影响代码的继承关系。被装饰的类依然是一个普通的类
2. 使用类的 Fields 类型注解，用原生的方法支持类型检查，不侵入代码，不像 attr 这种库对代码有侵入性（要用 attr 的函数将一些东西处理）

dataclass 并不是要取代这些库，作为标准库的 dataclass 只是提供了一种更加方便使用的途径来定义 Data Class。以上这些库有不同的 feature，依然有存在的意义。

## 基本用法

dataclasses 的 dataclass 装饰器的原型如下：

```python
def dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
```

很明显，这些默认参数可以控制是否生成魔术方法。通过本文开头的例子可以看出，不用加括号也可以调用。

通过 field 可以对参数做更多的定制化，比如默认值、是否参与 repr、是否参与 hash 等。比如文档中的这个例子，由于 `mylist` 的缺失，就调用了 `default_factory` 。更多 field 能做的事情[参考文档](https://docs.python.org/3.7/library/dataclasses.html#dataclasses.field)吧。

```python
@dataclass
class C:
    mylist: List[int] = field(default_factory=list)

c = C()
c.mylist += [1, 2, 3]
```

此外，dataclasses 模块还提供了很多有用的函数，可以将 dataclass 转换成 tuple、dict 等形式。话说我自己重复过很多这样的方法了……

```python
@dataclass
class Point:
     x: int
     y: int

@dataclass
class C:
     mylist: List[Point]

p = Point(10, 20)
assert asdict(p) == {'x': 10, 'y': 20}

c = C([Point(0, 0), Point(10, 4)])
assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}
```

## Hook init

自动生成的 `__init__` 可以被 hook。很简单，自动生成的 `__init__` 方法会调用 `__post_init__`

```python
@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b
```

如果想传给 `__post_init__` 方法但是不传给 `__init__` ，可以使用一个特殊的类型 `InitVar`

```python
@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database=my_database)
```

## 不可修改的功能

Python 没有 const 类似的东西，理论上任何东西都是可以修改的。如果非要说不能修改的实现呢，这里有个[比较著名的实现](http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991)。只有不到 10 行代码。

但是有了 dataclass ，可以直接使用 `@dataclass(frozen=True)` 了。然后装饰器会对 Class 添加上 `__setattr__` 和 `__delattr__` 。Raise 一个 [FrozenInstanceError](https://docs.python.org/3.7/library/dataclasses.html#dataclasses.FrozenInstanceError)。缺点是会有一些性能损失，因为 `__init__` 必须通过 `object.__setattr__` 。

## 继承

对于有继承关系的 dataclass，会按照 MRO 的反顺序（从 object 开始），对于每一个基类，将在基类找到的 fields 添加到顺序的一个 mapping 中。所有的基类都找完了，按照这个 mapping 生成所有的魔术方法。所以方法中这些参数的顺序，是按照找到的顺序排的，先找到的排在前面。因为是先找的基类，所以相同 name 的话，后面子类的 fields 定义会覆盖基类的。比如文档中的这个例子：

```python
@dataclass
class Base:
    x: Any = 15.0
    y: int = 0

@dataclass
class C(Base):
    z: int = 10
    x: int = 15
```

那么最后生成的将会是：

```python
def __init__(self, x: int = 15, y: int = 0, z: int = 10):
```

注意 x y 的顺序是 Base 中的顺序，但是 C 的 x 是 int 类型，覆盖了 Base 中的 Any。

## 可变对象的陷阱

在前面的“基本用法”一节中，使用了 default_factory 。为什么不直接使用 `[]` 作为默认呢？

老鸟都会知道 Python 这么一个坑：将可变对象比如 list 作为函数的默认参数，那么这个参数会被缓存，导致意外的错误。详细的可以参考这里：[Python Common Gotchas](http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments)。

考虑到下面的代码：

```python
@dataclass
class D:
    x: List = []
    def add(self, element):
        self.x += element
```

将会生成：

```python
class D:
    x = []
    def __init__(self, x=x):
        self.x = x
    def add(self, element):
        self.x += element

assert D().x is D().x
```

这样无论实例化多少对象，`x` 变量将在多个实例之间共享。dataclass 很难有一个比较好的办法预防这种情况。所以这个地方做的设计是：如果默认参数的类型是 `list` `dict` 或 `set` ，就抛出一个 TypeError。虽然不算完美，但是可以预防很大一部分情况了。

如果默认参数需要是 list，那么就用上面提到的 [default_factory](https://docs.python.org/3.7/library/dataclasses.html#default-factory-functions) 。

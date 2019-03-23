# 函数

每一个函数都在其末尾隐含了一句 `return None`，除非你写了你自己的 return 语句。

`*args` 和 `**kwargs` 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。

## `*args`

`*args` 是用来发送一个非键值对的可变数量的参数列表给一个函数。

## `**kwargs`

`**kwargs` 允许你将不定长度的键值对, 作为参数传递给一个函数。

## `Map`

Map 会将一个函数映射到一个输入列表的所有元素上。`map(function_to_apply, list_of_inputs)`

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

使用匿名函数(lambdas)来配合`map`

## 默认参数

默认参数的值应该是不可变的对象，比如 None、True、False、数字或字符串。

## `Filter`

`filter`过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，`符合要求`即函数映射到该元素时返回值为 True：

```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))

# Output: [-5, -4, -3, -2, -1]
```

## 函数缓存

函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。

当一个 I/O 密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。

在 Python 3.2 以后版本，有个 lru_cache 的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。

## 元信息

使用函数参数注解，提示程序员应该怎样正确使用这个函数。

```python
def add(x:int, y:int) -> int:
    return x + y
```

python 解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距。然而，对于那些阅读源码的人来讲就很有帮助啦。

函数注解只存储在函数的 `__annotations__` 属性中。

```python
>>> add.__annotations__
{'y': <class 'int'>, 'return': <class 'int'>, 'x': <class 'int'>}
```

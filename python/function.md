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

## `Filter`

`filter`过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，`符合要求`即函数映射到该元素时返回值为 True.：

```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))

# Output: [-5, -4, -3, -2, -1]
```

## 函数缓存

函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。

当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。

在Python 3.2以后版本，有个lru_cache的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。
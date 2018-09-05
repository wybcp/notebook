# [Python 中字符串拼接的 N 种方法](https://my.oschina.net/mutoushirana/blog/1861267)

python 拼接字符串一般有以下几种方法：

## 直接通过（+）操作符拼接

```python
s = 'Hello'+' '+'World'+'!'
print(s)
```

输出结果：_Hello World!_

使用这种方式进行字符串连接的操作效率低下，因为 python 中使用 + 拼接两个字符串时会生成一个新的字符串，生成新的字符串就需要重新申请内存，当拼接字符串较多时自然会影响效率。

## 通过 str.join()方法拼接**

```python
strlist=['Hello',' ','World','!']
print(''.join(strlist))
```

输出结果：_Hello World!_

这种方式一般常使用在将集合转化为字符串，''.join()其中''可以是空字符，也可以是任意其他字符，当是任意其他字符时，集合中字符串会被该字符隔开，例如：

```python
strlist=['Hello',' ','World','!']
print(','.join(strlist))
```

输出结果：_Hello, ,World,!_

** 通过 str.format()方法拼接

```python
s='{} {}!'.format('Hello','World')
print(s)
```

输出结果：_Hello World!_

通过这种方式拼接字符串需要注意的是字符串中{}的数量要和 format 方法参数数量一致，否则会报错。

** 通过(%)操作符拼接

```python
s = '%s %s!' % ('Hello', 'World')
print(s)
```

输出结果：_Hello World!_

这种方式与 str.format()使用方式基本一致。

** 通过()多行拼接

```python
s = (
    'Hello'
    ' '
    'World'
    '!'
)
print(s)
```

输出结果：_Hello World!_

python 遇到未闭合的小括号，自动将多行拼接为一行。

** 通过 string 模块中的 Template 对象拼接

```python
from string import Template
s = Template('${s1} ${s2}!')
print(s.safe_substitute(s1='Hello',s2='World'))
```

输出结果：_Hello World!_

Template 的实现方式是首先通过 Template 初始化一个字符串。这些字符串中包含了一个个 key。通过调用 substitute 或 safe_subsititute，将 key 值与方法中传递过来的参数对应上，从而实现在指定的位置导入字符串。这种方式的好处是不需要担心参数不一致引发异常，如：

```python
from string import Template
s = Template('${s1} ${s2} ${s3}!')
print(s.safe_substitute(s1='Hello',s2='World'))
```

输出结果：_Hello World ${s3}!_

** 通过 F-strings 拼接

在 python3.6.2 版本中，PEP 498 提出一种新型字符串格式化机制，被称为“字符串插值”或者更常见的一种称呼是**F-strings，**F-strings 提供了一种明确且方便的方式将 python 表达式嵌入到字符串中来进行格式化：

```python
s1='Hello'
s2='World'
print(f'{s1} {s2}!')
```

输出结果：_Hello World!_

在 F-strings 中我们也可以执行函数：

```python
def power(x):
    return x*x
x=4
print(f'{x} * {x} = {power(x)}')
```

输出结果：_4 \* 4 = 16_

而且 F-strings 的运行速度很快，比%-string 和 str.format()这两种格式化方法都快得多。

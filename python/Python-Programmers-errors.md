# [易犯的错误](https://www.oschina.net/translate/top-10-mistakes-that-python-programmers-make)

## 1: 滥用表达式作为函数参数的默认值

Python 允许为函数的参数提供默认的可选值，但是它可能会导致一些易变默认值的混乱。例如，看一下这个 Python 函数的定义：

```bash
>>> def foo(bar=[]):        # bar is optional and defaults to [] if not specified
...    bar.append("baz")    # but this line could be problematic, as we'll see...
...    return bar
```

一个常见的错误是认为在函数每次不提供可选参数调用时可选参数将设置为默认指定值。在上面的代码中，例如，人们可能会希望反复（即不明确指定 bar 参数）地调用 foo()时总返回'baz'，由于每次 foo()调用时都假定（不设定 bar 参数）bar 被设置为[]（即一个空列表）。

```bash
>>> foo()
["baz"]>>> foo()
["baz", "baz"]>>> foo()
["baz", "baz", "baz"]
```

耶？为什么每次 foo()调用时都要把默认值"baz"追加到现有列表中而不是创建一个新的列表呢？

答案是函数参数的默认值只会评估使用一次—在函数定义的时候。因此，bar 参数在初始化时为其默认值（即一个空列表），即 foo()首次定义的时候，但当调用 foo()时（即，不指定 bar 参数时）将继续使用 bar 原本已经初始化的参数。

下面是一个常见的解决方法：

```bash
>>> def foo(bar=None):
...    if bar is None:        # or if not bar:
...        bar = []
...    bar.append("baz")
...    return bar
...
>>> foo()
["baz"]
>>> foo()
["baz"]
>>> foo()
["baz"]
```

## 2: 错误地使用类变量

考虑一下下面的例子：

```bash
>>> class A(object):
...     x = 1
...
>>> class B(A):
...     pass
...
>>> class C(A):
...     pass
...
>>> print A.x, B.x, C.x
1 1 1
```

常规用一下。

```bash
>>> B.x = 2
>>> print A.x, B.x, C.x
1 2 1
```

嗯，再试一下也一样。

```bash
>>> A.x = 3
>>> print A.x, B.x, C.x
3 2 3
```

什么 $%#!&?? 我们只改了 A.x，为什么 C.x 也改了?

在 Python 中，类变量在内部当做字典来处理，其遵循常被引用的方法解析顺序（[MRO](https://python-history.blogspot.jp/2010/06/method-resolution-order.html)）。所以在上面的代码中，由于 class C 中的 x 属性没有找到，它会向上找它的基类（尽管 Python 支持多重继承，但上面的例子中只有 A）。换句话说，class C 中没有它自己的 x 属性，其独立于 A。因此，C.x 事实上是 A.x 的引用。

## 3: 为 except 指定错误的参数

假设你有如下一段代码：

```bash
>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except ValueError, IndexError:  # To catch both exceptions, right?
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range
```

这里的问题在于 except 语句并不接受以这种方式指定的异常列表。相反，在 Python 2.x 中，使用语法 except Exception, e 是将一个异常对象绑定到第二个可选参数（在这个例子中是 e）上，以便在后面使用。所以，在上面这个例子中，IndexError 这个异常并不是被 except 语句捕捉到的，而是被绑定到一个名叫 IndexError 的参数上时引发的。

在一个 except 语句中捕获多个异常的正确做法是将第一个参数指定为一个含有所有要捕获异常的元组。并且，为了代码的可移植性，要使用 as 关键词，因为 Python 2 和 Python 3 都支持这种语法：

```bash
>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except (ValueError, IndexError) as e:
...     pass
```

## 4: 不理解 Python 的作用域

Python 是基于 [LEGB](https://blog.mozilla.org/webdev/2011/01/31/python-scoping-understanding-legb/) 来进行作用于解析的, LEGB 是 Local, Enclosing, Global, Built-in 的缩写。看下面一段代码：

```bash
>>> x = 10
>>> def foo():
...     x += 1
...     print x
...
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'x' referenced before assignment
```

这里出什么问题了？

上面的问题之所以会发生是因为当你给作用域中的一个**变量赋值**时，Python 会自动的把它当做是当前作用域的局部变量，从而会隐藏外部作用域中的同名变量。

很多人会感到很吃惊，当他们给之前可以正常运行的代码的函数体的某个地方添加了一句赋值语句之后就得到了一个 UnboundLocalError 的错误。 (你可以在这里了解到更多)

尤其是当开发者使用 lists 时，这个问题就更加常见. 请看下面这个例子：

```bash
>>> lst = [1, 2, 3]
>>> def foo1():
...     lst.append(5)   # 没有问题...
...
>>> foo1()
>>> lst
[1, 2, 3, 5]

>>> lst = [1, 2, 3]
>>> def foo2():
...     lst += [5]      # ... 但是这里有问题!
...
>>> foo2()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'lst' referenced before assignment
```

嗯？为什么 foo2 报错，而 foo1 没有问题呢？

原因和之前那个例子的一样，不过更加令人难以捉摸。foo1 没有对 lst 进行赋值操作，而 foo2 做了。要知道， lst += [5] 是 lst = lst + [5] 的缩写，我们试图对 lst 进行赋值操作（Python 把他当成了局部变量）。此外，我们对 lst 进行的赋值操作是基于 lst 自身（这再一次被 Python 当成了局部变量），但此时还未定义。因此出错！

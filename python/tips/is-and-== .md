# is 和 == 的区别

官方文档中说 `is` 表示的是对象标示符（object identity），而 `==`表示的是相等（equality）。

`is` 的作用是用来检查对象的标示符是否一致，也就是比较两个对象在内存中的地址是否一样，而 `==` 是用来检查两个对象是否相等。

一般情况下，如果 `a is b` 返回 True 的话，即 a 和 b 指向同一块内存地址的话，`a == b` 也返回 True，即 a 和 b 的值也相等。

## 字符串驻留机制

```bash
>>> a="hello"
>>> b="hello"
>>> id(a)
4360372720
>>> id(b)
4360372720
>>> d="hello world"
>>> c="hello world"
>>> id(c)
4360369584
>>> id(d)
4360369520
```

对于较小的字符串，为了提高系统性能 Python 会保留其值的一个副本，当创建新的字符串的时候直接指向该副本即可。所以 "hello" 在内存中只有一个副本，a 和 b 的 id 值相同，而 "hello world" 是长字符串，不驻留内存，Python 中各自创建了对象来表示 a 和 b，所以他们的值相同但 id 值不同。

总结一下，is 是检查两个对象是否指向同一块内存空间，而 == 是检查他们的值是否相等。可以看出，is 是比 == 更严格的检查，is 返回 True 表明这两个对象指向同一块内存，值也一定相同。

## Python 里和 None 比较时，为什么是 is None 而不是 == None 呢？

这是因为 None 在 Python 里是个单例对象，一个变量如果是 None，它一定和 None 指向同一个内存地址。而 `== None`背后调用的是`__eq__`，而`__eq__`可以被重载，下面是一个 `is not None`但 `== None`的例子

```python
class Foo(object):
    def __eq__(self, other):
        return True

f = Foo()
print(f == None)  # 输出 True
print(f is None)  # 输出 False
```

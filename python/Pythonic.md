# [Pythonic](http://lovesoo.org/tag/pythonic)

Python最大的优点之一就是语法简洁，好的代码就像伪代码一样，干净、整洁、一目了然。要写出 [Pythonic](http://lovesoo.org/tag/pythonic)（优雅的、地道的、整洁的）代码，需要多看多学大牛们写的代码，

## 类的命名规范

类的名称应该像大多数其他语言一样使用驼峰大小写。

## 变量和函数

使用小写字母命名函数和变量，并用下划线分隔单词，提高代码可读性。

## **使用文档字符串**

Docstrings 可以在 Python 中声明代码的功能的。通常在方法，类和模块的开头使用。 docstring 是该对象的 **doc** 特殊属性。 Python 官方语言建议使用 “” 三重双引号 “” 来编写文档字符串。

- 即使字符串符合一行，也会使用三重引号。当你想要扩展时，这种注释非常有用。

- 三重引号中的字符串前后不应有任何空行。
  
- 使用句点（.）结束 docstring 中的语句
  
  类似地，可以应用 Python 多行 docstring 规则来编写多行 docstring。在多行上编写文档字符串是用更具描述性的方式记录代码的一种方法。你可以利用 Python 多行文档字符串在 Python 代码中编写描述性文档字符串，而不是在每一行上编写注释。 **多行的 docstring**

  ```python
  def call_weather_api(url, location):
      """Get the weather of specific location.
      
      Calling weather api to check for weather by using weather api and 
      location. Make sure you provide city name only, country and county 
      names won't be accepted and will throw exception if not found the 
      city name.
  
      :param url:URL of the api to get weather.
      :type url: str
      :param location:Location of the city to get the weather.
      :type location: str
      :return: Give the weather information of given location.
      :rtype: str"""
  ```

- 第一行是函数或类的简要描述
- 每一行语句的末尾有一个句号
- 文档字符串中的简要描述和摘要之间有一行空白

如果使用 Python3.6 可以使用类型注解对上面的 docstring 以及参数的声明进行修改。

```python
def call_weather_api(url: str, location: str) -> str:
    """Get the weather of specific location.
    
    Calling weather api to check for weather by using weather api and 
    location. Make sure you provide city name only, country and county 
    names won't be accepted and will throw exception if not found the 
    city name.
    """
```

如果使用 Python 代码中的类型注解，则不需要再编写参数信息。

### **模块级别的 docstring**

一般在文件的顶部放置一个模块级的 docstring 来简要描述模块的使用。 这些注释应该放在在导包之前，模块文档字符串应该表明模块的使用方法和功能。 如果觉得在使用模块之前客户端需要明确地知道方法或类，你还可以简要地指定特定方法或类。

```python
"""This module contains all of the network related requests. 
This module will check for all the exceptions while making the network 
calls and raise exceptions for any unknown exception.
Make sure that when you use this module,
you handle these exceptions in client code as:
NetworkError exception for network calls.
NetworkNotFound exception if network not found.
"""

import urllib3
import json
```

在为模块编写文档字符串时，应考虑执行以下操作：

- 对当前模块写一个简要的说明
- 如果想指定某些对读者有用的模块，如上面的代码，还可以添加异常信息，但是注意不要太详细。

- 将模块的 docstring 看作是提供关于模块的描述性信息的一种方法，而不需要详细讨论每个函数或类具体操作方法。 **类级别的 docstring** 类 docstring 主要用于简要描述类的使用及其总体目标。 让我们看一些示例，看看如何编写类文档字符串 **单行类 docstring**

## 常见的[Pythonic](http://lovesoo.org/tag/pythonic)写法

1. 程序必须先让人读懂，然后才能让计算机执行。

   “Programs must be written for people to read, and only incidentally for machines to execute.”

2. 交换赋值

   ```python
   ##不推荐
   temp = a
   a = b
   b = a
   ##推荐
   a, b = b, a
   # 先生成一个元组(tuple)对象，然后unpack
   ```

3. Unpacking

   ```python
   ##不推荐
   l = ['David', 'Pythonista', '+1-514-555-1234']
   first_name = l[0]
   last_name = l[1]
   phone_number = l[2]
   
   ##推荐
   l = ['David', 'Pythonista', '+1-514-555-1234']
   first_name, last_name, phone_number = l
   # Python 3 Only
   first, *middle, last = another_list
   ```

4. 使用操作符 in

   ```python
   ##不推荐
   if fruit == "apple" or fruit == "orange" or fruit == "berry":
    # 多次判断
   
   ##推荐
   if fruit in ["apple", "orange", "berry"]:
       # 使用 in 更加简洁
   ```

5. 字符串操作

   ```python
   ##不推荐
   colors = ['red', 'blue', 'green', 'yellow']
   
   result = ''
   for s in colors:
       result += s  #  每次赋值都丢弃以前的字符串对象, 生成一个新对象
   
   ##推荐
   colors = ['red', 'blue', 'green', 'yellow']
   result = ''.join(colors)  #  没有额外的内存分配
   ```

6. 字典键值判断

   ```python
   ##不推荐
   if my_dict.has_key(key):
       # ...do something with d[key]
   
   ##推荐
   if key in my_dict:
       # ...do something with d[key]
   ```

7. 字典 get 和 setdefault 方法

   ```python
   ##不推荐
   navs = {}
   for (portfolio, equity, position) in data:
       if portfolio not in navs:
               navs[portfolio] = 0
       navs[portfolio] += position * prices[equity]
   ##推荐
   navs = {}
   for (portfolio, equity, position) in data:
       # 使用 get 方法
       navs[portfolio] = navs.get(portfolio, 0) + position * prices[equity]
       # 或者使用 setdefault 方法
       navs.setdefault(portfolio, 0)
       navs[portfolio] += position * prices[equity]
   ```

8. 判断真伪

   ```python
   ##不推荐
   if x == True:
       # ....
   if len(items) != 0:
       # ...
   if items != []:
       # ...
   
   ##推荐
   if x:
       # ....
   if items:
       # ...
   ```

9. 遍历列表以及索引

   ```python
   ##不推荐
   items = 'zero one two three'.split()
   # method 1
   i = 0
   for item in items:
       print i, item
       i += 1
   # method 2
   for i in range(len(items)):
       print i, items[i]
   
   ##推荐
   items = 'zero one two three'.split()
   for i, item in enumerate(items):
       print i, item
   ```

10. 列表推导

    ```python
    ##不推荐
    new_list = []
    for item in a_list:
        if condition(item):
            new_list.append(fn(item))
    
    ##推荐
    new_list = [fn(item) for item in a_list if condition(item)]
    ```

11. 列表推导-嵌套

    ```python
    ##不推荐
    for sub_list in nested_list:
        if list_condition(sub_list):
            for item in sub_list:
                if item_condition(item):
                    # do something...
    ##推荐
    gen = (item for sl in nested_list if list_condition(sl) \
                for item in sl if item_condition(item))
    for item in gen:
        # do something...
    ```

12. 循环嵌套

    ```python
    ##不推荐
    for x in x_list:
        for y in y_list:
            for z in z_list:
                # do something for x & y
    
    ##推荐
    from itertools import product
    for x, y, z in product(x_list, y_list, z_list):
        # do something for x, y, z
    ```

13. 尽量使用生成器代替列表

    ```python
    ##不推荐
    def my_range(n):
        i = 0
        result = []
        while i < n:
            result.append(fn(i))
            i += 1
        return result  #  返回列表
    
    ##推荐
    def my_range(n):
        i = 0
        result = []
        while i < n:
            yield fn(i)  #  使用生成器代替列表
            i += 1
    ```

14. 中间结果尽量使用 imap/ifilter 代替 map/filter

    ```python
    ##不推荐
    reduce(rf, filter(ff, map(mf, a_list)))
    
    ##推荐
    from itertools import ifilter, imap
    reduce(rf, ifilter(ff, imap(mf, a_list)))
    *lazy evaluation 会带来更高的内存使用效率，特别是当处理大数据操作的时候。
    ```

15. 使用 any/all 函数

    ```python
    ##不推荐
    found = False
    for item in a_list:
        if condition(item):
            found = True
            break
    if found:
        # do something if found...
    
    ##推荐
    if any(condition(item) for item in a_list):
        # do something if found...
    ```

16. 属性(property)

    ```python
    ##不推荐
    class Clock(object):
        def __init__(self):
            self.__hour = 1
        def setHour(self, hour):
            if 25 > hour > 0: self.__hour = hour
            else: raise BadHourException
        def getHour(self):
            return self.__hour
    
    ##推荐
    class Clock(object):
        def __init__(self):
            self.__hour = 1
        def __setHour(self, hour):
            if 25 > hour > 0: self.__hour = hour
            else: raise BadHourException
        def __getHour(self):
            return self.__hour
        hour = property(__getHour, __setHour)
    ```

17. 使用 with 处理文件打开

    ```python
    ##不推荐
    f = open("some_file.txt")
    try:
        data = f.read()
        # 其他文件操作..
    finally:
        f.close()
    
    ##推荐
    with open("some_file.txt") as f:
        data = f.read()
        # 其他文件操作...
    ```

18. 使用 with 忽视异常(仅限[Python](http://lovesoo.org/tag/python) 3)

    ```python
    ##不推荐
    try:
        os.remove("somefile.txt")
    except OSError:
        pass
    
    ##推荐
    from contextlib import ignored  # Python 3 only
    
    with ignored(OSError):
        os.remove("somefile.txt")
    ```

19. 使用 with 处理加锁

    ```python
    ##不推荐
    import threading
    lock = threading.Lock()
    
    lock.acquire()
    try:
        # 互斥操作...
    finally:
        lock.release()
    
    ##推荐
    import threading
    lock = threading.Lock()
    
    with lock:
        # 互斥操作...
    ```

## 参考

1. Idiomatic Python: <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>
2. PEP 8: Style Guide for Python Code: <http://www.python.org/dev/peps/pep-0008/>
3. 译文：<http://lovesoo.org/pythonic-python-programming.html>

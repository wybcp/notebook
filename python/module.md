# [The Module Search Path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)

1. built-in module
2. The directory containing the input script .
3. `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable PATH).
4. The installation-dependent default.
5. Python programs can modify `sys.path`. The directory containing the script being run is placed at the beginning of the search path

```python
sys.path.append("..")
import common_function.common_file as common_file
```

## `dir()`

显示 module 下面所有的方法

```python
import sys
dir(sys)
```

没有参数，则显示当前已定义的方法

返回一个列表，列出了一个对象所拥有的属性和方法。

## builtins

显示内置的方法和变量

```python
import builtins
dir(builtins)
```

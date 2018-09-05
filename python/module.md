https://docs.python.org/3/tutorial/modules.html#the-module-search-path

## The Module Search Path
1. built-in module
2. The directory containing the input script .
3. `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable PATH).
4. The installation-dependent default.
5. Python programs can modify `sys.path`. The directory containing the script being run is placed at the beginning of the search path
```
sys.path.append("..")
import common_function.common_file as common_file
```
## `dir()`
显示module下面所有的方法

```
import sys
dir(sys)
```
没有参数，则显示当前已定义的方法
### builtins
显示内置的方法和变量

```
import builtins
dir(builtins) 
```


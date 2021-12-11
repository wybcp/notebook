# pathlib

编程的一个小麻烦之一是：Microsoft Windows 在文件夹名称之间使用反斜杠字符，而几乎所有其他计算机都使用正斜杠：

    Windows filenames:
    C:\some_folder\some_file.txt
    
    Most other operating systems:
    /some_folder/some_file.txt

这是一个意外--[1980 年早期的计算机历史记录](https://blogs.msdn.microsoft.com/larryosterman/2005/06/24/why-is-the-dos-path-character/)。MS-DOS 的第一个版本使用正斜杠字符来指定命令行选项。当 Microsoft 在 MS-DOS 2.0 中添加对文件夹的支持时，正斜杠字符已被采用，因此它们使用反斜杠。三十五年后，我们仍然陷于这种不相容的窘境。

如果你希望你的 Python 代码可以在 Windows 和 Mac / Linux 上工作，你需要处理这些特定于平台的问题。幸运的是，Python 3 有一个名为`pathlib`的新模块，它能很愉悦地处理文件兼容问题。

让我们快速浏览一下处理文件名路径的不同方法，就会发现`pathlib`如何让你的生活更美好！

## 错误的解决方案：手动建立文件路径

假设您有一个数据文件夹，其中包含 Python 程序,并想用程序打开的文件夹：
![cd](https://cdn-images-1.medium.com/max/800/1*T2o_EXaDbMEj0C2djNXEFw.png)
在 Python 中，这样编码是错误方式：

```python
data_folder = "source_data/text_files/"
file_to_open = data_folder + "raw_data.txt"
f = open(file_to_open)
print(f.read())
```

请注意，我在 Mac 上使用 Unix 风格的正斜杠对路径进行了硬编码。这会让 Windows 用户很生气。

技术上讲，该代码在 Windows 上仍将工作，因为 Python 有一个黑技术，当在 Windows 上使用`open()`函数，无论是哪种斜线的 Python 都会识别。但即使如此，你也不应该依赖这一点。如果在错误的操作系统上使用错误类型的斜线，并不是所有的 Python 库都可以正常工作—— 特别是当它们与外部程序或库连接时。

而 Python 对混合斜线类型的支持是仅适用于 Windows 操作系统的黑技术，在其他操作系统它不能正常工作。在 Mac 中使用反斜杠，代码中的将会报错。

出于这些原因，使用硬编码路径字符串编写代码会使其他程序员傻瓜一样看你。一般来说，你应该尽量避免它。

## 旧解决方案：Python 的 os.path 模块

Python 的 os.path 模块有很多工具用于解决这些特定于操作系统的文件系统问题。

您可以使用 os.path.join（）为当前操作系统使用正确类型的斜杠构建路径：

```python
import os.path
data_folder = os.path.join("source_data", "text_files")
file_to_open = os.path.join(data_folder, "raw_data.txt")
f = open(file_to_open)
print(f.read())
```

这段代码可以在 Windows 或 Mac 上完美工作。问题是这是一个痛苦的使用。写出`os.path.join()`并将路径的每个部分作为一个单独的字符串传递是很罗嗦的，也是不直观的。

由于 os.path 模块中的大部分函数都是类似的恼人的使用，开发人员通常会忘记使用它们，即使他们知道使用这些会更好。这导致了很多跨平台的 bug 和愤怒的用户。

## 更好的解决方案：Python 3 的 pathlib

Python 3.4 引入了一个新的标准库，用于处理文件和路径称为 pathlib 的。 这真是太棒了！

要使用它，只需使用正斜杠将路径或文件名传递到新的`Path()`对象中，然后`Path()`会处理剩下的部分：

```python
from pathlib import Path
data_folder = Path("source_data/text_files/")
file_to_open = data_folder / "raw_data.txt"
with open(file_to_open,mode='r') as f:
    print(f.read())
# 或者使用pathlib自有的open
with file_to_open.open('r') as f:
    print(f.read())
```

这里需要注意两点：

- 你应该在 pathlib 函数中使用正斜杠。`Path()`对象为当前的操作系统将正斜杠转换成正确的斜线。
- 如果要添加到路径中，可以直接在代码中使用`/`运算符。

例如，我们可以读取文本文件的内容，而不必打开和关闭文件：

```python
from pathlib import Path
data_folder = Path("source_data/text_files/")
file_to_open = data_folder / "raw_data.txt"
print(file_to_open.read_text())
```

pathlib 还提供几种文件的读写方式：可以不用再使用 with open 的形式即可以进行读写。

> .read_text(): 找到对应的路径然后打开文件，读成str格式。等同open操作文件的"r"格式。
> .read_bytes(): 读取字节流的方式。等同open操作文件的"rb"格式。
> .write_text(): 文件的写的操作，等同open操作文件的"w"格式。
> .write_bytes(): 文件的写的操作，等同open操作文件的"wb"格式。		

实际上，pathlib 使得大多数标准的文件操作变得简单快捷：

```python
from pathlib import Path

filename = Path("source_data/text_files/raw_data.txt")
print(filename.name)
# prints "raw_data.txt"
print(filename.suffix)
# prints "txt"
print(filename.stem)
# prints "raw_data"
print(filename.anchor)
# print 类似盘符的一个东西/
print(filename.parent)
# print 上级目录
if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
```

你甚至可以使用 pathlib 将 Unix 路径显式转换成 Windows 格式的路径：

```python
from pathlib import Path, PureWindowsPath
filename = Path("source_data/text_files/raw_data.txt")
# Convert path to Windows format
path_on_windows = PureWindowsPath(filename)
print(path_on_windows)
# prints "source_data\text_files\raw_data.txt"
```

如果你真的想安全地在你的代码中使用反斜杠，你可以声明你的路径为 Windows 格式，并且 pathlib 可以为当前操作系统将它转换正确的格式：

```python
from pathlib import Path, PureWindowsPath
# I've explicitly declared my path as being in Windows format, so I can use forward slashes in it.
filename = PureWindowsPath("source_data\\text_files\\raw_data.txt")
# Convert path to the right format for the current operating system
correct_path = Path(filename)
print(correct_path)
# prints "source_data/text_files/raw_data.txt" on Mac and Linux
# prints "source_data\text_files\raw_data.txt" on Windows
```

如果你想要的话，你甚至可以使用 pathlib 来完成解析相关文件路径，解析网络共享路径以及生成`file：//` urls。下面是一个例子，它用两行代码,使你在 Web 浏览器中打开一个本地文件：

```python
from pathlib import Path
import webbrowser
filename = Path("source_data/text_files/raw_data.txt")
webbrowser.open(filename.absolute().as_uri())
```

这只是 pathlib 的一个小高峰。它可以替代许多不同的文件相关的功能，这些功能曾经分散在不同的 Python 模块中。

```python
from pathlib import Path

now_path = Path.cwd()
home_path = Path.home()

print("当前工作目录",now_path,type(now_path))
print("home目录",home_path,type(home_path))
```

### **移动和删除文件**

当然 pathlib 还可以支持文件其他操作，像移动，更新，甚至删除文件，但是使用这些方法的时候要小心因为，使用过程不用有任何的错误提示即使文件不存在也不会出现等待的情况。 使用 replace 方法可以移动文件，如果文件存在则会覆盖。为避免文件可能被覆盖，最简单的方法是在替换之前测试目标是否存在。

```python
import pathlib

destination = pathlib.Path.cwd() / "target" 
source = pathlib.Path.cwd() / "demo.txt"
if not destination.exists():
    source.replace(destination)
```

但是上面的方法存在问题就是，在多个进程多 destination 进行的操作的时候就会现问题，可以使用下面的方法避免这个问题。也就是说上面的方法适合单个文件的操作。

```python
import pathlib

destination = pathlib.Path.cwd() / "target" 
source = pathlib.Path.cwd() / "demo.txt"
with destination.open(mode='xb') as fid: 
    #xb表示文件不存在才操作
    fid.write(source.read_bytes())
```

当 destination 文件存在的时候上面的代码就会出现 FileExistsError 异常。 从技术上讲，这会复制一个文件。 要执行移动，只需在复制完成后删除源即可。 使用 with_name 和 with.shuffix 可以修改文件名字或者后缀。

```python
import pathlib
source = pathlib.Path.cwd() / "demo.py"
source.replace(source.with_suffix(".txt")) #修改后缀并移动文件，即重命名
```

可以使用 .rmdir () 和 .unlink () 来删除文件。

```python
import pathlib

destination = pathlib.Path.cwd() / "target" 
source = pathlib.Path.cwd() / "demo.txt"
source.unlink()
```

### **统计文件个数**

我们可以使用.iterdir 方法获取当前文件下的所以文件.

```
import pathlib
from collections import Counter
now_path = pathlib.Path.cwd()
gen = (i.suffix for i in now_path.iterdir())
print(Counter(gen))
```

输出内容

```
Counter({'.py': 16, '': 11, '.txt': 1, '.png': 1, '.csv': 1})
```

通过配合使用 collections 模块的 Counter 方法，我们获取了当文件夹下文件类型情况。 前面我们说过 glob 模块点这里了解【[https://www.cnblogs.com/c-x-a/p/9261832.html](https://link.zhihu.com/?target=https%3A//www.cnblogs.com/c-x-a/p/9261832.html)】，同样的 pathlib 也有 glob 方法和 rglob 方法，不同的是 glob 模块里的 glob 方法结果是列表形式的，iglob 是生成器类型，在这里 pathlib 的 glob 模块返回的是生成器类型，然后 pathlib 还有一个支持递归操作的 rglob 方法。 下面的这个操作我通过使用 glob 方法，设定规则进行文件的匹配。

```
import pathlib
from  collections import Counter
gen =(p.suffix for p in pathlib.Path.cwd().glob('*.py'))
print(Counter(gen))
```

### **展示目录树**

下一个示例定义了一个函数 tree ()，该函数的作用是打印一个表示文件层次结构的可视树，该树以一个给定目录为根。因为想列出其子目录，所以我们要使用 .rglob () 方法：

```
import pathlib
from  collections import Counter
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

now_path = pathlib.Path.cwd()

if __name__ == '__main__':
    tree(now_path)
```

其中 relative_to 的方法的作用是返回 path 相对于 directory 的路径。 parts 方法可以返回路径的各部分。例如

```
import pathlib
now_path = pathlib.Path.cwd()
if __name__ == '__main__':
    print(now_path.parts)
```

返回

```
('/', 'Users', 'chennan', 'pythonproject', 'demo')
```

### **获取文件最后一次修改时间**

iterdir (),.glob () 和.rglob () 方法非常适合于生成器表达式和列表理解。 使用 stat () 方法可以获取文件的一些基本信息，使用.stat ().st_mtime 可以获取文件最后一次修改的信息

```python
import pathlib
now_path = pathlib.Path.cwd()
from datetime import datetime
time, file_path = max((f.stat().st_mtime, f) for f in now_path.iterdir())
print(datetime.fromtimestamp(time), file_path)
```

甚至可以使用类似的表达式获取上次修改的文件内容

```python
import pathlib
from datetime import datetime
now_path =pathlib.Path.cwd()
result = max((f.stat().st_mtime, f) for f in now_path.iterdir())[1]
print(result.read_text())
```

.stat ().st_mtime 会返回文件的时间戳，可以使用 datetime 或者 time 模块对时间格式进行进一步转换。

### **其他内容**

## 常用方法

- `Path.resolve(strict=False)`:返回绝对路径的路径对象
- [`Path.glob(pattern)`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob)返回匹配文件的相对路径`Path('.').glob('*.py')`，当使用`**`模式意味着递归当前目录及子目录`Path('.').glob('**/*.py')`,和一个专门的方法`Path.rglob(pattern)`一样的效果

查看更多关于[pathlib](https://docs.python.org/3/library/pathlib.html)的使用

原作者：[Adam Geitgey](https://medium.com/@ageitgey)

原文：[Python 3 Quick Tip: The easy way to deal with file paths on Windows, Mac and Linux](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f)

# logging

[一看就懂，Python 日志 logging 模块详解及应用 | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/6921.html)

[Python 中 logging 模块的基本用法 | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/6080.html)

logging 提供了一组便利的日志函数，它们分别是：debug ()、 info ()、 warning ()、 error () 和 critical ()。

logging 函数根据它们用来跟踪的事件的级别或严重程度来命名。标准级别及其适用性描述如下（以严重程度递增排序）：每个级别对应的数字值为 CRITICAL：50，ERROR：40，WARNING：30，INFO：20，DEBUG：10，NOTSET：0。 Python 中日志的默认等级是 WARNING，DEBUG 和 INFO 级别的日志将不会得到显示，在 logging 中更改设置（ basicConfig 中设定 level 参数的级别即可）。

```python
import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

当 Python 记录一个事件的日志时，它会创建一个 LogRecord 对象，保存关于该事件的信息。

打印日志信息时，使用 logging.debug() 函数。

[Logging Cookbook](https://docs.python.org/3.6/howto/logging-cookbook.html)

 ## basicConfig 的参数



- filename：即日志输出的文件名，如果指定了这个信息之后，实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了。
- filemode：这个是指定日志文件的写入方式，有两种形式，一种是 w，一种是 a，分别代表清除后写入和追加写入。
- format：指定日志信息的输出格式，即上文示例所示的参数，详细参数-[logging --- Python 的日志记录工具 — Python 3.10.0 文档](https://docs.python.org/zh-cn/3/library/logging.html#logrecord-attributes)，部分参数如下所示：
  - %(levelno) s：打印日志级别的数值。
  - %(levelname) s：打印日志级别的名称。
  - %(pathname) s：打印当前执行程序的路径，其实就是 sys.argv [0]。
  - %(filename) s：打印当前执行程序名。
  - %(funcName) s：打印日志的当前函数。
  - %(lineno) d：打印日志的当前行号。
  - %(asctime) s：打印日志的时间。
  - %(thread) d：打印线程 ID。
  - %(threadName) s：打印线程名称。
  - %(process) d：打印进程 ID。
  - %(processName) s：打印线程名称。
  - %(module) s：打印模块名称。
  - %(message) s：打印日志信息。
- datefmt：指定时间的输出格式。
- style：如果 format 参数指定了，这个参数就可以指定格式化时的占位符风格，如 %、{、$ 等。
- level：指定日志输出的类别，程序会输出大于等于此级别的信息。
- stream：在没有指定 filename 的时候会默认使用 StreamHandler，这时 stream 可以指定初始化的文件流。
- handlers：可以指定日志处理时所使用的 Handlers，必须是可迭代的。

## 日志分类

日志级别指的是 Debug、Info、WARNING、ERROR 以及 CRITICAL 等严重等级进行划分。

## [Python 中更优雅的日志记录方案 loguru | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/7776.html)

loguru，可以将 log 的配置和使用更加简单和方便。
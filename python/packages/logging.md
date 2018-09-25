# logging

```python
import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

当 Python 记录一个事件的日志时，它会创建一个 LogRecord 对象，保存关于该事件的信息。

打印日志信息时，使用 logging.debug() 函数。

[Logging Cookbook](https://docs.python.org/3.6/howto/logging-cookbook.html)
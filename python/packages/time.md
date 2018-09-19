# 时间相关包

## time

- time.time()：取得 Unix 纪元时间戳，
- time.sleep()

## datetime

Unix 纪元时间戳可以通过 datetime.datetime.fromtimestamp()，转换为 datetime 对象。
`datetime.datetime.fromtimestamp(time.time())`

timedelta 数据类型，表示一段时间。datetime.timedelta()函数接受关键字参数 weeks、days、hours、minutes、seconds、milliseconds 和 microseconds。 没有 month 和 year 关键字参数，因为“月”和“年”是可变的时间，依赖于特定月份或年份。

strftime()方 法，可以将 datetime 对象显示为字符串。

datetime.datetime.strftime()，将字符串转换成 datetime 对象。

## [python-dateutil](https://pypi.org/project/python-dateutil/)

处理时区，模糊时间范围，节假日计算

## 查找星期中某一天最后出现的日期

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 最后的周五
Desc :
"""
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_by_day(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    # 获取日期的星期索引
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
```

大规模日期计算：

```bash
>>> from datetime import datetime
>>> from dateutil.relativedelta import relativedelta
>>> from dateutil.rrule import *
>>> d = datetime.now()
>>> print(d)
2018-09-18 09:59:14.467000

>>> # Next Friday
>>> print(d + relativedelta(weekday=FR))
2018-09-21 09:59:14.467000
>>> # Last Friday
>>> print(d + relativedelta(weekday=FR(-1)))
2018-09-14 09:59:14.467000
```

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
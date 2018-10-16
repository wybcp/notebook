# [数据类型](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

## [数字类型](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html)

### 整数

| Type        | Storage (Bytes) | Minimum Value Signed | Minimum Value Unsigned | Maximum Value Signed | Maximum Value Unsigned | 默认显示宽度（与有符号的最小值宽度相同） |
| ----------- | --------------- | -------------------- | ---------------------- | -------------------- | ---------------------- | ---------------------------------------- |
| `TINYINT`   | 1               | `-128`               | `0`                    | `127`                | `255`                  | 4                                        |
| `SMALLINT`  | 2               | `-32768`             | `0`                    | `32767`              | `65535`                | 6                                        |
| `MEDIUMINT` | 3               | `-8388608`           | `0`                    | `8388607`            | `16777215`             | 9                                        |
| `INT`       | 4               | `-2147483648`        | `0`                    | `2147483647`         | `4294967295`           | 11                                       |
| `BIGINT`    | 8               | `-263`               | `0`                    | `263-1`              | `264-1`                | 20                                       |

负号占有一个显示位。

### 浮点数

| Type           | Storage (Bytes) | Minimum Value Signed     | Minimum Value Unsigned | Maximum Value Signed     |
| -------------- | --------------- | ------------------------ | ---------------------- | ------------------------ |
| FLOAT          | 4               | -3.402823466E+38         | 0                      | -1.175494351E-38         |
| DOUBLT         | 8               | -1.7976931348623157E+308 | `0`                    | -2.2250738585072014E-308 |
| DECIMAL（M,D） | M+2             |                          |                        |                          |

## [日期时间类型](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html)

|                              Data Type                               |      “Zero” Value       |        格式         |                      范围                       | Storage (Bytes) |
| :------------------------------------------------------------------: | :---------------------: | :-----------------: | :---------------------------------------------: | --------------- |
|   [`DATE`](https://dev.mysql.com/doc/refman/8.0/en/datetime.html)    |     `'0000-00-00'`      |     YYYY-MM-DD      |              1000-01-01~9999-12-3               | 3               |
|     [`TIME`](https://dev.mysql.com/doc/refman/8.0/en/time.html)      |      `'00:00:00'`       |      HH:MM:SS       |              -838:59:59~838:59:59               | 3               |
| [`DATETIME`](https://dev.mysql.com/doc/refman/8.0/en/datetime.html)  | `'0000-00-00 00:00:00'` | YYYY-MM-DD HH:MM:SS |     1000-01-01 00:00:00~9999-12-3 23:59:59      | 8               |
| [`TIMESTAMP`](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) | `'0000-00-00 00:00:00'` | YYYY-MM-DD HH:MM:SS | 1970-01-01 00:00:01 UTC~2038-01-19 03:14:07 UTC | 4               |
|     [`YEAR`](https://dev.mysql.com/doc/refman/8.0/en/year.html)      |         `0000`          |        YYYY         |                    1901~2155                    | 1               |

## 字符串

文本字符串和二进制字符串

## **字符串类型**

| 字符串类型   | 字节数    | 描述                                                          | 规则                                                             |
| ------------ | --------- | ------------------------------------------------------------- | ---------------------------------------------------------------- |
| char(m)      | m         | m 为 0 ~ 255 之间的整数                                       | 固定长度，右侧填充空格以达到指定长度                             |
| varchar(m)   | 值长度+1  | m 为 0~65535 之间的整数                                       |                                                                  |
| tinytext     | 值长度+1  | 允许长度 0~255 字节                                           |                                                                  |
| text         | 值长度+2  | 允许长度 0~65535 字节                                         |                                                                  |
| mediumtext   | 值长度+3  | 允许长度 0~167772150 字节                                     |                                                                  |
| longtext     | 值长度+4  | 允许长度 0~4294967295 字节                                    |                                                                  |
| bit(m)       | (m+7)/8   | 1~64                                                          | m 默认为 1，左边用 0 填充                                        |
| binary(m)    | m         | 允许 0~m 个字节定长的字符串                                   |                                                                  |
| varbinary(m) | 值长度+1  | 允许 0~m 个字节变长的字符串                                   |                                                                  |
| tinyblob     | 值长度+1  | 允许长度 0~255 字节                                           |                                                                  |
| blob         | 值长度+2  | 允许长度 0~65535 字节                                         |                                                                  |
| mediumblob   | 值长度+3  | 允许长度 0~167772150 字节                                     |                                                                  |
| longblob     | 值长度+4  | 允许长度 0~4294967295 字节                                    |                                                                  |
| enum         | 1 或 2    | 1~255 个成员需要 1 个字节；255~65535 个成员，2 个字节         | 索引值从 1 开始,`select enum_colunm+0 from table_name`查看索引值 |
| set          | 1/2/3/4/8 | 类似 enum,set 一次可以选取多个成员(最多 64)，而 enum 只能一个 | 固定设置的值得顺序，插入的值自动调整为该顺序。                   |
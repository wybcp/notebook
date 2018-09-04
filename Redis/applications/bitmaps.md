# 位图

位图不是特殊的数据结构，它的内容其实就是普通的字符串，也就是 byte 数组。我们可以使用普通的 get/set 直接获取和设置整个位图的内容，也可以使用位图操作 getbit/setbit 等将 byte 数组看成「位数组」来处理。

## 基本使用

Redis 的位数组是自动扩展，如果设置了某个偏移位置超出了现有的内容范围，就会自动将位数组进行零扩充。

### setbit

「零存」就是使用 setbit 对位值进行逐个设置，
使用位操作将字符串设置为 hello (不是直接使用 set 指令)，首先我们需要得到 hello 的 ASCII 码，用 Python 命令行可以很方便地得到每个字符的 ASCII 码的二进制值。

```bash
>>> bin(ord('h'))
'0b1101000'   # 高位 -> 低位
```

「零存」就是使用 setbit 对位值进行逐个设置，

redis 设置值为 1 的位:

```bash
127.0.0.1:6379[8]> setbit s 1 1
(integer) 0
127.0.0.1:6379[8]> setbit s 2 1
(integer) 0
127.0.0.1:6379[8]> setbit s 4 1
(integer) 0
127.0.0.1:6379[8]> get s
"h"
127.0.0.1:6379[8]> getbit s 3
(integer) 0
```

### set

「整存」就是使用字符串一次性填充所有位数组，覆盖掉旧值。

```bash
127.0.0.1:6379[8]> set w h
OK
127.0.0.1:6379[8]> getbit w 1
(integer) 1
127.0.0.1:6379[8]> getbit w 0
(integer) 0
```

## 统计和查找

Redis 提供了位图统计指令 bitcount 和位图查找指令 bitpos，bitcount 用来统计指定位置范围内 1 的个数，bitpos 用来查找指定范围内出现的第一个 0 或 1。

### 魔术指令 [bitfield](https://redis.io/commands/bitfield)

bitfield 有三个子指令，分别是 get/set/incrby，它们都可以对指定位片段进行读写，但是最多只能处理 64 个连续的位，如果超过 64 位，就得使用多个子指令，bitfield 可以一次执行多个子指令。

`BITFIELD key [GET type offset] [SET type offset value] [INCRBY type offset increment] [OVERFLOW WRAP|SAT|FAIL]`

例子:

```bash
127.0.0.1:6379[8]> set w hello
OK
127.0.0.1:6379[8]> bitfield w get u4 0 # 从第一个位开始取 4 个位，结果是无符号数 (u)
1) (integer) 6
127.0.0.1:6379[8]> bitfield w get i4 1 # 从第二个位开始取 4 个位，结果是有符号数 (i)
```

一次执行多个子指令:

```bash
127.0.0.1:6379[8]> bitfield w get u4 0 get u3 2 get i4 0 get i3 2
1) (integer) 6
2) (integer) 5
3) (integer) 6
4) (integer) -3
```

## 记录大量数据的布尔值

bitmaps 最大的优势是在存储数据时可以极大的节省空间，比如在一个项目中采用自增长的 id 来标识用户，就可以仅用 512M 的内存来记录 4 亿用户的信息（比如用户是否希望收到新的通知，用 1 和 0 标识）。

## 参考

- [节衣缩食--位图](https://juejin.im/book/5afc2e5f6fb9a07a9b362527/section/5b330620e51d4558e03ce7f8)

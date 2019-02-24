# 二进制日志

## 什么是 Binlog

binlog 是 Mysql sever 层维护的一种二进制日志，其主要是用来记录对 mysql 数据和结构更新或潜在发生更新的 SQL 语句，并以"事务"的形式保存在磁盘中。

作用主要有：

- 主从复制：MySQL Replication 在 Master 端开启 binlog，Master 把它的二进制日志传递给 slaves 并回放来达到 master-slave 数据一致的目的
- 数据恢复：通过 mysqlbinlog 工具恢复数据
- 增量备份

## 启用 Binlog

通常情况 MySQL 是默认关闭 Binlog 的，所以你得配置一下以启用它。

启用的过程就是修改配置文件 `my.cnf` 了。

紧接着配置 `log-bin` 和 `log-bin-index` 的值，如果没有则自行加上去。

```conf
log-bin=master-bin
log-bin-index=master-bin.index
expire_logs_days=10
max_binlog_size=100M
```

- `log-bin` 是指以后生成各 Binlog 文件的前缀，比如上述使用`master-bin`，那么文件就将会是`master-bin.000001`
- `log-bin-index` 则指 binlog index 文件的名称，这里我们设置为`master-bin.index`。默认使用主机名命名。
- `expire_logs_days`清除过期日志的时间
- `max_binlog_size`单个文件大小限制，4096B~1GB，默认 1G

做完之后重启 MySQL 服务，验证一下：

```sql
SHOW VARIABLES LIKE '%log_bin%';
```

如果结果里面出来这样类似的话就表示成功了：

```sh
+---------------------------------+---------------------------------------+
| Variable_name                   | Value                                 |
+---------------------------------+---------------------------------------+
| log_bin                         | ON                                    |
| log_bin_basename                | /usr/local/var/mysql/master-bin       |
| log_bin_index                   | /usr/local/var/mysql/master-bin.index |
| log_bin_trust_function_creators | OFF                                   |
| log_bin_use_v1_row_events       | OFF                                   |
| sql_log_bin                     | ON                                    |
+---------------------------------+---------------------------------------+
```

可以参考这篇《[MySQL 的 binary log 初探](http://blog.csdn.net/jolly10/article/details/13998761)》。

## 查看

查看 binary log 文件个数和文件名 `mysql>show binary logs;`

查看二进制日志`mysqlbinlog log-file`

## 删除

除了配置自动删除 binlog 文件外，可以使用`msyql>reset master;`删除所有二进制文件，`purge master logs`删除指定文件。

## 结构解析

### 索引文件

索引文件就是上文中的 `master-bin.index` 文件，是一个普通的文本文件，以换行为间隔，一行一个文件名。比如它可能是：

    master-bin.000001
    master-bin.000002
    master-bin.000003

然后对应的每行文件就是一个 Binlog 实体文件了。

### Binlog 文件

Binlog 的文件结构大致由如下几个方面组成。

#### 文件头

文件头由一个四字节 Magic Number，其值为`1852400382`，在内存中就是`"\xfe\x62\x69\x6e"`，参考 MySQL 源码的 [log_event.h](https://xcoder.in/2015/08/10/mysql-binlog-try/://github.com/mysql/mysql-server/blob/a2757a60a7527407d08115e44e889a25f22c96c6/sql/log_event.h#L187)，也就是`'\0xfe' 'b' 'i' 'n'`。

与平常二进制一样，通常都有一个 Magic Number 进行文件识别，如果 Magic Number 不吻合上述的值那么这个文件就不是一个正常的 Binlog。

#### 事件

在文件头之后，跟随的是一个一个事件依次排列。每个事件都由一个事件头和事件体组成。

事件头里面的内容包含了这个事件的类型（如新增、删除等）、事件执行时间以及是哪个服务器执行的事件等信息。

第一个事件是一个事件描述符，描述了这个 Binlog 文件格式的版本。接下去的一堆事件将会按照第一个事件描述符所描述的结构版本进行解读。最后一个事件是一个衔接事件，指定了下一个 Binlog 文件名——有点类似于链表里面的 `next` 指针。

根据《[High-Level Binary Log Structure and Contents](https://xcoder.in/2015/08/10/mysql-binlog-try/High-Level%20Binary%20Log%20Structure%20and%20Contents)》所述，不同版本的 Binlog 格式不一定一样，所以也没有一个定性。在我写这篇文章的时候，目前有三种版本的格式。

- v1，用于 MySQL 3.2.3
- v3，用于 MySQL 4.0.2 以及 4.1.0
- v4，用于 MySQL 5.0 以及更高版本

实际上还有一个 v2 版本，不过只在早期 4.0.x 的 MySQL 版本中使用过，但是 v2 已经过于陈旧并且不再被 MySQL 官方支持了。

> **通常我们现在用的 MySQL 都是在 5.0 以上的了，所以就略过 v1 ~ v3 版本的 Binlog，如果需要了解 v1 ~ v3 版本的 Binlog 可以自行前往上述的《High-level…》文章查看。**

##### 事件头

一个事件头有 19 字节，依次排列为四字节的时间戳、一字节的当前事件类型、四字节的服务端 ID、四字节的当前事件长度描述、四字节的下个事件位置（方便跳转）以及两字节的标识。

用 ASCII Diagram 表示如下：

    +---------+---------+---------+------------+-------------+-------+
    |timestamp|type code|server_id|event_length|next_position|flags  |
    |4 bytes  |1 byte   |4 bytes  |4 bytes     |4 bytes      |2 bytes|
    +---------+---------+---------+------------+-------------+-------+

也可以字节编造一个结构体来解读这个头：

```c
struct BinlogEventHeader
{
    int   timestamp;
    char  type_code;
    int   server_id;
    int   event_length;
    int   next_position;
    char  flags[2];
};
```

> 如果你要直接用这个结构体来读取数据的话，需要加点手脚。
>
> 因为默认情况下 GCC 或者 G++ 编译器会对结构体进行字节对齐，这样读进来的数据就不对了，因为 Binlog 并不是对齐的。为了统一我们需要取消这个结构体的字节对齐，一个方法是使用`#pragma pack(n)`，一个方法是使用`__attribute__((__packed__))`，还有一种情况是在编译器编译的时候强制把所有的结构体对其取消，即在编译的时候使用 `fpack-struct` 参数，如：

```sh
g++ temp.cpp -o a -fpack-struct=1
```

根据上述的结构我们可以明确得到各变量在结构体里面的偏移量，所以在 MySQL 源码里面（[libbinlogevents/include/binlog_event.h](https://github.com/mysql/mysql-server/blob/5.7/libbinlogevents/include/binlog_event.h#L353)）有下面几个常量以快速标记偏移：

```c
#define EVENT_TYPE_OFFSET    4
#define SERVER_ID_OFFSET     5
#define EVENT_LEN_OFFSET     9
#define LOG_POS_OFFSET       13
#define FLAGS_OFFSET         17
```

而具体有哪些事件则在 [libbinlogevents/include/binlog_event.h#L245](https://github.com/mysql/mysql-server/blob/5.7/libbinlogevents/include/binlog_event.h#L245) 里面被定义。如有个 `FORMAT_DESCRIPTION_EVENT` 事件的 `type_code` 是 15、`UPDATE_ROWS_EVENT` 的 `type_code` 是 31。

还有那个`next_position`，在 v4 版本中代表从 Binlog 一开始到下一个事件开始的偏移量，比如到第一个事件的 `next_position` 就是 4，因为文件头有一个字节的长度。然后接下去对于事件 n 和事件 n + 1 来说，他们有这样的关系：

> next_position(n + 1) = next_position(n) + event_length(n)

关于 flags 暂时不需要了解太多，如果真的想了解的话可以看看 MySQL 的[相关官方文档](http://dev.mysql.com/doc/internals/en/event-flags.html)。

##### 事件体

事实上在 Binlog 事件中应该是有三个部分组成，`header`、`post-header` 和`payload`，不过通常情况下我们把 `post-header` 和 `payload` 都归结为事件体，实际上这个 `post-header` 里面放的是一些定长的数据，只不过有时候我们不需要特别地关心。想要深入了解可以去查看 MySQL 的官方文档。

所以实际上一个真正的事件体由两部分组成，用 ASCII Diagram 表示就像这样：

    +=====================================+
    | event  | fixed part (post-header)   |
    | data   +----------------------------+
    |        | variable part (payload)    |
    +=====================================+

而这个 `post-header` 对于不同类型的事件来说长度是不一样的，同种类型来说是一样的，而这个长度的预先规定将会在一个“格式描述事件”中定好。

##### 跳转事件

跳转事件即`ROTATE_EVENT`，其 `type_code` 是 4，其 `post-header` 长度为 8。

当一个 Binlog 文件大小已经差不多要分割了，它就会在末尾被写入一个 `ROTATE_EVENT`——用于指出这个 Binlog 的下一个文件。

它的 `post-header` 是 8 字节的一个东西，内容通常就是一个整数`4`，用于表示下一个 Binlog 文件中的第一个事件起始偏移量。我们从上文就能得出在一般情况下这个数字只可能是四，就偏移了一个魔法数字。当然我们讲的是在 v4 这个 Binlog 版本下的情况。

然后在 `payload` 位置是一个字符串，即下一个 Binlog 文件的文件名。

##### 各种不同的事件体

由于篇幅原因这里就不详细举例其它普通的不同事件体了，具体的详解在 [MySQL 文档](http://dev.mysql.com/doc/internals/en/event-data-for-specific-event-types.html)中一样有介绍，用到什么类型的事件体就可以自己去查询。

## 参考

[初探 MySQL 的 Binlog](https://xcoder.in/2015/08/10/mysql-binlog-try/)

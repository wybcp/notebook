# 内存

高效利用 Redis 内存首先理解 Redis 内存消耗，如何管理内存，如何优化内存。

## 内存消耗

```shell
info memory
```

查看内存相关指标。

```shell
# redis分配器分配的内存总量
used_memory:2101184
used_memory_human:2.00M
# 从操作系统角度显示redis进程占用的物理内存总和
used_memory_rss:839680
used_memory_rss_human:820.00K
# 内存使用的最大值
used_memory_peak:2947808
used_memory_peak_human:2.81M
used_memory_peak_perc:71.28%
used_memory_overhead:1065594
used_memory_startup:980736
used_memory_dataset:1035590
used_memory_dataset_perc:92.43%
total_system_memory:17179869184
total_system_memory_human:16.00G

used_memory_lua:36864
used_memory_lua_human:36.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
# used_memory_rss/used_memory比值，表示内存碎片率
mem_fragmentation_ratio:0.40
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0
```

理想情况是 mem_fragmentation_ratio 略微大于 1。

- mem_fragmentation_ratio>1，说明有部分内存没有用于存储数据，而被内存碎片化消耗
- mem_fragmentation_ratio<1，操作系统将一部分 redis 内存交换到硬盘，可能导致性能变差

### 进程内消耗

#### 自身内存

redis 空进程自身消耗很小，used_memory_rss 3m 左右，used_memory 800k 左右。

#### 对象内存

sizeof(keys)+sizeof(values)

避免使用过长的键（字符串）。

#### 缓存内存

- 客户端缓存，所有连接到 redis 服务器 TCP 连接的输入输出缓存，输入缓存无法控制，最大为 1，如果超时将断开连接。输出缓存参数`client-output-buffer-limit`。
- 复制积压缓冲区，
- AOF 缓冲区。

#### 内存碎片

原因：

- 频繁更新操作
- 大量过期键删除

处理方式：

- 数据对齐
- 安全重启

## 内存管理

### 设置内存上限 maxmemory

由于碎片，Redis 实际消耗内存比 maxmemory 大。

### 动态调整内存上限

```shell
config set maxmemory
```

### 内存回收策略

- 删除过期键对象
  - 惰性删除
  - 定期任务删除
- 内存溢出控制策略：`config set maxmemory-policy {policy}`
  - noeviction：默认策略
  - Volatile-lru：
  - allkeys-lru

## 优化内存

### redisobject 对象

Redis 存储的数据都是使用 Redisobject 来封装。

- type 字段：数据类型

- encoding 字段：编码类型

- lru 字段：记录对象最后一次被访问的时间。`object idletime {key}`可以在不更新 lru 字段的情况下查看当前键的空闲实现。

- refcount 字段：记录引用次数，`object refcount {key}`获取当前对象的引用次数

- \*ptr 字段：与数据内容相关，如果是整数，直接存储数据；否则表示指向数据的指针。

### 缩减键值对象

- key 长度：在完整描述业务的情况下，键越短越好
- value 长度：把业务对象序列化，选中合适的序列化工具；如果内存紧张，可以使用 snappy 压缩工具处理常见的 json 等通用格式数据。

### 共享对象池

Redis 内部有一个 0~9999 的整数对象池，尽量使用整数对象。

### 字符串优化

### [编码优化](../data-structure/Redis-encoding.md)

### 控制键的数量

hash 结构降低键数量。

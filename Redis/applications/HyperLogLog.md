# HyperLogLog 数据结构

Redis 的高级数据结构，提供不精确的去重计数方案，虽然不精确但是也不是非常不精确，标准误差是 0.81%。

HyperLogLog 提供了两个指令 pfadd 和 pfcount，一个是增加计数，一个是获取计数。

第三个指令 pfmerge，用于将多个 pf 计数值累加在一起形成一个新的 pf 值。

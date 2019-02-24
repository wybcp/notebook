# 集群

Redis 分布式解决方案 Redis Cluster。

## 数据分布

分布式数据库首先解决整个数据集按照分区规则映射到多个节点，重点在于数据分区规则。

Redis Cluster 采用虚拟槽分区，所有的键根据哈希函数映射到 0~16383 整数槽（slot），计算公式：`slot=CRC16(key)&16383`，每个节点负责维护一部分槽以及槽所映射的键值数据。

## 集群功能限制

很多情况下只支持具有相同 slot 值的 key 的操作。

- key 事务支持有限。
- key 批量操作支持有限。
- hash、list 只能保存到同意节点。
- 只能使用一个数据库空间 db 0。
- 复制结构只支持一层。

## 集群节点

实例的集群模式需要通过配置来开启， 开启集群模式的实例将可以使用集群特有的功能和命令。

集群配置文件示例：

```conf
port 7000
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
```

文件中的 `cluster-enabled` 选项用于开实例的集群模式， 而 `cluster-conf-file` 选项则设定了保存节点配置文件的路径， 默认值为 `nodes.conf` 。

节点配置文件无须人为修改， 它由 Redis 集群在启动时创建， 并在有需要时自动进行更新。

集群正常运作强烈建议使用六个节点： 其中三个为主节点， 而其余三个则是各个主节点的从节点。

首先， 让我们进入一个新目录， 并创建六个以端口号为名字的子目录， 稍后我们在将每个目录中运行一个 Redis 实例：

```shell
mkdir cluster-test
cd cluster-test
mkdir 7000 7001 7002 7003 7004 7005
```

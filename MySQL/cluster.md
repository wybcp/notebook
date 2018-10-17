# MySQL Group Replication 集群

- MySQL 5.7 引入了 Group Replication 功能，可以在一组 MySQL 服务器之间实现自动主机选举，形成一主多从结构。经过高级配置后，可以实现多主多从结构。
- MySQL Router 是一个轻量级透明中间件，可以自动获取上述集群的状态，规划 SQL 语句，分配到合理的 MySQL 后端进行执行。
- MySQL Shell 是一个同时支持 JavaScript 和 SQL 的交互程序，可以快速配置 InnoDB Cluster。

## 功能分类

- 管理节点：对 SQL 节点和数据节点进行管理配置。
- SQL 节点：对数据节点进行数据访问，并从数据节点返回数据结果。
- 数据节点

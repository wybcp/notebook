# MySQL Group Replication 集群

- MySQL 5.7 引入了 Group Replication 功能，可以在一组 MySQL 服务器之间实现自动主机选举，形成一主多从结构。经过高级配置后，可以实现多主多从结构。
- MySQL Router 是一个轻量级透明中间件，可以自动获取上述集群的状态，规划 SQL 语句，分配到合理的 MySQL 后端进行执行。
- MySQL Shell 是一个同时支持 JavaScript 和 SQL 的交互程序，可以快速配置 InnoDB Cluster。

MySQL 集群是一种在无共享架构（SNA，Share Nothing Architecture）系统里应用内存数据库集群的技术。这种无共享的架构可以使得系统使用低廉的硬件获取高的可扩展性。

MySQL 集群是一种分布式设计，目标是要达到没有任何单点故障点。因此，任何组成部分都应该拥有自己的内存和磁盘。任何共享存储方案如网络共享，网络文件系统和 SAN 设备是不推荐或不支持的。通过这种冗余设计，MySQL 声称数据的可用度可以达到 99.999%。

实际上，MySQL 集群是把一个叫做 NDB 的内存集群存储引擎集成与标准的 MySQL 服务器集成。它包含一组计算机，每个都跑一个或者多个进程，这可能包括一个 MySQL 服务器，一个数据节点，一个管理服务器和一个专有的一个数据访问程序。

## 功能分类

MySQL Cluster 由 3 个不同功能的服务构成，每个服务由一个专用的守护进程提供，一项服务也叫做一个节点。

- 管理节点（The management (MGM) node）：对 SQL 节点和数据节点进行管理配置，理论上一般只启动一个，而且宕机也不影响 cluster 的服务，这个进程只在 cluster 启动以及节点加入集群时起作用， 所以这个节点不是很需要冗余，理论上通过一台服务器提供服务就可以了。通过 ndb_mgmd 命令启动，使用 config.ini 配置文件。
- SQL 节点（The client (API) node）：对数据节点进行数据访问，并从数据节点返回数据结果。通过他实现 Cluster DB 的访问，这个节点也就是普通的 mysqld 进程， 需要在配置文件中配置 ndbcluster 指令打开 NDB Cluster storage engine 存储引擎，增加 API 节点会提高整个集群的并发访问速度和整体的吞吐量，该节点可以部署在 Web 应用服务器上，也可以部署在专用的服务器上，也开以和 DB 部署在同一台服务器上。通过 mysqld_safe 命令启动
- 数据节点（The storage or database (DB) node）：用来存储数据，可以和管理节点(MGM)、  用户端节点(API)处在不同的机器上，也可以在同一个机器上面，集群中至少要有一个 DB 节点，2 个以上时就能实现集群的高可用保证，DB 节点增加时，集群的处理速度会变慢。通过 ndbd 命令启动，第一次创建好 cluster DB 节点时，需要使用 –init 参数初始化。

这 3 类节点可以分布在不同的主机上，比如 DB 可以是多台专用的服务器，也可以每个 DB 都有一个 API，当然也可以把 API 分布在 Web 前端的服务器上去，通常来说， API 越多 cluster 的性能会越好。

## 存储引擎

MySQL Cluster 使用了一个专用的基于内存的存储引擎（NDB 引擎），这样做的好处是速度快， 没有磁盘 I/O 的瓶颈，但是由于是基于内存的，所以数据库的规模受系统总内存的限制，如果运行 NDB 的 MySQL 服务器一定要内存够大，比如 4G, 8G, 甚至 16G。NDB 引擎是分布式的，它可以配置在多台服务器上来实现数据的可靠性和扩展性，理论上 通过配置 2 台 NDB 的存储节点就能实现整个数据库集群的冗余性和解决单点故障问题。

该存储引擎有下列缺点：

1、基于内存，数据库的规模受集群总内存的大小限制

2、基于内存，断电后数据可能会有数据丢失，这点还需要通过测试验证。

3、多个节点通过网络实现通讯和数据同步、查询等操作，因此整体性受网络速度影响，

4、因此速度也比较慢

当然也有它的优点：

1、多个节点之间可以分布在不同的地理位置，因此也是一个实现分布式数据库的方案。

2、扩展性很好，增加节点即可实现数据库集群的扩展。

3、冗余性很好，多个节点上都有完整的数据库数据，因此任何一个节点宕机都不会造成服务中断。

4、实现高可用性的成本比较低，不象传统的高可用方案一样需要共享的存储设备和专用的软件才能实现，NDB 只要有足够的内存就能实现。
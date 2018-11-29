# [etcd](https://github.com/etcd-io/etcd)

Etcd 是 CoreOS 团队于 2013 年 6 月发起的开源项目，它的目标是构建一个高可用的分布式键值（key-value）仓库，遵循 Apache v2 许可，基于 Go 语言实现。

Etcd 专门为集群环境设计，采用了更为简洁的 Raft 共识算法㊟，同样可以实现数据强一致性，并支持集群节点状态管理和服务自动发现等。

## 安装

```bash
root@iZwz97tbgo9lk6rm6lxu2wZ:~# wget https://github.com/etcd-io/etcd/releases/download/v3.3.10/etcd-v3.3.10-linux-amd64.tar.gz
root@iZwz97tbgo9lk6rm6lxu2wZ:~# tar -zxvf etcd-v3.3.10-linux-amd64.tar.gz
root@iZwz97tbgo9lk6rm6lxu2wZ:~# cd etcd-v3.3.10-linux-amd64/
root@iZwz97tbgo9lk6rm6lxu2wZ:~/etcd-v3.3.10-linux-amd64# ls
Documentation  README-etcdctl.md  README.md  READMEv2-etcdctl.md  etcd  etcdctl
# etcd 是服务主文件，etcdctl 是提供给用户的命令客户端，其他都是文档文件。
# 将所需要的二进制文件都放到系统可执行路径/usr/local/bin/下
root@iZwz97tbgo9lk6rm6lxu2wZ:~/etcd-v3.3.10-linux-amd64#  cp etcd* /usr/local/bin/
```

### Docker 镜像方式下载

以 Etcd 3.3.10 为例，镜像名称为 quay.io/coreos/etcd：v3.3.10，可以通过下面的命令启动 etcd 服务监听到本地的 2379 和 2380 端口：

```bash
$ docker run \
 -p 2379:2379 \
 -p 2380:2380 \
 -v /etc/ssl/certs/:/etc/ssl/certs/
quay.io/coreos/etcd:v3.3.10
```

## 使用

启动一个服务节点，监听在本地的 2379（客户端请求端口）和 2380（其他节点连接端口）。

```bash
root@iZwz97tbgo9lk6rm6lxu2wZ:~/etcd-v3.3.10-linux-amd64# etcd
2018-10-29 15:13:33.648817 I | etcdmain: etcd Version: 3.3.10
2018-10-29 15:13:33.649041 I | etcdmain: Git SHA: 27fc7e2
2018-10-29 15:13:33.649125 I | etcdmain: Go Version: go1.10.4
2018-10-29 15:13:33.649214 I | etcdmain: Go OS/Arch: linux/amd64
2018-10-29 15:13:33.649314 I | etcdmain: setting maximum number of CPUs to 1, total number of available CPUs is 1
2018-10-29 15:13:33.649401 W | etcdmain: no data-dir provided, using default data-dir ./default.etcd
2018-10-29 15:13:33.649921 I | embed: listening for peers on http://localhost:2380
2018-10-29 15:13:33.650196 I | embed: listening for client requests on localhost:2379
2018-10-29 15:13:33.655074 I | etcdserver: name = default
2018-10-29 15:13:33.655157 I | etcdserver: data dir = default.etcd
2018-10-29 15:13:33.655188 I | etcdserver: member dir = default.etcd/member
2018-10-29 15:13:33.655285 I | etcdserver: heartbeat = 100ms
2018-10-29 15:13:33.655350 I | etcdserver: election = 1000ms
2018-10-29 15:13:33.655385 I | etcdserver: snapshot count = 100000
2018-10-29 15:13:33.655430 I | etcdserver: advertise client URLs = http://localhost:2379
2018-10-29 15:13:33.655485 I | etcdserver: initial advertise peer URLs = http://localhost:2380
2018-10-29 15:13:33.655536 I | etcdserver: initial cluster = default=http://localhost:2380
2018-10-29 15:13:33.660479 I | etcdserver: starting member 8e9e05c52164694d in cluster cdf818194e3a8c32
2018-10-29 15:13:33.660577 I | raft: 8e9e05c52164694d became follower at term 0
2018-10-29 15:13:33.660659 I | raft: newRaft 8e9e05c52164694d [peers: [], term: 0, commit: 0, applied: 0, lastindex: 0, lastterm: 0]
2018-10-29 15:13:33.660689 I | raft: 8e9e05c52164694d became follower at term 1
2018-10-29 15:13:33.689866 W | auth: simple token is not cryptographically signed
2018-10-29 15:13:33.694223 I | etcdserver: starting server... [version: 3.3.10, cluster version: to_be_decided]
2018-10-29 15:13:33.696998 I | etcdserver: 8e9e05c52164694d as single-node; fast-forwarding 9 ticks (election ticks 10)
2018-10-29 15:13:33.697546 I | etcdserver/membership: added member 8e9e05c52164694d [http://localhost:2380] to cluster cdf818194e3a8c32
2018-10-29 15:13:34.161047 I | raft: 8e9e05c52164694d is starting a new election at term 1
2018-10-29 15:13:34.161213 I | raft: 8e9e05c52164694d became candidate at term 2
2018-10-29 15:13:34.161323 I | raft: 8e9e05c52164694d received MsgVoteResp from 8e9e05c52164694d at term 2
2018-10-29 15:13:34.161413 I | raft: 8e9e05c52164694d became leader at term 2
2018-10-29 15:13:34.161504 I | raft: raft.node: 8e9e05c52164694d elected leader 8e9e05c52164694d at term 2
2018-10-29 15:13:34.162061 I | etcdserver: setting up the initial cluster version to 3.3
2018-10-29 15:13:34.162219 I | etcdserver: published {Name:default ClientURLs:[http://localhost:2379]} to cluster cdf818194e3a8c32
2018-10-29 15:13:34.162482 E | etcdmain: forgot to set Type=notify in systemd service file?
2018-10-29 15:13:34.162521 I | embed: ready to serve client requests
2018-10-29 15:13:34.163342 N | embed: serving insecure client requests on 127.0.0.1:2379, this is strongly discouraged!
2018-10-29 15:13:34.164125 N | etcdserver/membership: set the initial cluster version to 3.3
2018-10-29 15:13:34.164222 I | etcdserver/api: enabled capabilities for version 3.3
```

查看集群健康状态

```bash
# 通过 REST API
root@iZwz97tbgo9lk6rm6lxu2wZ:~# curl http://localhost:2379/health
{"health":"true"}
# etcdctl 命令进行查看
root@iZwz97tbgo9lk6rm6lxu2wZ:~# etcdctl cluster-health
member 8e9e05c52164694d is healthy: got healthy result from http://localhost:2379
cluster is healthy
```

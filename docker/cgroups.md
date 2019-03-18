# 资源控制组 Control Groups

资源控制组（CGroups）是 Linux 内核的一个特性，主要用来对共享资源进行隔离、限制、审计等。只有将分配到容器的资源进行控制，才能避免多个容器同时运行时对宿主机系统的资源竞争。每个控制组是一组对资源的限制，支持层级化结构，硬件资源的隔离。

Docker 容器每次启动时候，通过调用 `func setCapabilities（s*specs.Spec，c*container.Container）error` 方法来完成对各个命名空间的配置。安装 Docker 后，用户可以在`/sys/fs/cgroup/memory/docker/`目录下看到对 Docker 组应用的各种限制项，包括全局限制和位于子目录中对于某个容器的单独限制

进入对应的容器文件夹，可以看到对应容器的限制和目前的使用状态

```bash
root@iZwz97tbgo9lk6rm6lxu2wZ:~# cd /sys/fs/cgroup/memory/docker/
root@iZwz97tbgo9lk6rm6lxu2wZ:/sys/fs/cgroup/memory/docker# ls
1baf29c0e0e8f9e1a654df549877f11992dc2a4a10214edc8a4bfddc13b32716  memory.kmem.failcnt                 memory.numa_stat
42b524d608e9c24ab06aaa287ca24bd8c3d343903650ecfe19d2562a0769ac00  memory.kmem.limit_in_bytes          memory.oom_control
51d6fd963f838cce019d921753799d10708ee9d9bebc8d105060d8515f9d08db  memory.kmem.max_usage_in_bytes      memory.pressure_level
8af6da9b2c2152c4ffe7e0621054c5cc628482678a8fa4d738c8f51c6a3d52fc  memory.kmem.slabinfo                memory.soft_limit_in_bytes
a0fbdfcb164c6f38fc0ec14c60fed992ecc7ba0942b297911d7e9798f4a9723a  memory.kmem.tcp.failcnt             memory.stat
cacfe86e695b91d0c62d87251179094d5037b5f0e906a760aa57a743c79ee650  memory.kmem.tcp.limit_in_bytes      memory.swappiness
cgroup.clone_children                                             memory.kmem.tcp.max_usage_in_bytes  memory.usage_in_bytes
cgroup.event_control                                              memory.kmem.tcp.usage_in_bytes      memory.use_hierarchy
cgroup.procs                                                      memory.kmem.usage_in_bytes          notify_on_release
f46952e02726e3c4d74f4fb174051d8c03dcf365dbbd4abdef265d5599343139  memory.limit_in_bytes               tasks
memory.failcnt                                                    memory.max_usage_in_bytes
memory.force_empty                                                memory.move_charge_at_immigrate
```

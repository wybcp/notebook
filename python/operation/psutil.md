# psutil

一个开源且跨平台的库，其提供了便利的函数用来获取操作系统的信息，如 cpu、内存、磁盘、网络等信息。 此外， psutil 还可以用来进行进程管理，包括判断进程是否存在、获取进程列表、获取进程的详细信息等。 psutil 广泛应用于系统监控、进程管理、资源限制等场景。 此外， psutil 还提供了许多命令行工具提供的功能，包括 ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap。

psutil 是一个跨平台的库，支持 Linux, Windows, OSX, Sun Solaris, FreeBSD, OpenBSD 以及 NetBSD 等操作系统。同时， psutil 也支持 32 位与 64 位的系统架构，支持 Python 2.6 到 Python 3.6 之间所有的 Python 版本 。 psutil 具有简单易用、功能强大、跨平台等诸多优点，广泛应用于开源项目中，比较有名的有 glances、 facebook 的 osquery、 google 的 grr 等。 psutil 不但广泛应用于 Python 语言开发的开源项目中，还被移植到了其他编程语言中，如 Go 语言的 gopsutil、 C 语言的 cpslib、 Rust 语言的 rust-psutil、 Ruby 语言的 posixpsutil 等。 作为一个不算复杂的开源项目， psutil 可以说是非常成功了。

psutil 是一个第三方的开源项目，安装语句如下:
`$ pip3 install psutil`

## cpu

cpu_count 默认返回逻辑 cpu 的个数，也可以指定 logical=False 获取物理 cpu 的个数。

```python
In [2]: import psutil

In [3]: psutil.cpu_count()
Out[3]: 8

In [4]: psutil.cpu_count(logical=False)
Out[4]: 4
```

cpu_percent 返回 cpu 的利用率，可以通过 interval 参数阻塞式地获取 interval 时间范围内的 cpu 利用率，否则，获取上一次调用 cpu_percent 这段时间以来的 cpu 利用率。 可以使用 percpu 参数指定获取每个 cpu 的利用率，默认获取整体的 cpu 利用率。

```python
In [5]: psutil.cpu_percent()
Out[5]: 10.2

In [6]: psutil.cpu_percent(percpu=True)
Out[6]: [25.4, 2.1, 21.1, 1.6, 16.7, 1.5, 12.1, 1.3]

In [7]: psutil.cpu_percent(interval=2,percpu=True)
Out[7]: [9.8, 1.0, 6.4, 0.5, 4.4, 0.5, 3.9, 1.0]
```

cpu_times 以命名元组的形式返回 cpu 的时间花费，也可以通过 percpu 参数指定获取每个 cpu 的统计时间 。

```python
In [9]: psutil.cpu_times()
Out[9]: scputimes(user=81585.4, nice=0.0, system=43806.27, idle=1502731.56)
```

cpu 频率

```python
In [8]: psutil.cpu_freq()
Out[8]: scpufreq(current=2600, min=2600, max=2600)
```

cpu_stats 以命名元组的形式返回 cpu 的统计信息，包括上下文切换、中断、软中断和系统调用的次数 。

```python
In [10]: psutil.cpu_stats()
Out[10]: scpustats(ctx_switches=261118, interrupts=787733, soft_interrupts=379157861, syscalls=1210306)
```

## memory

virtual_memory 以命名元组的形式返回内存使用情况，包括总内存、可用内存、内存利用率、 buffer 和 cached 等。 除了内存利用率，其他字段都以字节为单位返回。

```python
In [11]: psutil.virtual_memory()
Out[11]: svmem(total=17179869184, available=5393928192, percent=68.6, used=14138552320, free=184233984, active=6001106944, inactive=5209694208, wired=2927751168)
```

swap_memory 以命名元组的形式返回 swap memory 的使用情况，显然，对 swap memory 的统计包含了页的换入与换出。

```python
In [12]: psutil.swap_memory()
Out[12]: sswap(total=4294967296, used=2778726400, free=1516240896, percent=64.7, sin=64873414656, sout=538402816)
```

## 磁盘

disk_partitions 返回所有已经挂载的磁盘，以命名元组的形式返回。命名元组包含磁盘名称、挂载点、文件系统类型等信息。

```python
In [2]: psutil.disk_partitions()
Out[2]:
[sdiskpart(device='/dev/disk1s1', mountpoint='/', fstype='apfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel'),
 sdiskpart(device='/dev/disk1s4', mountpoint='/private/var/vm', fstype='apfs', opts='rw,noexec,local,dovolfs,dontbrowse,journaled,multilabel,noatime'),
 sdiskpart(device='/dev/disk1s3', mountpoint='/Volumes/Recovery', fstype='apfs', opts='rw,local,dovolfs,dontbrowse,journaled,multilabel'),]
```

disk_usage 获取磁盘的使用情况，包括磁盘的容量 、已使用的磁盘容量、磁盘空间利用率等。

```python
In [4]: psutil.disk_usage('/')
Out[4]: sdiskusage(total=250685575168, used=176348655616, free=67197939712, percent=72.4)
```

disk_io_counters 以命名元组的形式返回磁盘 io 统计信息，包括读的次数 、写的次数、读字节数、写字节数等。等同`/proc/diskstats`

```python
In [5]: psutil.disk_io_counters()
Out[5]: sdiskio(read_count=6443035, write_count=7245030, read_bytes=170347044864, write_bytes=184492453888, read_time=4362396, write_time=3694126)
```

## 网络

net_io_counters() 函数以命名元组的形式返回了每块网卡的网络 io 统计信息，包括收发字节数、收发包的数量、出错情况与删包情况。等同`/proc/net/dev`

```python
In [6]: psutil.net_io_counters()
Out[6]: snetio(bytes_sent=23920351232, bytes_recv=55712862208, packets_sent=44539931, packets_recv=54945936, errin=0, errout=0, dropin=0, dropout=0)
```

net_connections()以列表的形式返回每个网络连接的详细信息，可以使用该函数查看网络连接状态，统计连接个数以及处于特定状态的网络连接个数。

```python
In [2]: psutil.net_connections()
Out[2]:
[sconn(fd=11, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=6234), raddr=(), status='LISTEN', pid=91505),
 sconn(fd=4, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=53113), raddr=addr(ip='127.0.0.1', port=53112), status='ESTABLISHED', pid=91115),
...]
```

net_if_addrs 以字典的形式返回网卡的配置信息，包括 ip 地址或 mac 地址、子网掩码和广播地址。

net_if_stats 返回网卡的详细信息，包括是否启动、通信类型、传输速度与 mtu。

## 其他

users 以命名元组的方式返回当前登录用户的信息，包括用户名，登录时间，终端与主机信息。

boot_time以时间戳的形式返回系统的启动时间。

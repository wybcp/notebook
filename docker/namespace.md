# 命名空间

命名空间（namespace）是 Linux 内核的一个强大特性，为容器虚拟化的实现带来极大便利。利用这一特性，每个容器都可以拥有自己单独的命名空间，运行在其中的应用都像是在独立的操作系统环境中一样。命名空间机制保证了容器之间彼此互不影响。

在操作系统中，包括内核、文件系统、网络、进程号（Process ID，PID）、用户号（User ID，UID）、进程间通信（InterProcess Communication，IPC）等资源，所有的资源都是应用进程直接共享的。要想实现虚拟化，除了要实现对内存、CPU、网络 IO、硬盘 IO、存储空间等的限制外，还要实现文件系统、网络、PID、UID、IPC 等的相互隔离。前者相对容易实现一些，后者则需要宿主主机系统的深入支持。

docker-containerd 进程作为父进程，会为每个容器启动一个 docker-containerd-shim 进程，作为该容器内所有进程的根进程。

在容器内的进程空间中，则把 docker-containerd-shim 进程作为 0 号根进程（类似宿主系统中 0 号根进程 idle），while 进程的进程号则变为 1（类似宿主系统中 1 号初始化进程/sbin/init）。容器内只能看到 docker-containerd-shim 进程往下的子进程空间，而无法获知宿主机上的进程信息。

## IPC 命名空间

容器中的进程交互还是采用了 Linux 常见的进程间交互方法（Interprocess Communication，IPC），包括信号量、消息队列和共享内存等方式。PID 命名空间和 IPC 命名空间可以组合起来一起使用，同一个 IPC 命名空间内的进程可以彼此可见，允许进行交互；不同空间的进程则无法交互。

## 网络命名空间

Docker 采用虚拟网络设备（Virtual Network Device，VND）的方式，将不同命名空间的网络设备连接到一起。默认情况下，Docker 在宿主机上创建多个虚机网桥（如默认的网桥 docker0），容器中的虚拟网卡通过网桥进行连接

使用 `docker network ls` 命令可以查看到当前系统中的网桥

使用 brctl 工具（需要安装 bridge-utils 工具包），还可以看到连接到网桥上的虚拟网口的信息。每个容器默认分配一个网桥上的虚拟网口，并将 docker0 的 IP 地址设置为默认的网关，容器发起的网络流量通过宿主机的 iptables 规则进行转发：

`brctl show`

## UTS 命名空间

UTS（UNIX Time-sharing System）命名空间允许每个容器拥有独立的主机名和域名，从而可以虚拟出一个有独立主机名和网络空间的环境，就跟网络上一台独立的主机一样。

如果没有手动指定主机名称，Docker 容器的主机名就是返回的容器 ID 的前 6 字节前缀，否则为指定的用户名
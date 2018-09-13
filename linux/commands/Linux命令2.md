## 磁盘管理

查看磁盘空间利用大小

```
df -h
```

查看当前目录所占空间大小

```
du -sh
```

## 打包和解压

在 linux 中打包和压缩和分两步来实现的

tar、zip 命令

打包是将多个文件归并到一个文件:

```shell
tar -cvf etc.tar /etc <==仅打包，不压缩！
gzip demo.txt #压缩
zip -q -r html.zip /home/Blinux/html #打包压缩成zip文件
```

解压

```shell
tar -zxvf xx.tar.gz
unzip test.zip# 解压zip文件
```

## 进程管理

### 查看进程 ps

```shell
 ps -ef	# 查询正在运行的进程信息
 ps -A | grep nginx #查看进程中的nginx
 top #显示进程信息，并实时更新
 lsof -p 23295 #查询指定的进程ID(23295)打开的文件：
```

### 杀死进程 kill

```shell
# 杀死指定PID的进程 (PID为Process ID)
kill 1111
#杀死相关进程
kill -9 3434
```

## 查看网络服务和端口

netstat 命令用于显示各种网络相关信息，如网络连接，路由表，接口状态 (Interface Statistics)，masquerade 连接，多播成员 (Multicast Memberships) 等等。

列出所有端口 (包括监听和未监听的):

```
netstat -a
```

列出所有 tcp 端口:

```
netstat -at
```

列出所有有监听的服务状态:

```
netstat -l
```

## 查看内存 free

缺省时 free 的单位为 KB

```shell
$free
total       used       free     shared    buffers     cached
Mem:       8175320    6159248    2016072          0     310208    5243680
-/+ buffers/cache:     605360    7569960
Swap:      6881272      16196    6865076
```

free 的输出一共有四行，第四行为交换区的信息，分别是交换的总量（total），使用量（used）和有多少空闲的交换区（free），这个比较清楚，不说太多

## 磁盘与目录的容量

### df

列出文件系统的整体磁盘使用量

    [root@study ~]# df [-ahikHTm] [目录或文件名]
    选项与参数：
    -a  ：列出所有的文件系统，包括系统特有的 /proc 等文件系统；
    -k  ：以 KBytes 的容量显示各文件系统；
    -m  ：以 MBytes 的容量显示各文件系统；
    -h  ：以人们较易阅读的 GBytes, MBytes, KBytes 等格式自行显示；
    -H  ：以 M=1000K 取代 M=1024K 的进位方式；
    -T  ：连同该 partition 的 filesystem 名称 （例如 xfs） 也列出；
    -i  ：不用磁盘容量，而以 inode 的数量来显示

由于 df 主要读取的数据几乎都是针对一整个文件系统，因此读取的范围主要是在 Superblock 内的信息

### du

评估文件系统的磁盘使用量（常用在推估目录所占容量）

    [root@study ~]# du [-ahskm] 文件或目录名称
    选项与参数：
    -a  ：列出所有的文件与目录容量，因为默认仅统计目录下面的文件量而已。
    -h  ：以人们较易读的容量格式 （G/M） 显示；
    -s  ：列出总量而已，而不列出每个各别的目录占用容量；
    -S  ：不包括子目录下的总计，与 -s 有点差别。
    -k  ：以 KBytes 列出容量显示；
    -m  ：以 MBytes 列出容量显示；

du 这个指令其实会直接到文件系统内去搜寻所有的文件数据

## 实体链接与符号链接： ln

在 Linux 下面的链接文件有两种，一种是类似 Windows 的捷径功能的文件，可以让你快速的链接到目标文件（或目录）； 另一种则是通过文件系统的 inode 链接来产生新文件名，而不是产生新文件！这种称为实体链接 （hard link）。

### Hard Link

（实体链接, 硬式链接或实际链接）
不能跨 Filesystem；
不能 link 目录。

### Symbolic Link

（符号链接，亦即是捷径）

    [root@study ~]# ln [-sf] 来源文件 目标文件
    选项与参数：
    -s  ：如果不加任何参数就进行链接，那就是hard link，至于 -s 就是symbolic link
    -f  ：如果 目标文件 存在时，就主动的将目标文件直接移除后再创建！

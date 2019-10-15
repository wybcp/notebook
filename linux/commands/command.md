# linux 常用命令

- 查看系统版本信息： `lsb_release -a`
- 查看当前目录文件：`ls -a[查看所有文件包括隐藏]/-l[查看文件显示权限和所属]`
- 查看当前所在路径: `pwd(Print Working Directory)`
- 复制文件或者文件夹：`cp [filename/-r folder]`
- 远程复制文件或者文件夹：
  - 复制本地到远程：`scp [-r] local_path username@ip:path`
  - 复制远程到本地：`scp [-r] username@ip:path local_path`
- 移动或重命名文件或文件夹：`mv [file/folder]`
- 创建文件夹： `mkdir [folder_name]`;
- 变更文件或文件夹权限：`chmod [-R:遍历文件夹下所有文件][权限] [file/folder]`

  - 解释：例如权限为 777 代表 user/group/other 的权限为 4+2+1/4+2+1/4+2+1，4 代表 read 读权限 2 代表写权限 1 代表执行权限
  - drwxr--r--中的第一位: d 代表文件夹，s 代表 socket 文件，-代表普通文件，l 代表软链

- 变更文件所属用户或用户组： `chown owner:group [file/folder]`
- 新建文件：
  - `touch [filename]`
  - `vi/vim [filename]`
- 查看文件：
  - 输出文件内容：`cat [filename]`
  - `tail [-f:实时输出文件内容][filename]`
- 查找内容：

  - grep [正则]
  - awk

- 建立软链： `ln -s [realpath/filename][realpath]`
- 查看包含所有用户的进程：`ps -aux`
- 查看端口： `netstat -anp`

  - a 代表：显示所有，默认不显示 LISTEN 的
  - n 代表：不显示数字别名
  - p 代表：显示关联的程序

- 压缩
  - 解压缩：`tar -zxvf [filename]`
  - 压缩：`tar -zcvf [filename]`
- 查看当前命令所在的路径: `which`
- 查看当前用户
  - who
  - whoami
- 查看当前系统运行多长时间：uptime
- 可读性好的查看磁盘空间：`df -h`
- 可读性好的查看文件空间：`du -f --max-depth=[遍历文件夹的深度][file/folder]`
- debian 添加软件源：apt-add-repository [源]
- 查找文件：

  - `find [path] -name [filename]`
  - `find [path] -user [owername]`
  - `find [path] -group [groupname]`

- 删除文件或者文件夹： rm [-r][file/folder]
- 杀掉进程： kill [pid]
- `ls -al ~`:以 ls 这个“指令”列出“自己主文件夹（~）”下的“所有隐藏文件与相关的文件属性”
- `date`:显示日期与时间,格式化输出：

  ```bash
  date +%Y/%m/%d
  ```

- `cal [month] [year]`:显示日历。显示整年的月历情况：
- `bc`：计算模式，`quit`退出
- `locale`：显示目前所支持的语系
- `who`：看目前有谁在线上
- `netstat -a`：网络的连线状态
- `ps -aux`：背景执行的程序可以执行。
- `sudo -i`：切换为 root 用户
- `su`：切换用户

## 关机

- 关机：`shutdown -h now`
- 关机: `poweroff -f`
- 关机: `reboot`
- 重启: `shutdown -r now`
- 关机: `init 0`
- 关机: `halt`

### 管道和重定向

- 批处理命令连接执行，使用 `|`
- 串联: 使用分号`;`
- 前面成功，则执行后面一条，否则，不执行:`&&`
- 前面失败，则后一条执行: `||`

```shell
ls /proc && echo  suss! || echo failed.
```

## 文本处理

### 文件查找 find

find 参数:

- -name 按名字查找
- -type 按类型
- -atime 访问时间

```shell
find . -atime 7 -type f -print
find . -type d -print  //只列出所有目录
find / -name "hello.c" 查找hello.c文件
```

### 文本查找 grep

```sh
grep match_patten file // 默认访问匹配行
```

常用参数

- -o 只输出匹配的文本行 **VS** -v 只输出没有匹配的文本行

- -c 统计文件中包含文本的次数

  `grep -c “text” filename`

- -n 打印匹配的行号

- -i 搜索时忽略大小写

- -l 只打印文件名

```shell
grep "class" . -R -n # 在多级目录中对文本递归搜索(程序员搜代码的最爱）
cat LOG.* | tr a-z A-Z | grep "FROM " | grep "WHERE" > b #将日志中的所有带where条件的sql查找查找出来
```

### 文本替换 sed

```shell
sed [options] 'command' file(s)
```

- 首处替换

```sh
sed 's/text/replace_text/' file   //替换每一行的第一处匹配的text
```

- 全局替换

```sh
sed 's/text/replace_text/g' file
```

默认替换后，输出替换后的内容，如果需要直接替换原文件,使用-i:

```sh
sed -i 's/text/repalce_text/g' file
```

- 移除空白行

```sh
sed '/^$/d' file
```

```shell
sed 's/book/books/' file #替换文本中的字符串：
sed 's/book/books/g' file
sed '/^$/d' file #删除空白行
```

### 数据流处理 awk

详细教程可以查看 http://awk.readthedocs.io/en/latest/chapter-one.html

```shell
awk ' BEGIN{ statements } statements2 END{ statements } '
```

工作流程

1.执行 begin 中语句块；

2.从文件或 stdin 中读入一行，然后执行 statements2，重复这个过程，直到文件全部被读取完毕；

3.执行 end 语句块；

**特殊变量**

NR:表示记录数量，在执行过程中对应当前行号；

NF:表示字段数量，在执行过程总对应当前行的字段数；

\$0:这个变量包含执行过程中当前行的文本内容；

\$1:第一个字段的文本内容；

\$2:第二个字段的文本内容；

```shell
awk '{print $2, $3}' file
# 日志格式：'$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for"'
#统计日志中访问最多的10个IP
awk '{a[$1]++}END{for(i in a)print a[i],i|"sort -k1 -nr|head -n10"}' access.log
```

### 排序 port

- -n 按数字进行排序 VS -d 按字典序进行排序
- -r 逆序排序
- -k N 指定按第 N 列排序

```shell
sort -nrk 1 data.txt
sort -bd data // 忽略像空格之类的前导空白字符
```

### 去重 uniq

- 消除重复行

```sh
sort unsort.txt | uniq
```

### 统计 wc

```shell
wc -l file // 统计行数
wc -w file // 统计单词数
wc -c file // 统计字符数
```

## 目录

cd：Change Directory 变换工作目录的指令

### 特殊的目录

- `.` 代表此层目录
- `..` 代表上一层目录
- `-` 代表前一个工作目录
- `~` 代表“目前使用者身份”所在的主文件夹
- `~account` 代表 account 这个使用者的主文件夹（account 是个帐号名称）

### mkdir

`mkdir [-mp] 目录名称`

选项与参数：

- `-m` ：设置文件的权限！
- `-p`：帮助你直接将所需要的目录（包含上层目录）递回创建起来！

### rmdir （删除“空”的目录）

`rmdir [-p] 目录名称`

选项与参数：

- -p ：连同“上层”“空的”目录也一起删除

### 删除目录及内容(非空)

```bash
rm -r test
```

### ls

ls 用于列出目录中的文件

选项与参数：

- -a ：全部的文件，连同隐藏文件（ 开头为 . 的文件） 一起列出来（常用）
- -A ：全部的文件，连同隐藏文件，但不包括 . 与 .. 这两个目录
- -d ：仅列出目录本身，而不是列出目录内的文件数据（常用）
- -f ：直接列出结果，而不进行排序 （ls 默认会以文件名排序！）
- -F ：根据文件、目录等信息，给予附加数据结构，例如：\*:代表可可执行文件； /:代表目录； =:代表 socket 文件； &#124;:代表 FIFO 文件；
- -h ：将文件大小以人类较易读的方式（例如 GB, KB 等等）列出来；
- -i ：列出 inode 号码，inode 的意义下一章将会介绍；
- -l ：长数据串行出，包含文件的属性与权限等等数据；（常用）
- -n ：列出 UID 与 GID 而非使用者与群组的名称 （UID 与 GID 会在帐号管理提到！）
- -r ：将排序结果反向输出，例如：原本文件名由小到大，反向则为由大到小；
- -R ：连同子目录内容一起列出来，等于该目录下的所有文件都会显示出来；
- -S ：以文件大小大小排序，而不是用文件名排序；
- -t ：依时间排序，而不是用文件名。
- --color=never ：不要依据文件特性给予颜色显示；
- --color=always ：显示颜色
- --color=auto ：让系统自行依据设置来判断是否给予颜色
- --full-time ：以完整时间模式 （包含年、月、日、时、分） 输出
- --time={atime,ctime} ：输出 access 时间或改变权限属性时间 （ctime）而非内容变更时间 （modification time）

## 查找

### which （寻找“可执行文件”）

`which [-a] command`

选项或参数：

-a ：将所有由 PATH 目录中可以找到的指令均列出，而不止第一个被找到的指令名称

## find 文件文件名的搜寻

通常 find 不很常用的！因为速度慢之外， 也很操硬盘！一般我们都是先使用 whereis 或者是 locate 来检查，如果真的找不到了，才以 find 来搜寻呦！ 为什么呢？因为 whereis 只找系统中某些特定目录下面的文件而已，locate 则是利用数据库来搜寻文件名，当然两者就相当的快速， 并且没有实际的搜寻硬盘内的文件系统状态，比较省时间啦！

### whereis （由一些特定的目录中寻找文件文件名）

    [root@study ~]# whereis [-bmsu] 文件或目录名
    选项与参数：
    -l    :可以列出 whereis 会去查询的几个主要目录而已
    -b    :只找 binary 格式的文件
    -m    :只找在说明文档 manual 路径下的文件
    -s    :只找 source 来源文件
    -u    :搜寻不在上述三个项目当中的其他特殊文件

whereis 主要是针对 /bin /sbin 下面的可执行文件， 以及 /usr/share/man 下面的 man page 文件，

### locate / updatedb

    [root@study ~]# locate [-ir] keyword
    选项与参数：
    -i  ：忽略大小写的差异；
    -c  ：不输出文件名，仅计算找到的文件数量
    -l  ：仅输出几行的意思，例如输出五行则是 -l 5
    -S  ：输出 locate 所使用的数据库文件的相关信息，包括该数据库纪录的文件/目录数量等
    -r  ：后面可接正则表达式的显示方式

经由数据库来搜寻的，而数据库的创建默认是在每天执行一次 （每个 distribution 都不同，CentOS 7.x 是每天更新数据库一次！）

更新 locate 数据库的方法非常简单，直接输入“ updatedb ”就可以了！ updatedb 指令会去读取 /etc/updatedb.conf 这个配置文件的设置，然后再去硬盘里面进行搜寻文件名的动作， 最后就更新整个数据库文件

## 磁盘管理

查看磁盘空间利用大小

```sh
df -h
```

查看当前目录所占空间大小

```sh
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

```sh
netstat -a
```

列出所有 tcp 端口:

```sh
netstat -at
```

列出所有有监听的服务状态:

```sh
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

（实体链接, 硬式链接或实际链接）不能跨 Filesystem；不能 link 目录。

### Symbolic Link

（符号链接，亦即是捷径）

    [root@study ~]# ln [-sf] 来源文件 目标文件
    选项与参数：
    -s  ：如果不加任何参数就进行链接，那就是hard link，至于 -s 就是symbolic link
    -f  ：如果 目标文件 存在时，就主动的将目标文件直接移除后再创建！

## curl

curl 用于传输一个 URL。可以使用这条命令用于测试应用程序的端点或与上游服务端点的连接。curl 还可用于检查你的应用程序是否能连接到其他服务，例如数据库，或检查您的服务是否处于健康的状态。

不带有任何参数时，curl 就是发出 `GET` 请求。
`$ curl https://www.taobao.com`
上面命令向 https://www.taobao.com 发出 `GET` 请求，服务器返回的内容会在命令行输出。

举个例子，假如你的应用程序抛出一个 HTTP 500 错误，表示无法访问 MongoDB 数据库：

```sh
$ curl -I -s myapplication:5000

HTTP/1.0 500 INTERNAL SERVER ERROR
```

-I 选项用于显示头信息，-s 选项表示使用静默模式，不显示错误和进度。检查数据库的端点是否正确：

```sh
$ curl -I -s database:27017

HTTP/1.0 200 OK
```

那么可能是什么问题呢？ 检查您的应用程序是否可以访问数据库以外的其他位置：

```
$ curl -I -s https://opensource.com

HTTP/1.1 200 OK
```

看起来这没问题，现在尝试访问数据库。您的应用程序正在使用数据库的主机名，因此请先尝试：

```sh
$ curl database:27017

curl: (6) Couldn't resolve host 'database'
```

这表示您的应用程序无法解析数据库，因为数据库的 URL 不可用或主机（容器或 VM）没有可用于解析主机名的域名服务器。

## tail

tail 显示文件的最后一部分内容。通常情况下，你不需要浏览每行日志以进行故障排除。而是需要检查日志中对应用程序的最新请求的说明。例如，当你向 Apache HTTP 服务器发起请求时，可以使用 tail 来检查日志中发生的情况。

使用 `tail -f` 来跟踪日志文件并在发起请求时查看它们。

-f 选项表示跟随的意思，它可在日志被写入文件时输出它们。下面的示例具有每隔几秒访问端点的后台脚本，日志会记录请求。除了实时跟踪日志，还可以使用 tail 带上 -n 选项来查看文件的最后 100 行。

```sh
$ tail -n 100 /var/log/httpd/access_log
```

### cat （concatenate 连续）

主要的功能是将一个文件的内容连续的印出在屏幕上面！

```sh
[root@study ~]# cat [-AbEnTv]
选项与参数：
-A  ：相当于 -vET 的整合选项，可列出一些特殊字符而不是空白而已；[tab]会以 ^I 表示，
断行字符则是以 $ 表示，所以你可以发现每一行后面都是 $ 啊！不过断行字符
在Windows/Linux则不太相同，Windows的断行字符是 ^M$ 啰。
-b  ：列出行号，仅针对非空白行做行号显示，空白行不标行号！
-E  ：将结尾的断行字符 $ 显示出来；
-n  ：打印出行号，连同空白行也会有行号，与 -b 的选项不同；
-T  ：将 [tab] 按键以 ^I 显示出来；
-v  ：列出一些看不出来的特殊字符
```

查看文件内容 cat 可以加 more 、less 控制输出的内容的大小

```shell
cat a.text
cat a.text | more
cat a.text| less
```

### tac （反向列示）

### nl （添加行号打印）

      nl [-bnw] 文件
      选项与参数：
      -b  ：指定行号指定的方式，主要有两种：
            -b a ：表示不论是否为空行，也同样列出行号（类似 cat -n）；
            -b t ：如果有空行，空的那一行不要列出行号（默认值）；
      -n  ：列出行号表示的方法，主要有三种：
            -n ln ：行号在屏幕的最左方显示；
            -n rn ：行号在自己字段的最右方显示，且不加 0 ；
            -n rz ：行号在自己字段的最右方显示，且加 0 ；
      -w  ：行号字段的占用的字符数。

## 可翻页检视

### more （一页一页翻动）

    空白键 （space）：代表向下翻一页；
    Enter         ：代表向下翻“一行”；
    /字串   ，重复搜寻同一个字串， 可以直接按下 n      ：代表在这个显示的内容当中，向下搜寻“字串”这个关键字；
    :f            ：立刻显示出文件名以及目前显示的行数；
    q             ：代表立刻离开 more ，不再显示该文件内容。
    b 或 [ctrl]-b ：代表往回翻页，不过这动作只对文件有用，对管线无用。

### less （一页一页翻动）

    空白键    ：向下翻动一页；
    [pagedown]：向下翻动一页；
    [pageup]  ：向上翻动一页；
    /字串     ：向下搜寻“字串”的功能；
    ?字串     ：向上搜寻“字串”的功能；
    n         ：重复前一个搜寻 （与 / 或 ? 有关！）
    N         ：反向的重复前一个搜寻 （与 / 或 ? 有关！）
    g         ：前进到这个数据的第一行去；
    G         ：前进到这个数据的最后一行去 （注意大小写）；
    q         ：离开 less 这个程序；

## 数据撷取

### head （取出前面几行）

```sh
[root@study ~]# head [-n number] 文件
选项与参数：
-n  ：后面接数字，代表显示几行的意思
# 默认的情况中，显示前面十行！
```

### tail （取出后面几行）

```sh
[root@study ~]# tail [-n number] 文件
选项与参数：
-n  ：后面接数字，代表显示几行的意思
-f  ：表示持续侦测后面所接的文件名，要等到按下[ctrl]-c才会结束tail的侦测
```

## 非纯文本文件： od

```sh
[root@study ~]# od [-t TYPE] 文件
选项或参数：
-t  ：后面可以接各种“类型 （TYPE）”的输出，例如：
      a       ：利用默认的字符来输出；
      c       ：使用 ASCII 字符来输出
      d[size] ：利用十进制（decimal）来输出数据，每个整数占用 size Bytes ；
      f[size] ：利用浮点数值（floating）来输出数据，每个数占用 size Bytes ；
      o[size] ：利用八进位（octal）来输出数据，每个整数占用 size Bytes ；
      x[size] ：利用十六进制（hexadecimal）来输出数据，每个整数占用 size Bytes ；
```

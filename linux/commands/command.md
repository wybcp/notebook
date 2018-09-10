# linux 常用命令

- 查看当前目录文件：ls -a[查看所有文件包括隐藏]/-l[查看文件显示权限和所属]
- 查看当前所在路径: pwd(Print Working Directory)
- 复制文件或者文件夹：cp [filename/-r folder]
- 远程复制文件或者文件夹：
  - 复制本地到远程： scp [-r] local_path username@ip:path
  - 复制远程到本地： scp [-r] username@ip:path local_path
- 移动或重命名文件或文件夹： mv [file/folder]
- 创建文件夹： mkdir [folder_name];
- 变更文件或文件夹权限：chmod [-R:遍历文件夹下所有文件][权限] [file/folder]

  - 解释： 例如权限为 777 代表 user/group/other 的权限为 4+2+1/4+2+1/4+2+1，
    4 代表 read 读权限， 2 代表写权限， 1 代表执行权限
  - drwxr--r--中的第一位: d 代表文件夹，s 代表 socket 文件，-代表普通文件，l 代表软链

- 变更文件所属用户或用户组： chown owner:group [file/folder]
- 新建文件：

  - touch [filename]
  - vi/vim [filename]

- 查看文件：

  - 输出文件内容：cat [filename]
  - tail [-f:实时输出文件内容][filename]

- 查找内容：

  - grep [正则]
  - awk

- 建立软链： ln -s [realpath/filename][realpath]
- 查看包含所有用户的进程：ps -aux
- 查看端口： netstat -anp

  - a 代表：显示所有，默认不显示 LISTEN 的
  - n 代表：不显示数字别名
  - p 代表：显示关联的程序

- 压缩
  - 解压缩：tar -zxvf [filename]
  - 压缩：tar -zcvf [filename]
- 查看当前命令所在的路径: which
- 查看当前用户
  - who
  - whoami
- 查看当前系统运行多长时间：uptime
- 可读性好的查看磁盘空间：df -h
- 可读性好的查看文件空间：du -f --max-depth=[遍历文件夹的深度][file/folder]
- debian 添加软件源：apt-add-repository [源]
- 查找文件：

  - find [path] -name [filename]
  - find [path] -user [owername]
  - find [path] -group [groupname]

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

## 文件和目录管理

### 创建和删除

- 删除日志 rm *log (等价: $find ./ -name “*log” -exec rm {} ;)
- 移动：mv
- 复制：cp (复制目录：cp -r )
- 创建文件 touch

### 查看

- 显示当前目录下的文件 **ls**
- 按时间排序，以列表的方式显示目录项 **ls -lrt**

```shell
ls -l
```

- 查看文件内容 cat 可以加 more 、less 控制输出的内容的大小

```shell
cat a.text
cat a.text | more
cat a.text| less
```

### 权限

- 改变文件的拥有者 chown
- 改变文件读、写、执行等属性 chmod
- 递归子目录修改： chown -R tuxapp source/
- 增加脚本可执行权限： chmod a+x myscript

### 管道和重定向

- 批处理命令连接执行，使用 |
- 串联: 使用分号 ;
- 前面成功，则执行后面一条，否则，不执行:&&
- 前面失败，则后一条执行: ||

```shell
ls /proc && echo  suss! || echo failed.
```

## 文本处理

### 文件查找 find

find 参数很多，本文只介绍几个常用的

-name 按名字查找

-type 按类型

-atime 访问时间

```shell
find . -atime 7 -type f -print
find . -type d -print  //只列出所有目录
find / -name "hello.c" 查找hello.c文件
```

### 文本查找 grep

```
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

```
sed 's/text/replace_text/' file   //替换每一行的第一处匹配的text
```

- 全局替换

```
sed 's/text/replace_text/g' file
```

默认替换后，输出替换后的内容，如果需要直接替换原文件,使用-i:

```
sed -i 's/text/repalce_text/g' file
```

- 移除空白行

```
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

$0:这个变量包含执行过程中当前行的文本内容；

$1:第一个字段的文本内容；

$2:第二个字段的文本内容；

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

```
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
- --time={atime,ctime} ：输出 access 时间或改变权限属性时间 （ctime）
  而非内容变更时间 （modification time）

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

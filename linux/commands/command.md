# linux 常用命令

- 切换目录：cd [目录]
- 查看当前目录文件：ls -a[查看所有文件包括隐藏]/-l[查看文件显示权限和所属]
- 查看当前所在路径: pwd
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
- 关机/重启

  - 关机：shutdown -h now
  - 关机: init 0
  - 关机: halt
  - 关机: poweroff
  - 重启: shutdown -r now

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

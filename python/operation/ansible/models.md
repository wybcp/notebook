# [模块](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

1. 将模块拷贝到远程服务器;
2. 执行模块定义的操作，完成对服务器的修改;
3. 在远程服务器中删除模块。

云模块、命令模块、数据库模块、文件模块、资产模块、消息模块、监控模块、网络模块、通知模块、包管理模块、源码控制模块、系统模块、单元模块、 web 设施模块、 windows 模块

## ping 模块

尝试建立 SSH 连接，以便验证用户的 SSH 是否已经正确配置。

```bash
$ ansible test -m ping
```

-m 指定了需要操作的模块。

## 远程命令模块

command、 raw、 script 和 shell 模块都可以实现在远程服务器上执行 Linux 命令。

command 是 Ansible 的默认模块，可以不指定模块名称直接运行 Linux 命令，也可以显示 地通过-m 参数指定 command 模块。 如下所示:

```bash
ansible test a 'hostname'
ansible test -m command -a 'hostname'
ansible test -m command -a '/shin/shutdown -t now’
```

raw 模块相当于使用 SSH 直接执行 Linux 命令，不会进入到 Ansible 的模块子系统中。

shell 模块还可以执行远程服务器上的 shell 脚本文件，脚本文件需要使用绝对路径。

script 模块可以在远程服务器上执行主控节点中的脚本文件，其功能相当于 scp+shell 的组合。 脚本执行完成以后会在远程服务器上删除脚本文件。

## file

file 模块主要用于对远程服务器上的文件(包括链接和目录)进行操作，的权限、修改文件的所有者、创建文件、删除文件等。

```bash
#创建一个目录
ansible test -m file -a 'path=/tmp/dd state=directory mode=0755'
#修改文件的权限
ansible test -m file -a 'path=/tmp/dd state=touch mode=”u=rw,g=r,o=r”'
#创建一个软链接
ansible test -m file -a "src=/tmp/dd dest=/tmp/ddl owner=lmx group=lmx state=link"
#修改一个文件的所有者
ansible test -m file -a "path=/tmp/dd owner=root group=root mode=0644" -become
```

## copy

copy 模块用来将主控节点的文件或目录拷贝到远程服务器上，类似于 Linux 下的 scp 命令。copy 模块比 scp 命令更强大，在拷贝文件到远程服务器的同时，也可以设置文件在远程服务器的权限和所有者。

```bash
#拷贝文件到远程服务器
ansible test -m copy -a 'src=test.sh dest=/tmp/test.sh'
#拷贝文件到远程服务器 ，
如果远程服务器已经存在，则备份文件
ansible test -m copy -a 'src=test.sh dest=/tmp/test.sh backup=yes force=yes'
#拷贝文件到远程服务器 ，并且修改文件的所有者和权限
ansible test -m copy -a 'src=test.sh dest=/tmp/test.sh owner=root group=root mode=644 force=yes' - become
```

## user/group

user 模块请求的是 useradd, userdel, usermod 三个指令，goup 模块请求的是 groupadd, groupdel, groupmod 三个指令。

```bash
#创建一个用户
ansible test m user -a 'name=johnd comment=”John Doe” uid=1329 group=root' -become
#删除一个用户
ansible test -m user -a 'name=johnd state=absent' -become
#创建一个用户，并且产生一对秘钥
ansible test -m user -a 'name=johnd comment=”John Doe” generate_ssh_key=yes ssh_ key_bits=2048 ' -become
#创建群组
ansible test -m group -a 'name=ansible state=present gid=l234' -become
#删除群组
ansible test -m group -a 'name=ansible state=absent' -become
```

## apt

apt 模块用来在 Debian/Ubuntu 系统中安装软件、删除软件。

```bash
#安装软件包
ansible test -m apt -a 'name=git state=present' - become
#卸载软件包
ansible test -m apt -a 'name=git state=absent' -become
#更新源
ansible test -m apt -a 'update_cache=yes' -become
```

## get_url

从互联网下载数据到本地，作用类似于 Linux 下的 curl 命令。get_url 模块比 curl 命令更加灵活，可以控制下载以后的数据所有者、权限以及检查下载数据的 checksum 等。

```bash
#下载文件到远程服务器
ansible test -m get_url -a 'url=http://localhost:8000/data.tar.gz dest=/tmp/data.tar.gz'
#下载文件到远程服务器，并修改文件的权限
ansible test -m get_url -a 'url=http://localhost:8000/data.tar.gz dest=/tmp/data.tar.gz mode=0777'
```

## unarchive

unarchive 模块用于解压文件，其作用类似于 Linux 下的 tar 命令。默认情况下，unarchive 的作用是将控制节点的压缩包拷贝到远程服务器 ，然后进行解压。

```bash
#先创建一个目录
ansible test -m file -a 'path=/tmp/data state=directory'
#解压本地文件
ansible test -m unarchive -a 'src=data.tar.gz dest=/tmp/data list_files=yes'
#将本地文件拷贝到远程
ansible test -m copy -a 'src=data.tar.bz2 dest=/tmp/data.tar.bz2'
#解压远程的文件
ansible test -m unarchive -a 'src=/tmp/data.tar.bz2 dest=/tmp remote_src=yes'
```

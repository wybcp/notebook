# linux 目录

- `.` 代表此层目录
- `..` 代表上一层目录
- `-` 代表前一个工作目录
- `~` 代表『目前使用者身份』所在的主目录
- `~account` 代表 account 用户的主目录(account 是个帐号名称)

## 相关命令

- cd (change directory, 变换目录)
- pwd (显示目前所在的目录)

        [root@study ~]# pwd [-P]
        选项与参数：
        -P ：显示出确实的路径，而非使用连结(link) 路径。

- mkdir (建立新目录)

        [root@study ~]# mkdir [-mp]目录名称
        选项与参数：
        -m ：设定档案的权限喔
        -p ：帮助你直接将所需要的目录(包含上层目录)递回建立起来！

- rmdir (删除空的目录)：将所有目录下的东西都杀掉，必须使用`rm -r 目录名称`

       [root@study ~]# rmdir [-p]目录名称
        选项与参数：
        -p ：连同上层空的目录也一起删除

- cp (复制档案或目录)
# 用户管理

## useradd

    [root@study ~]# useradd [-u UID] [-g 初始群组] [-G 次要群组] [-mM]\
    &gt;  [-c 说明栏] [-d 主文件夹绝对路径] [-s shell] 使用者帐号名
    选项与参数：
    -u  ：后面接的是 UID ，是一组数字。直接指定一个特定的 UID 给这个帐号；
    -g  ：后面接的那个群组名称就是我们上面提到的 initial group 啦～
          该群组的 GID 会被放置到 /etc/passwd 的第四个字段内。
    -G  ：后面接的群组名称则是这个帐号还可以加入的群组。
          这个选项与参数会修改 /etc/group 内的相关数据喔！
    -M  ：强制！不要创建使用者主文件夹！（系统帐号默认值）
    -m  ：强制！要创建使用者主文件夹！（一般帐号默认值）
    -c  ：这个就是 /etc/passwd 的第五栏的说明内容啦～可以随便我们设置的啦～
    -d  ：指定某个目录成为主文件夹，而不要使用默认值。务必使用绝对路径！
    -r  ：创建一个系统的帐号，这个帐号的 UID 会有限制 （参考 /etc/login.defs）
    -s  ：后面接一个 shell ，若没有指定则默认是 /bin/bash 的啦～
    -e  ：后面接一个日期，格式为“YYYY-MM-DD”此项目可写入 shadow 第八字段，
          亦即帐号失效日的设置项目啰；
    -f  ：后面接 shadow 的第七字段项目，指定密码是否会失效。0为立刻失效，
          -1 为永远不失效（密码只会过期而强制于登陆时重新设置而已。）

范例一：完全参考默认值创建一个使用者，名称为 vbird1

```bash
[root@study ~]# useradd vbird1
[root@study ~]# ll -d /home/vbird1
drwx------. 3 vbird1 vbird1 74 Jul 20 21:50 /home/vbird1
# 默认会创建使用者主文件夹，且权限为 700 ！这是重点！

[root@study ~]# grep vbird1 /etc/passwd /etc/shadow /etc/group
/etc/passwd:vbird1:x:1003:1004::/home/vbird1:/bin/bash
/etc/shadow:vbird1:!!:16636:0:99999:7:::
/etc/group:vbird1:x:1004:     &lt;==默认会创建一个与帐号一模一样的群组名
```

## passwd

    [root@study ~]# passwd [--stdin] [帐号名称]  &lt;==所有人均可使用来改自己的密码
    [root@study ~]# passwd [-l] [-u] [--stdin] [-S] \
    &gt;  [-n 日数] [-x 日数] [-w 日数] [-i 日期] 帐号 &lt;==root 功能
    选项与参数：
    --stdin ：可以通过来自前一个管线的数据，作为密码输入，对 shell script 有帮助！
    -l  ：是 Lock 的意思，会将 /etc/shadow 第二栏最前面加上 ! 使密码失效；
    -u  ：与 -l 相对，是 Unlock 的意思！
    -S  ：列出密码相关参数，亦即 shadow 文件内的大部分信息。
    -n  ：后面接天数，shadow 的第 4 字段，多久不可修改密码天数
    -x  ：后面接天数，shadow 的第 5 字段，多久内必须要更动密码
    -w  ：后面接天数，shadow 的第 6 字段，密码过期前的警告天数
    -i  ：后面接“日期”，shadow 的第 7 字段，密码失效日期

## chage 详细的密码参数显示功能

    [root@study ~]# chage [-ldEImMW] 帐号名
    选项与参数：
    -l ：列出该帐号的详细密码参数；
    -d ：后面接日期，修改 shadow 第三字段（最近一次更改密码的日期），格式 YYYY-MM-DD
    -E ：后面接日期，修改 shadow 第八字段（帐号失效日），格式 YYYY-MM-DD
    -I ：后面接天数，修改 shadow 第七字段（密码失效日期）
    -m ：后面接天数，修改 shadow 第四字段（密码最短保留天数）
    -M ：后面接天数，修改 shadow 第五字段（密码多久需要进行变更）
    -W ：后面接天数，修改 shadow 第六字段（密码过期前警告日期）

## usermod

    [root@study ~]# usermod [-cdegGlsuLU] username
    选项与参数：
    -c  ：后面接帐号的说明，即 /etc/passwd 第五栏的说明栏，可以加入一些帐号的说明。
    -d  ：后面接帐号的主文件夹，即修改 /etc/passwd 的第六栏；
    -e  ：后面接日期，格式是 YYYY-MM-DD 也就是在 /etc/shadow 内的第八个字段数据啦！
    -f  ：后面接天数，为 shadow 的第七字段。
    -g  ：后面接初始群组，修改 /etc/passwd 的第四个字段，亦即是 GID 的字段！
    -G  ：后面接次要群组，修改这个使用者能够支持的群组，修改的是 /etc/group 啰～
    -a  ：与 -G 合用，可“增加次要群组的支持”而非“设置”喔！
    -l  ：后面接帐号名称。亦即是修改帐号名称， /etc/passwd 的第一栏！
    -s  ：后面接 Shell 的实际文件，例如 /bin/bash 或 /bin/csh 等等。
    -u  ：后面接 UID 数字啦！即 /etc/passwd 第三栏的数据；
    -L  ：暂时将使用者的密码冻结，让他无法登陆。其实仅改 /etc/shadow 的密码栏。
    -U  ：将 /etc/shadow 密码栏的 ! 拿掉，解冻啦！

## id

    id [username]

相关 UID/GID 等等的信息

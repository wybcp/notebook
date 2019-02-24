# MySQL 安全

## 操作系统相关的安全问题

常见的操作系统安全问题主要出现在 MySQL 的安装和启动过程中.

### 1.严格控制操作系统账号和权限

在数据库服务器上要严格控制操作系统的账号和权限，比如：

- 锁定 mysql 用户
- 其他任何用户都采取独立的账号登录，管理员通过 mysql 专有用户管理 MySQL，或者通过 root su 到 mysql 用户下进行管理。
- mysql 用户目录下，除了数据文件目录，其他文件和目录属主都改为 root

### 2.尽量避免以 root 权限运行 MySQL

MySQL 安装完毕后，一般会将数据目录属主设置为 mysql 用户，而将 MySQL 软件目录的属主设置为 root，这样做的目的是当使用 mysql 启动数据库时，可以防止任何具有 FILE 权限的用户能够用 root 创建文件。而如果使用 root 用户启动数据库，则任何具有 FILE 权限的用户都可以读写 root 用户的文件，这样会给系统造成严重的安全隐患。

### 3.防止 DNS 欺骗

创建用户时，host 可以指定域名或者 IP 地址。但是，如果指定域名，就可能带来如下安全隐患： 如果域名对应的 IP 地址被恶意修改，则数据库就会被恶意的 IP 地址进行访问，导致安全隐患。

## 数据库相关的安全问题

常见的数据库问题大多数是由于账号的管理不当造成的。应该加强对账号管理的安全意识。

### 1.删除匿名账号

在某些版本的中，安装完毕 MySQL 后，会自动安装一个空账号，此账号具有对 test 数据库的全部权限，普通用户只需要执行 mysql 命令即可登录 MySQL 数据库，这个时候默认使用了空用户，可以在 test 数据库里面做各种操作，比如可以创建一个大表，占用大量磁盘空间，这样给系统造成了安全隐患。

### 2.给 root 账号设置口令

MySQL 安装完毕后，root 默认口令为空，需要马上修改口令

```sql
set password=password('newpassword');
```

### 3.设置安全密码

密码的安全体现在以下两个方面：

- 设置安全的密码，建议使用 6 位以上字母、数字、下划线和一些特殊字符组合的而成的字符串；
- 使用上的安全，使用密码期间尽量保证使用过程安全，不会被别人窃取。

（1）直接将密码写在命令行中。

`mysql -uroot -p123`

（2）交互式方式输入密码。

`mysql -uroot -p`

（3）将用户名和密码写在配置文件里面，连接的时候自动读取，比如应用连接数据库或者执行一些批处理脚本。对于这种方式，MySQL 供了一种方法，在 my.cnf 里面写入连接信息。

```conf
[client]
user=username
password=password
```

然后对配置文件进行严格的权限限制，例如：

`chomod +600 my.cnf`

以上是 3 种常见的密码使用方式。很显然，第 1 种最不安全，因为它将密码写成为明文；第 2 种比较安全，但是只能使用在交互的界面下；第 3 种比较方便，但是需要将配置文件设置严格的存取权限，而且任何只要可以登录操作系统的用户都可能自动登录，存在一定的安全隐患。

### 4.只授予账号必须的权限

### 5.除 root 外，任何用户不应有 mysql 库 user 表的存取权限

由于 MySQL 中可以通过更改 mysql 数据库的 user 表进行权限的增加、删除、变更等操作，因此，除了 root 以外，任何用户都不应该拥有对 user 表的存取权限（SELECT、UPDATE、INSERT、DELETE 等），造成系统的安全隐患。

### 6.不要把 FILE、PROCESS 或 SUPER 权限授予管理员以外的账号

FILE 权限主要以下作用：

将数据库的信息通过 SELECT ...INTO OUTFILE...写到服务器上有写权限的目录下，作为文本格式存放。具有权限的目录也就是启动 MySQL 时的用户权限目录。

可以将有读权限的文本文件通过 LOAD DATA INFILE...命令写入数据表，如果这些表中存放了很重要的信息，将对系统造成很大的安全隐患。

ROCESS 权限能被用来执行“show processlist”命令，查看当前所有用户执行的查询的明文文本，包括设定或改变密码的查询。在默认情况下，每个用户都可以执行“show processlist”命令，但是只能查询本用户的进程。因此，对 PROCESS 权限管理不当，有可能会使得普通用户能够看到管理员执行的命令。

SUPER 权限能够执行 kill 命令，终止其他用户进程。

### 7.LOAD DATA LOCAL 带来的安全问题

LOAD DATA 默认读的是服务器上的文件，但是加上 LOCAL 参数后，就可以将本地具有访问权限的文件加载到数据库中。这在在带来方便的同时，可带来了以下安全问题。

可以任意加载本地文件到数据库。

在 Web 环境中，客户从 Web 服务器连接，用户可以使用 LOAD DATA LOCAL 语句来读取 Web 服务器进程在读访问权限的任何文件（假定用户可以运行 SQL 服务器的任何命令）。在这种环境中，MySQL 服务器的客户实际上的是 Web 服务器，而不是连接 Web 服务器的用户运行的程序。

解决的方法是，可以用--local-infile=0 选项启动 mysqld 从服务器禁用所有 LOAD DATA LOCAL 命令。

对于 mysql 命令行客户端，可以通过指定--local-infile[=1]选项启用 LOAD DATA LOCAL，或通过--local-infile=0 选项禁用。类似地，对于 mysqlimport，--local or -L 选项启用本地文件装载。在任何情况下，成功进行本地装载需要服务器启用相关选项。

### 8.DROP TABLE 命令并不收回以前的相关访问权限

DROP 表的时候，其他用户对此表的权限并没有被收回，这样导致重新创建同名的表时，以前其他用户对此表的权限会自动自动赋予，进而产生权限外流。因此，在删除表时，要同时取消其他用户在此表上的相应权限。

### 9.使用 SSL

SSL（Secure Socket Layer，安全套接字层）是一种安全传输的协议，最初 Netscape 公司所开发，用以保障在 Internet 上数据传输之安全，利用 数据加密（Encryption）技术，可确保数据在网络上传输过程中不会被截取及窃听。

SSL 协议提供的服务主要有：

（1）认证用户和服务器，确保数据发送到正确的客户机和服务器；

（2）加密数据以防止数据中途被窃取；

（3）维护数据的完整性，确保数据在传输过程中不被改变。

在 MySQL 中，要想使用 SSL 进行安全传输，需要在命令行中或选项文件中设置“--ssl”选项。

对于服务器，“ssl”选项规定该服务器允许 SSL 连接。对于客户端端程序，它允许客户使用 SSL 连接。对于客户端程序，它允许客户端用 SSL 连接服务器。单单该选项不足以使用 SSL 连接。还必须指定--ssl-ca、--ssl-cert 和--ssl-key 选项。如果不想启用 SSL，可以将选项指定为--skip-ssl 或--ssl=0。

请注意，如果编译的服务器或客户端不支持 SSL，则使用普通的示加密的连接。

确保使用 SSL 连接的安全方式是，使用含 REQUIRE SSL 子句的 GRANT 语句在服务器上创建一账户，然后使用该账户来连接服务器，服务器和客户端均应启用 SSL 支持。下面例子创建了一个含 REQUIRE SSL 子句的账号：

```bash
mysql>grant select on *.* to cqh identified by '123' REQUIRE ssl;
```

- --ssl-ca=file_name 含可信的 SSL CA 的清单的文件的路径
- --ssl-cert=file_name SSL 证书文件名，用于建立安全连接
- --ssl-key=file_name SSL 密钥文件名，用于建立 安全连接

### 10.如果可能，给所有用户加上访问 IP 限制

### 11.REVOKE 命令的漏洞

当用户多次赋予权限后，由于各种原因，需要将此用户的权限全部取消，此时，REVOKE 命令可能并不会按照我们的意愿执行，来看看下面的例子。

这个是 MySQL 权限机制造成的隐患，在一个数据库上多次赋予权限，权限会自动合并；但是在多个数据库上多次赋予权限，每个数据库上都会认为是单独的一组权限，必须在此数据库上用 REVOKE 命令来单进行权限收回，而 REVOKE ALL PRIVILEGES ON _._ 并不会替用户自动完成这个情况。

## 外网访问 MySQL 安全

线上业务为了保证数据安全，一般只允许本地或者内网访问 MySQL。但一些特殊情况下，需要通过外网访问 MySQL。此时为了保证权限最小化开放，首先要做两方面措施：

一方面需要配置防火墙白名单

```bash
iptables -A INPUT -s 1.2.3.4 -p tcp -m tcp –dport 3306 -j ACCEPT
```

另一方面创建 MySQL 用户时限制访问 IP

```bash
mysql> CREATE USER ‘testuser’@’1.2.3.4’ IDENTIFIED BY ‘testpass’;
```

MySQL 的访问默认是明文的，与明文的 HTTP 的容易受到监听、劫持类似，暴露在外网的 MySQL 通信也有可能受到监听、中间人攻击等。下面以一个具体例子进行说明。

### 1 监听 MySQL 主从的明文通信

实现监听的方案有多种，我们采用了交换机端口镜像的方式进行旁路监听。

准备监听的机器为 xxx.xxx.xxx.83，发起攻击的机器为 xxx.xxx.xxx.109。

实施 MySQL 主从通信的监听时，无论是监听主库还是从库效果都类似，这里测试监听主库的情况。

#### 1.1 确定要监听的端口

如果不知道这两台机器对应交换机哪个端口，可以先登录交换机，ping 然后通过 arp 缓存查看。

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/1-6.png)

ping 之后就能通过 arp 缓存确定端口

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/2.jpg)

最后，确定 xxx.xxx.xxx.83 即镜像源端口为 g0/15，xxx.xxx.xxx.109 即镜像目标端口为 g0/1。

#### 1.2 配置端口镜像

登录交换机，开始没有配置镜像

```conf
<H3C>dis mir

The monitor port has not been configured! <H3C>sys

Password: ############

Enter system view, return to user view with Ctrl+Z.
```

分别配置镜像目标和镜像源端口

```conf
[H3C]monitor-port g0/1
Succeed! the monitor port has been specified to be Trunk port  and the pvid
changed.
[H3C]mirroring-port g0/15
[H3C]
[H3C]dis mir
Monitor-port:
        GigabitEthernet0/1
Mirroring-port:
        GigabitEthernet0/15
[H3C]q
<H3C>save
This will save the configuration in the EEPROM memory
Are you sure?[Y/N]y
Now saving current configuration to EEPROM memory
Please wait for a while...
Current configuration saved to EEPROM memory successfully
```

#### 1.3 监听明文的主从通信

在主动监听的机器 xxx.xxx.xxx.109 执行

tcpdump host xxx.xxx.xxx.83 -i eth0 -w hello.dump

xxx.xxx.xxx.83 配置了 MySQL 主库，另外的一台外网机器 xxx.xxx.xxx.104 配置了 MySQL 从库。并且该主从并未配置 SSL 加密。测试中利用 xxx.xxx.xxx.109 成功监听到 MySQL 主从的通信。

下图为监听到的 MySQL 帐号登录，可以得到用户名和加密后的密码：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://img.mp.sohu.com/upload/20170527/d3896b601cb8441892bf80999272a751.png)

对于不复杂的 MySQL 密码，可以很容易通过 cmd5 等网站解密出明文：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/3-1.jpg)

下图为监听到的主从数据：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/4.jpg)

可以看到，在 MySQL 主从明文通信的情况下，可以实现有效的窃听。

这里采用的交换机端口镜像需要获得交换机权限，有一定的实施难度。但在外网通信中，实际的网络环境非常复杂且不受我们控制，明文通信仍然有潜在的安全风险。

### 2 服务器间安全访问

那么如何在服务器之间的外网通信中确保 MySQL 的安全访问呢？这里介绍几种常用方案。

#### 2.1 加密隧道

加密隧道可以将客户端的网络数据进行加密，然后安全地传输到服务端后进行解密还原。以 stunnel 为例：

首先在客户端监听 3306 端口，并建立加密通信，连接到远程的 1.2.4.5:8000

`/usr/local/stunnel/etc/stunnelclient.conf`

```conf
sslVersion = TLSv1

CAfile = /usr/local/stunnel/etc/ca-cert.pem

cert = /usr/local/stunnel/etc/clientcert.pem

key = /usr/local/stunnel/etc/clientkey.pem

[mysql]

accept = 127.0.0.1:3306

connect =1.2.4.5:8000
```

服务端监听 8000 端口，并将数据解密后转发到本机的 3306 端口

`/usr/local/stunnel/etc/stunnelserver.conf`

```conf
sslVersion = TLSv1

CAfile = /usr/local/stunnel/etc/ca-cert.pem

cert = /usr/local/stunnel/etc/servercert.pem

key = /usr/local/stunnel/etc/serverkey.pem

[mysql]

accept=8000

connect=127.0.0.1:3306
```

这样，客户端访问本地 3306 端口实际会访问到远程 1.2.4.5 机器的 3306 端口，实现了通过加密隧道访问远程的 MySQL。

优点：无需单独创建外网的 MySQL 帐号，对本地访问透明。

缺点：只能实现从客户端到服务端的加密访问，需要额外维护加密隧道服务。

#### 2.2 VPN

VPN 可以将外网通信转化为虚拟的内网通信，直接解决外网访问的安全问题。以 OPENVPN 为例：

在其中一边的服务器搭建服务端，配置内网网段

`/etc/openvpn/server.conf`

```conf
port 1194

proto tcp-server

dev tap

#证书相关

ca /etc/openvpn/ca-cert.pem

cert /etc/openvpn/server.pem

key /etc/openvpn/server.key

dh /etc/openvpn/dh.pem

#指定Server端使用的地址

ifconfig 192.168.10.1 255.255.255.0

#指定客户端的IP

client-config-dir /etc/openvpn/ccd
```

在另一边的服务器搭建客户端，发起 VPN 链接

`/etc/openvpn/client.conf`

```conf
client

dev tap

proto tcp-client

remote 1.2.3.4 1194

#证书相关

ca /etc/openvpn/ca-cert.pem

cert /etc/openvpn/client1-cert.pem

key /etc/openvpn/client1-key.pem
```

这样，两边的服务器就建立起虚拟的内网，可以访问相互的 MySQL 或者其他服务。

优点：两边都可以相互访问，且不限于访问某个端口，特别适合异地机房间的内网互通。

缺点：需要额外维护 VPN 服务。

#### 2.3 MySQL SSL

除了建立加密隧道、加密虚拟网络，还可以直接使用 SSL 进行 MySQL 的访问加密。

2.3.1 SSL 证书的生成

首先检查 MySQL 是否支持 SSL。

```bash
mysql> SHOW VARIABLES LIKE ‘have_ssl’;

+—————+———-+ | Variable_name | Value

| +—————+———-+ | have_ssl      | DISABLED |

+—————+———-+ 1 row in set (0.00 sec)
```

如果输出如上，说明 MySQL 支持 SSL 但未启用。

SSL 证书分多种类型，实际中要根据不同用途来使用服务端或客户端的证书。

```conf
[mysqld]

# 服务端类型SSL证书，用于服务端，或者主从关系中的主库

ssl-ca=/home/mysql/certs/ca-cert.pem ssl-cert=/home/mysql/certs/server-cert.pem

ssl-key=/home/mysql/certs/server-key.pem
```

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/5.jpg)

```conf
[client]

# 客户端类型SSL证书，用于客户端（如命令行工具），或者主从关系中的从库

ssl-ca=/home/mysql/certs/ca-cert.pem

ssl-cert=/home/mysql/certs/client-cert.pem

ssl-key=/home/mysql/certs/client-key.pem
```

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/6.jpg)

此外，为了方便统一管理，在同一台机器可以使用同时支持服务端和客户端类型的单一 SSL 证书。只需要生成 SSL 证书时指定两种类型的用法或者直接不指定任一种用法。

配置完毕后，检查下 SSL 是否已启用

```bash
mysql> SHOW VARIABLES LIKE ‘%ssl%’;


+—————+———————–+

| Variable_name | Value                 |

+—————+———————–+

| have_openssl  | YES                   |

| have_ssl      | YES                   |

| ssl_ca        | /home/mysql/certs/ca-cert.pem  |

| ssl_capath    |                       |

| ssl_cert      | /home/mysql/certs/mysql-cert.pem |

| ssl_cipher    |                       |

| ssl_key       | /home/mysql/certs/mysql-key.pem |

+—————+———————–+

5 rows in set (0.00 sec)
```

如果输出如上，说明 SSL 已正常启用

2.3.2 require SSL 与 require X509

为了确保外网访问的 MySQL 用户使用了 SSL 加密，在生成用户时可以强制要求 REQUIRE SSL 或 REQUIRE X509：

```bash
mysql> CREATE USER ‘testuser’@’1.2.3.4’ IDENTIFIED BY ‘testpass’ REQUIRE SSL;

mysql> CREATE USER ‘testuser’@’1.2.3.4’ IDENTIFIED BY ‘testpass’ REQUIRE X509;
```

两者的区别在于，REQUIRE SSL 只要求客户端使用指定 ca 证书对服务端证书进行验证，而 REQUIRE X509 还要求服务端对客户端证书进行验证。为了避免中间人攻击，确保更安全的通信，一般建议使用 REQUIRE X509。

2.3.3 OpenSSL 与 yaSSL

MySQL 可以使用自带的 yaSSL 库进行加密通信，也可以使用 OpenSSL 进行加密通信。具体使用哪种，需要在编译时指定 WITH_SSL:STRING 的参数：

```bash
bundled (use yassl), yes (prefer os library if present, otherwise use bundled), system

(use os library), </path/to/custom/installation>
```

为了更好的安全性，可以使用系统自带的 OpenSSL，并及时做好 yum/apt 更新。

如果考虑不同版本的兼容性，那么建议使用自带的 yaSSL。

比如 OpenSSL 曾针对 CVE-2015-4000 的漏洞将 DH key 的最小值提高到 768 bits，而一些旧版本 MySQL 的 DH key 使用了 512 bits。因为 MySQL 的默认 SSL 加密算法是 DHE-RSA-AES256-SHA，如果使用了 OpenSSL 的 MySQL，在不同版本间的访问可能会出现 ERROR 2026 的错误提示。

#### 2.3.4 监听基于 SSL 的主从通信

配置了 SSL 加密之后，我们再次尝试抓取 MySQL 主从通信。

发现无法获取到 MySQL 主从的登录帐号：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/7.jpg)

此外截取到的 MySQL 主从数据也是乱码：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/8.jpg)

可以看到，在 MySQL 主从经过 SSL 加密的情况下，无法实现有效窃听。

### 3 本地安全访问

#### 3.1 SSH 隧道

一般我们都需要 SSH 方式从本地访问远程服务器，这时可以建立 SSH 隧道来访问远程服务器的特定端口。

如使用 SecureCRT 的端口转发功能（Putty 也类似），将本地 3306 端口转发到服务器的 3306 端口：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/10.jpg)

如果习惯使用 navicat 这类工具，可以使用自带的 SSH 隧道功能（注意旧版可能要将私钥转换成 ppk 格式）：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/11.jpg)

#### 3.2 phpmyadmin+HTTPS

如果习惯使用 phpmyadmin 的 web 方式访问 MySQL，那么只需要将访问方式统一为 HTTPS：

```conf
server
{
listen 80;
server_name phpmyadmin.example.com;
#使用HSTS强制把HTTP跳转到HTTPS
add_header Strict-Transport-Security “max-age=31536000 “;
……
}

server
{
listen 443 ssl http2;
server_name phpmyadmin.example.com;
#配置服务端SSL证书
ssl on;
ssl_certificate /etc/letsencrypt/live/phpmyadmin.example.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/ phpmyadmin.example.com/privkey.pem;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
……
}
```

## 4 总结

MySQL 的数据安全是一个非常大的课题，其中外网间的安全通信往往容易被忽略。而当前随着 HTTPS /SMTPS/POP3S/IMAPS 的逐步流行，各种基于 TCP、UDP 的加密通信方案也会越来越多地应用到线上业务中。本文针对服务器间/本地到服务器的一些访问 MySQL 的场景介绍了几种加密通信方案，希望能给到大家一些思路，并结合自己实际需要来使用 MySQL 的加密访问。

## 参考

- [MySQL 安全问题（防范必知）](http://www.cnblogs.com/chenqionghe/p/4873665.html)
- [远程访问 Mysql？教你为数据传输再加把安全锁！](http://www.yunweipai.com/archives/18614.html)

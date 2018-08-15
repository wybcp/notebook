线上业务为了保证数据安全，一般只允许本地或者内网访问MySQL。但一些特殊情况下，需要通过外网访问MySQL。此时为了保证权限最小化开放，首先要做两方面措施：

一方面需要配置防火墙白名单

```
iptables -A INPUT -s 1.2.3.4 -p tcp -m tcp –dport 3306 -j ACCEPT
```

另一方面创建MySQL用户时限制访问IP

```
mysql> CREATE USER ‘testuser’@’1.2.3.4’ IDENTIFIED BY ‘testpass’;
```

那么，做到这一步就可以高枕无忧了吗？如果是的话，文章到此就可以结束了。但是很遗憾，实际上仍然存在安全隐患。MySQL的访问默认是明文的，与明文的HTTP的容易受到监听、劫持类似，暴露在外网的MySQL通信也有可能受到监听、中间人攻击等。下面以一个具体例子进行说明。

**1 监听MySQL主从的明文通信**

实现监听的方案有多种，我们采用了交换机端口镜像的方式进行旁路监听。

准备监听的机器为xxx.xxx.xxx.83，发起攻击的机器为xxx.xxx.xxx.109。

实施MySQL主从通信的监听时， 无论是监听主库还是从库效果都类似，这里测试监听主库的情况。

**1.1 确定要监听的端口**

如果不知道这两台机器对应交换机哪个端口，可以先登录交换机，ping然后通过arp缓存查看。

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/1-6.png)

ping之后就能通过arp缓存确定端口

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/2.jpg)

最后，确定xxx.xxx.xxx.83即镜像源端口为g0/15，xxx.xxx.xxx.109即镜像目标端口为g0/1。

**1.2 配置端口镜像**

登录交换机，开始没有配置镜像

```
<H3C>dis mir

The monitor port has not been configured! <H3C>sys

Password: ************

Enter system view, return to user view with Ctrl+Z.
```

分别配置镜像目标和镜像源端口

```
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

**1.3 监听明文的主从通信**

在主动监听的机器xxx.xxx.xxx.109执行

tcpdump host xxx.xxx.xxx.83 -i eth0 -w hello.dump

xxx.xxx.xxx.83配置了MySQL主库，另外的一台外网机器xxx.xxx.xxx.104配置了MySQL从库。并且该主从并未配置SSL加密。测试中利用xxx.xxx.xxx.109成功监听到MySQL主从的通信。

下图为监听到的MySQL帐号登录，可以得到用户名和加密后的密码：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://img.mp.sohu.com/upload/20170527/d3896b601cb8441892bf80999272a751.png)

对于不复杂的MySQL密码，可以很容易通过cmd5等网站解密出明文：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/3-1.jpg)

下图为监听到的主从数据：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/4.jpg)

可以看到，在MySQL主从明文通信的情况下，可以实现有效的窃听。

这里采用的交换机端口镜像需要获得交换机权限，有一定的实施难度。但在外网通信中，实际的网络环境非常复杂且不受我们控制，明文通信仍然有潜在的安全风险。

**2 服务器间安全访问**

那么如何在服务器之间的外网通信中确保MySQL的安全访问呢？这里介绍几种常用方案。

**2.1 加密隧道**

加密隧道可以将客户端的网络数据进行加密，然后安全地传输到服务端后进行解密还原。以stunnel为例：

首先在客户端监听3306端口，并建立加密通信，连接到远程的1.2.4.5:8000

```
/usr/local/stunnel/etc/stunnelclient.conf
```

```
sslVersion = TLSv1

CAfile = /usr/local/stunnel/etc/ca-cert.pem

cert = /usr/local/stunnel/etc/clientcert.pem

key = /usr/local/stunnel/etc/clientkey.pem

[mysql]

accept = 127.0.0.1:3306

connect =1.2.4.5:8000
```

服务端监听8000端口，并将数据解密后转发到本机的3306端口

```
/usr/local/stunnel/etc/stunnelserver.conf
```

sslVersion = TLSv1

CAfile = /usr/local/stunnel/etc/ca-cert.pem

cert = /usr/local/stunnel/etc/servercert.pem

key = /usr/local/stunnel/etc/serverkey.pem

[mysql]

accept=8000

connect=127.0.0.1:3306

这样，客户端访问本地3306端口实际会访问到远程1.2.4.5机器的3306端口，实现了通过加密隧道访问远程的MySQL。

优点：无需单独创建外网的MySQL帐号，对本地访问透明。

缺点：只能实现从客户端到服务端的加密访问，需要额外维护加密隧道服务。

**2.2 VPN**

VPN可以将外网通信转化为虚拟的内网通信，直接解决外网访问的安全问题。以OPENVPN为例：

在其中一边的服务器搭建服务端，配置内网网段

```
/etc/openvpn/server.conf
```

```
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

在另一边的服务器搭建客户端，发起VPN链接

```
/etc/openvpn/client.conf

client

dev tap

proto tcp-client

remote 1.2.3.4 1194

#证书相关

ca /etc/openvpn/ca-cert.pem

cert /etc/openvpn/client1-cert.pem

key /etc/openvpn/client1-key.pem
```

这样，两边的服务器就建立起虚拟的内网，可以访问相互的MySQL或者其他服务。

优点：两边都可以相互访问，且不限于访问某个端口，特别适合异地机房间的内网互通。

缺点：需要额外维护VPN服务。

**2.3 MySQL SSL**

除了建立加密隧道、加密虚拟网络，还可以直接使用SSL进行MySQL的访问加密。

2.3.1 SSL证书的生成

首先检查MySQL是否支持SSL。

```
mysql> SHOW VARIABLES LIKE ‘have_ssl’;

+—————+———-+ | Variable_name | Value

| +—————+———-+ | have_ssl      | DISABLED |

+—————+———-+ 1 row in set (0.00 sec)
```

如果输出如上，说明MySQL支持SSL但未启用。

SSL证书分多种类型，实际中要根据不同用途来使用服务端或客户端的证书。

```
[mysqld]

# 服务端类型SSL证书，用于服务端，或者主从关系中的主库

ssl-ca=/home/mysql/certs/ca-cert.pem ssl-cert=/home/mysql/certs/server-cert.pem

ssl-key=/home/mysql/certs/server-key.pem
```

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/5.jpg)

```
[client]

# 客户端类型SSL证书，用于客户端（如命令行工具），或者主从关系中的从库

ssl-ca=/home/mysql/certs/ca-cert.pem

ssl-cert=/home/mysql/certs/client-cert.pem

ssl-key=/home/mysql/certs/client-key.pem
```

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/6.jpg)

此外，为了方便统一管理，在同一台机器可以使用同时支持服务端和客户端类型的单一SSL证书。只需要生成SSL证书时指定两种类型的用法或者直接不指定任一种用法。

配置完毕后，检查下SSL是否已启用

mysql> SHOW VARIABLES LIKE ‘%ssl%’;

```
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

如果输出如上，说明SSL已正常启用

2.3.2 require SSL与require X509

为了确保外网访问的MySQL用户使用了SSL加密，在生成用户时可以强制要求REQUIRE SSL或REQUIRE X509：

```
mysql> CREATE USER ‘testuser’@’1.2.3.4’ IDENTIFIED BY ‘testpass’ REQUIRE SSL;

mysql> CREATE USER ‘testuser’@’1.2.3.4’ IDENTIFIED BY ‘testpass’ REQUIRE X509;
```

两者的区别在于，REQUIRE SSL只要求客户端使用指定ca证书对服务端证书进行验证，而REQUIRE X509还要求服务端对客户端证书进行验证。为了避免中间人攻击，确保更安全的通信，一般建议使用REQUIRE X509。

2.3.3 OpenSSL与yaSSL

MySQL可以使用自带的yaSSL库进行加密通信，也可以使用OpenSSL进行加密通信。具体使用哪种，需要在编译时指定WITH_SSL:STRING的参数：

```
bundled (use yassl), yes (prefer os library if present, otherwise use bundled), system

(use os library), </path/to/custom/installation>
```

为了更好的安全性，可以使用系统自带的OpenSSL，并及时做好yum/apt更新。

如果考虑不同版本的兼容性，那么建议使用自带的yaSSL。

比如OpenSSL曾针对CVE-2015-4000的漏洞将DH key的最小值提高到768 bits，而一些旧版本MySQL的DH key使用了512 bits。因为MySQL的默认SSL加密算法是DHE-RSA-AES256-SHA，如果使用了OpenSSL的MySQL，在不同版本间的访问可能会出现ERROR 2026的错误提示。

2.3.4 监听基于SSL的主从通信

配置了SSL加密之后，我们再次尝试抓取MySQL主从通信。

发现无法获取到MySQL主从的登录帐号：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/7.jpg)

此外截取到的MySQL主从数据也是乱码：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/8.jpg)

可以看到，在MySQL主从经过SSL加密的情况下，无法实现有效窃听。

**3 本地安全访问**

**3.1 SSH隧道**

一般我们都需要SSH方式从本地访问远程服务器，这时可以建立SSH隧道来访问远程服务器的特定端口。

如使用SecureCRT的端口转发功能（Putty也类似），将本地3306端口转发到服务器的3306端口：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/10.jpg)

如果习惯使用navicat这类工具，可以使用自带的SSH隧道功能（注意旧版可能要将私钥转换成ppk格式）：

![如何让远程访问Mysql更安全！如何让远程访问Mysql更安全！](https://www.linuxprobe.com/wp-content/uploads/2018/02/11.jpg)

**3.2 phpmyadmin+HTTPS**

如果习惯使用phpmyadmin的web方式访问MySQL，那么只需要将访问方式统一为HTTPS：

```
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

**4 总结**

MySQL的数据安全是一个非常大的课题，其中外网间的安全通信往往容易被忽略。而当前随着HTTPS /SMTPS/POP3S/IMAPS的逐步流行，各种基于TCP、UDP的加密通信方案也会越来越多地应用到线上业务中。本文针对服务器间/本地到服务器的一些访问MySQL的场景介绍了几种加密通信方案，希望能给到大家一些思路，并结合自己实际需要来使用MySQL的加密访问。

> 原文来自：<http://www.yunweipai.com/archives/18614.html>
>
> 本文地址：<https://www.linuxprobe.com/remote-access-mysql.html>
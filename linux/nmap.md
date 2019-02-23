# [nmap](https://nmap.org/man/zh/index.html)

知名的网络探测和安全扫描程序，是 Network Mapper 的简称。nmap 可以进行主机发现(Host Discovery)、端口扫描(Port Scanning)、版本侦测( Version Detection)、操作系统侦测(Operating System Detection), nmap 是网络管理员必用的软件之一。nmap 因为功能强大、跨平台、开源 、文档丰富等诸多优点，在安全领域使用非常广泛 。

```bash
apt-get install nmap
```

nmap 的使用非常灵活，功能又很强大，因此 nmap 有很多命令行选项 。使用 nmap 时，首先需要确定要对哪些主机进行扫描，然后确定怎么进行扫描(如使用何种技术，对哪些端口进行扫描)。

## 端口扫描

用于确定目标主机 TCP/UDP 端口的开放情况。

```bash
$ nmap 140.205.220.96
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-26 11:04 CST
Nmap scan report for 140.205.220.96
Host is up (0.049s latency).
Not shown: 998 filtered ports
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 5.69 seconds
```

### 端口扫描参数

- 端口扫描协议: T(TCP)、 U(UDP)、 S(SCTP)、 p(IP);
- 口端口扫描类型:- sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans ;
- 口扫描的端口号:-p 80,443 -p 80-160。

### 端口扫描状态

| 端口状态         | 状态含义                                  |
| ---------------- | ----------------------------------------- |
| open             | 端口是开放的                              |
| closed           | 端口是关闭的                              |
| filtered         | 端口被防火墙 IDS/IPS 屏蔽，无法确定其状态 |
| unfiltered       | 端口没有被屏蔽，但是否开放需要进一步确定  |
| open\|filtered   | 端口是开放的或被屏蔽                      |
| closed\|filtered | 端口是关闭的或被屏蔽                      |

### 端口扫描类型

- TCP SYNC SCAN :半开放扫描，这种类型的扫描为发送一个 SYN 包，启动一个 TCP 会话，并等待响应的数据包。如果收到的是一个 reset 包，表明端口是关闭的; 如果收到的是一个 SYNC/ACK 包，则表示端口是打开的。
- TCP NULL SCAN : NULL 扫描把 TCP 头中的所有标志位都设置为 NULL。如果收到的是一个 RST 包，则表示相应的端口是关闭的。
- TCP FIN SCAN : TCP FIN 扫描发送一个表示结束一个活跃的 TCP 连接的 FIN 包，让对方关闭连接。如果收到了一个 RST 包，则表示相应的端口是关闭的。
- TCP XMAS SCAN : TCP XMAS 扫描发送 PSH、 FIN、 URG 和 TCP 标志位被设置为 1 的数据包，如果收到一个 RST 包，则表示相应端口是关闭的。

nmap 具有非常灵活的方式指定需要扫描的主机，我们可以使用 nmap 命令的，sL 选项来进行测试。 `-sL`选项仅仅打印 IP 列表，不会进行任何操作。

```bash
nmap -sL 192.168.0.0/30
```

可以将 IP 地址保存到文件中，通过`-iL`选项读取文件中的 IP 地址。`nmap -iL ip.list`

## 主机发现

使用`-sP` 或`-sn` 选项可以告诉 nmap 不要进行端口扫描，仅仅判断主机是否可达。

```bash
$ nmap -sn 140.205.220.96
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-26 11:03 CST
Nmap scan report for 140.205.220.96
Host is up (0.11s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.21 seconds
```

## 版本检测

```bash
$ nmap -sV www.mycodon.com

Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-26 11:14 CST
Nmap scan report for www.mycodon.com (106.15.103.227)
Host is up (0.051s latency).
Not shown: 996 filtered ports
PORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
80/tcp open http nginx 1.14.0
443/tcp open ssl/http nginx 1.14.0
3306/tcp closed mysql
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.71 seconds
```

### 操作系统检测

```bash
$ sudo nmap -O www.mycodon.com
Password:
Starting Nmap 7.70 ( https://nmap.org ) at 2018-09-26 11:33 CST
Nmap scan report for www.mycodon.com (106.15.103.227)
Host is up (0.041s latency).
Not shown: 996 filtered ports
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https
3306/tcp closed mysql
Device type: general purpose|broadband router|firewall
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (92%), WatchGuard Fireware 11.X (86%), IPFire 2.X (86%)
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:2.6.32 cpe:/o:watchguard:fireware:11.8 cpe:/o:ipfire:ipfire:2.11
Aggressive OS guesses: Linux 3.11 - 4.1 (92%), Linux 4.4 (92%), Linux 3.16 (91%), Linux 3.10 - 3.16 (90%), Linux 3.13 (89%), Linux 2.6.32 (87%), Linux 4.0 (87%), Linux 3.10 - 3.12 (86%), Linux 3.2 - 3.8 (86%), Linux 3.8 (86%)
No exact OS matches for host (test conditions non-ideal).

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.27 seconds
```

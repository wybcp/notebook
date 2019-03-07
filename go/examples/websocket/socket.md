# socket

Socket 起源于 Unix，而 Unix 基本哲学之一就是“一切皆文件”，都可以用“打开 open –> 读写 write/read –> 关闭 close”模式来操作。Socket 就是该模式的一个实现，网络的 Socket 数据传输是一种特殊的 I/O，Socket 也是一种文件描述符。Socket 也具有一个类似于打开文件的函数调用：Socket()，该函数返回一个整型的 Socket 描述符，随后的连接建立、数据传输等操作都是通过该 Socket 实现的。

## 常用的 Socket 类型

流式 Socket（SOCK_STREAM）和数据报式 Socket（SOCK_DGRAM）。流式是一种面向连接的 Socket，针对于面向连接的 TCP 服务应用；数据报式 Socket 是一种无连接的 Socket，对应于无连接的 UDP 服务应用

唯一标识一个进程:

- 本地可以通过进程 PID 来唯一标识一个进程
- 利用三元组（ip 地址，协议，端口）标识网络的进程

## tcp

### TCPAddr

TCP 的地址信息

```go
type TCPAddr struct {
        IP   IP
        Port int
        Zone string // IPv6 scoped addressing zone; added in Go 1.1
}
```

通过 ResolveTCPAddr 获取一个 TCPAddr

```go
func ResolveTCPAddr(network, address string) (*TCPAddr, error)
```

- network:"tcp", "tcp4", "tcp6"分别表示 TCP(IPv4-only),TCP(IPv6-only)或者 TCP(IPv4,IPv6 的任意一个).
- address 表示域名或者 IP 地址

### TCPConn

```go
// TCPConn is an implementation of the Conn interface for TCP network
// connections.
type TCPConn struct {
	conn
}
```

在 Go 语言的 net 包中有一个类型 TCPConn，这个类型可以用来作为客户端和服务器端交互的通道，他有两个主要的函数：

```go
func (c *TCPConn) Write(b []byte) (int, error)
func (c *TCPConn) Read(b []byte) (int, error)
```

### 建立 tcp 连接

Go 语言中通过 net 包中的 DialTCP 函数来建立一个 TCP 连接，并返回一个 TCPConn 类型的对象，当连接建立时服务器端也创建一个同类型的对象，此时客户端和服务器段通过各自拥有的 TCPConn 对象来进行数据交换。一般而言，客户端通过 TCPConn 对象将请求信息发送到服务器端，读取服务器端响应的信息。服务器端读取并解析来自客户端的请求，并返回应答信息，这个连接只有当任一端关闭了连接之后才失效，不然这连接可以一直在使用。

```go
func DialTCP(network string, laddr, raddr *TCPAddr) (*TCPConn, error)
```

If laddr(local address) is nil, a local address is automatically chosen. If the IP field of raddr(remote address) is nil or an unspecified IP address, the local system is assumed.

#### 服务端

在服务器端我们需要绑定服务到指定的非激活端口，并监听此端口，当有客户端请求到达的时候可以接收到来自客户端连接的请求。net 包中有相应功能的函数，函数定义如下：

```go
func ListenTCP(net string, laddr *TCPAddr) (l *TCPListener, err os.Error)
func (l *TCPListener) Accept() (c Conn, err os.Error)
```

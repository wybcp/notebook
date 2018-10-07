# SSH

SSH (Secure Shell)是一种由 IETF 的网络工作小组制定、创建在应用层和传输层基础上的安全协议，为计算机上的 Shell 提供安全的传输和使用环境。

在 Linux 下广泛使用的是 OpenSSH，它是一款应用广泛的开源软件，实现 ssh 协议 。

## OpenSSH

OpenSSH ( OpenBSD Secure Shell)是 OpenBSD 的一个子项目，是 SSH 协议的开源实现。在服务端，OpenSSH 启动 sshd 守护进程，该进程默认监听 22 端口。客户端使用用户名和密码连接服务端。连接成功以后，OpenSSH 返回给用户一个 Shell，用户可以使用该 Shell 在远程服务器执行命令。

在生产环境中，为了防止黑客攻击，一般会修改 ssh 服务的默认端口号。修改 ssh 服务默认端口号，在/etc/ssh/sshd_config 中完成的。我们也可以通过该配置文件禁止用户使用密码进行认证，只能使用密钥认证。修改完配置文件以后，执行下面的命令重启 OpenSSH 的守护进程才能生效:`/etc/init.d/ssh restart`

### 上传公钥

密钥登录的原理也很简单，即事先将用户的公钥储存在远程服务器上(`~/.ssh/authorized_keys` 文件)。使用密钥登录时，远程服务器会向用户发送一段随机字符串，SSH 使用用户的私钥加密字符串后发送给远程服务器。远程服务器用事先储存的公钥进行解密 如果成功，就证明用户是可信的，直接允许登录 Shell，不再要求密码。

ssh-keygen 是用来生成密钥对的工具。

将公钥保存到远程服务器的`~/.ssh/authorized_key` 文件中。

```bash
ssh root@120.78.62.106 'mkdir -p .ssh && cat > .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```

OpenSSH 专门提供了一个名为 ssh-copy-id 的工具。我们可以使用该工具将公钥保存到远程服务器中， 这种方式比前面 Shell 脚本的方式更加方便。

```bash
ssh-copy-id -i ~ / .ssh/id_rsa.pub remote-host
```

使用私钥登录时需要注意，私钥文件与远程服务器中 authorized_keys 文件的权限都必须为 600，否则登录会出错。

### ssh-agent 管理私钥

在 Linux 下，直接执行 ssh-agent 命令启动 `ssh-agent` 即可。启动以后，使用 `ssh-add` 命令将私钥添加到 ssh-agent 中。

`ssh_add -L`命令查看哪些私钥

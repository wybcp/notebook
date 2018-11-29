# [machine](https://github.com/docker/machine)

在本地或者云环境中创建 Docker 主机。类似于ansible

Machine 项目主要由 Go 语言编写，用户可以在本地任意指定由 Machine 管理的 Docker 主机，并对其进行操作。

## 安装

```bash
root@iZwz97tbgo9lk6rm6lxu2wZ:~# base=https://github.com/docker/machine/releases/download/v0.15.0
root@iZwz97tbgo9lk6rm6lxu2wZ:~# curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/usr/local/bin/docker-machine
# 命令自动补全，安装补全脚本
root@iZwz97tbgo9lk6rm6lxu2wZ:~#base=https://raw.githubusercontent.com/docker/machine/v0.15.0
for i in docker-machine-prompt.bash docker-machine-wrapper.bash docker-machine.bash
do
  sudo wget "$base/contrib/completion/bash/${i}" -P /etc/bash_completion.d
done
```

# [操作系统](https://www.zhihu.com/pub/reader/119570839/chapter/1035129530792570880)

## [BusyBox](https://busybox.net/)

BusyBox 是一个集成了一百多个最常用 Linux 命令（如 cat、echo、grep、mount、telnet 等）的精简工具箱，它只有不到 2 MB 大小，被誉为「Linux 系统的瑞士军刀」。

## [Alpine](https://alpinelinux.org/)

Alpine 操作系统是一个面向安全的轻型 Linux 发行版，关注安全，性能和资源效能。不同于其他发行版，Alpine 采用了 musl libc 和 BusyBox 以减小系统的体积和运行时资源消耗，比 BusyBox 功能上更完善。在保持瘦身的同时，Alpine 还提供了包管理工具 apk 查询和安装软件包。

### apk 安装软件包工具

`$ apk add --no-cache <package>`
Alpine 中软件安装包的名字可能会与其他发行版有所不同，可以在 <https://pkgs.alpinelinux.org/packages> 网站搜索并确定安装包名称。如果需要的安装包不在主索引内，但是在测试或社区索引中。那么首先需要更新仓库列表，如下所示。
```
$ echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
$ apk --update add --no-cache <package>
```

```bash
$ docekr image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
busybox                     latest              59788edf1f3e        3 weeks ago         1.15MB
alpine                      latest              196d12cf6ab1        6 weeks ago         4.41MB
ubuntu                      latest              ea4c82dcd15a        5 days ago          85.8MB
debian                      latest              be2868bebaba        8 days ago          101MB
centos                      latest              75835a67d134        2 weeks ago         200MB
```

Docker 官方推荐使用 Alpine 作为默认的基础镜像环境，如镜像下载速度加快、镜像安全性提高、主机之间的切换更方便、占用更少磁盘空间等。

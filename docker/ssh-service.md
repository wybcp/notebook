# ssh 服务

```bash
$ docker run -it ubuntu:18.04 bash
root@cacfe86e695b:/# apt update
root@cacfe86e695b:/# apt-get install openssh-server
root@cacfe86e695b:/# mkdir -p /var/run/sshd
root@cacfe86e695b:/# /usr/sbin/sshd -D &
```

```Dockerfile
#设置继承镜像
FROM ubuntu:18.04
#提供一些作者的信息
MAINTAINER docker_user (user@docker.com)
RUN apt-get update
#安装 ssh 服务
RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN mkdir -p /root/.ssh
#取消pam限制
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
#复制配置文件到相应位置,并赋予脚本可执行权限
ADD authorized_keys /root/.ssh/authorized_keys
ADD run.sh /run.sh
RUN chmod 755 /run.sh
#开放端口
EXPOSE 22
#设置自启动命令
CMD ["/run.sh"]
```

`run.sh`

```shell
#!/bin/bash
/usr/sbin/sshd -D
```

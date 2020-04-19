# 安装

## macOS

macOS 操作系统上的安装目录：`/usr/local/mysql/`，`/etc/mysql/my.cnf`

## Ubuntu

[A Quick Guide to Using the MySQL APT Repository](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)

1. 添加[apt仓库](https://dev.mysql.com/downloads/repo/apt/)

    ```shell
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb
    ```

1. 安装`.deb`文件

    ```shell
    sudo dpkg -i mysql-apt-config_0.8.15-1_all.deb
    ```

1. 选择版本

   ```shell
   dpkg-reconfigure mysql-apt-config
   ```

1. 更新apt仓库信息

   ```shell
   apt update
   ```

1. 安装MySQL

   ```shell
   apt install -y mysql-community-server
   ```

## 卸载

检查现有的包：

```shell
dpkg -l | grep -i mysql
# 删除
sudo apt remove --purge mysql-* -y
apt autoremove -y
# 确认
dpkg -l | grep -i mysql
#rc表示已删除（c），只保留配置文件（c）
#
```

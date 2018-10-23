# [Docker 数据管理](https://docs.docker.com/storage/volumes/)

容器中的管理数据主要有两种方式：

- 数据卷（Data Volumes）：容器内数据直接映射到本地主机环境；
- 数据卷容器（Data Volume Containers）：使用特定容器维护数据卷。

## data valumes

数据卷（Data Volumes）是一个可供容器使用的特殊目录，它将主机操作系统目录直接映射进容器，类似于 Linux 中的 mount 行为。

优势：

- 数据卷可以在容器之间共享和重用，容器间传递数据将变得高效与方便；
- 对数据卷内数据的修改会立马生效，无论是容器内操作还是本地操作；
- 对数据卷的更新不会影响镜像，解耦开应用和数据；
- 卷会一直存在，直到没有容器使用，可以安全地卸载它。

### 创建数据卷

在本地创建一个数据卷：

```bash
$ docker volume create -d local test
test
```

此时，查看`/var/lib/docker/volumes` 路径下，会发现所创建的数据卷位置：

```bash
$ ls -l /var/lib/docker/volumes
metadata.db  test
$ docker volume ls
DRIVER              VOLUME NAME
local               test
$ docker volume inspect test
[
    {
        "CreatedAt": "2018-10-22T21:09:17+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/test/_data",
        "Name": "test",
        "Options": {},
        "Scope": "local"
    }
]
```

### 绑定数据卷

可以在创建容器时将主机本地的任意路径挂载到容器内作为数据卷，这种形式创建的数据卷称为绑定数据卷。

使用-mount 选项来使用数据卷,支持三种类型的数据卷，包括：

- volume：普通数据卷，映射到主机/var/lib/docker/volumes 路径下；
- bind：绑定数据卷，映射到主机指定路径下；
- tmpfs：临时数据卷，只存在于内存中。

```bash
$ docker run -d \
  --name devtest \
  --mount source=test,target=/app \
  ubuntu:18.04
```

本地目录的路径必须是绝对路径，容器内路径可以为相对路径。如果目录不存在，Docker 会自动创建。

Docker 挂载数据卷的默认权限是读写（rw），用户也可以通过 ro 指定为只读：

## 数据卷容器

如果用户需要在多个容器之间共享一些持续更新的数据，最简单的方式是使用数据卷容器，专门提供数据卷给其他容器挂载。

如果删除了挂载的容器，数据卷并不会被自动删除。如果要删除一个数据卷，必须在删除最后一个还挂载着它的容器时显式使用 `docker rm-v` 命令来指定同时删除关联的容器。
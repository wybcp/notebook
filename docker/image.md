# image 文件

**Docker 把应用程序及其依赖，打包在 image 文件里面。**只有通过这个文件，才能生成 Docker 容器。image 文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例。

对于 Linux 而言，内核启动后，会挂载 root 文件系统为其提供用户空间支持。而 Docker 镜像（Image），就相当于是一个 root 文件系统。

image 是二进制文件。实际开发中，一个 image 文件往往通过继承另一个 image 文件，加上一些个性化设置而生成。举例来说，你可以在 Ubuntu 的 image 基础上，往里面加入 Apache 服务器，形成你的 image。

```bash
# 列出本机的所有 image 文件。
$ docker image ls
# or
$ docker images
# images 子命令的选项
#·-a，--all=true|false：列出所有（包括临时文件）镜像文件，默认为否；
#·--digests=true|false：列出镜像的数字摘要值，默认为否；
#·-f，--filter=[]：过滤列出的镜像，如dangling=true只显示没有被使用的镜像；也可指定带有特定标注的镜像等；
#·--format="TEMPLATE"：控制输出格式，如.ID代表ID信息，.Repository代表仓库信息等；
#·--no-trunc=true|false：对输出结果中太长的部分是否进行截断，如镜像的ID信息，默认为是；
#·-q，--quiet=true|false：仅输出ID信息，默认为否。


# 删除 image 文件
$ docker image rm [imageName]
```

image 文件是通用的，一台机器的 image 文件拷贝到另一台机器，照样可以使用。一般来说，为了节省时间，我们应该尽量使用别人制作好的 image 文件，而不是自己制作。即使要定制，也应该基于别人的 image 文件进行加工，而不是从零开始制作。

为了方便共享，image 文件制作完成后，可以上传到网上的仓库。Docker 的官方仓库 [Docker Hub](https://hub.docker.com/) 是最重要、最常用的 image 仓库。此外，出售自己制作的 image 文件也是可以的。

## 分层存储

因为镜像包含操作系统完整的 root 文件系统，其体积往往是庞大的，因此在 Docker 设计时，就充分利用 Union FS 的技术，将其设计为分层存储的架构。所以严格来说，镜像并非是像一个 ISO 那样的打包文件，镜像只是一个虚拟的概念，其实际体现并非由一个文件组成，由多层文件系统联合组成。

镜像构建时，会一层层构建，前一层是后一层的基础。每一层构建完就不会再发生改变，后一层上的任何改变只发生在自己这一层。因此，在构建镜像的时候，需要额外小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。

6c953ac5d795 这样的字符串是层的唯一 id（实际上完整的 id 包括 256 比特，64 个十六进制字符组成）。

分层存储的特征还使得镜像的复用、定制变得更为容易。甚至可以用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。

## 获取镜像

`docker pull NAME[:TAG]`

- NAME：镜像仓库的名称
- TAG：镜像的标签（通常表示版本信息）
- -a，--all-tags=true|false：是否获取仓库中的所有镜像，默认为否；
- --disable-content-trust：取消镜像的内容校验，默认为真。

如果不显式指定 TAG，则默认会选择 latest 标签，这会下载仓库中最新版本的镜像。

`docker tag`命令来为本地镜像任意添加新的标签，类似链接的作用。

## [查看 image 的具体信息](https://docs.docker.com/engine/reference/commandline/inspect/)

`docker inspect [OPTIONS] NAME|ID [NAME|ID...]`返回的是一个 JSON 格式的消息，包括制作者、适应架构、各层的数字摘要等

## [查看 image 的历史信息](https://docs.docker.com/engine/reference/commandline/history/)

`docker history [OPTIONS] IMAGE` 列出各层的创建信息。

## [搜寻镜像](https://docs.docker.com/engine/reference/commandline/search/)

`docker search [OPTIONS] TERM`搜索 Docker Hub 官方仓库中的镜像。

- ·-f，--filter filter：过滤输出内容；
- ·--format string：格式化输出内容；
- ·--limit int：限制输出结果个数，默认为 25 个；
- ·--no-trunc：不截断输出结果。

## [删除镜像](https://docs.docker.com/engine/reference/commandline/rmi/)

`docker rmi [OPTIONS] IMAGE [IMAGE...]`使用标签删除镜像，其中 IMAGE 可以为标签或 ID。

- ·-f，-force：强制删除镜像，即使有容器依赖它；
- ·-no-prune：不要清理未带标签的父镜像。

## 清理镜像

`docker image prune` 命令来进行清理。

- ·-a，-all：删除所有无用镜像，不光是临时镜像；

- ·-filter filter：只清理符合给定过滤器的镜像；

- ·-f，-force：强制删除镜像，而不进行提示确认。

## 创建镜像

### 基于已有容器创建

`docker[container]commit[OPTIONS]CONTAINER[REPOSITORY[：TAG]]`

- ·-a，--author=「」：作者信息；

- ·-c，--change=[]：提交的时候执行 Dockerfile 指令，包括 CMD|ENTRYPOINT|ENV|EXPOSE|LABEL|ONBUILD|USER|VOLUME|WORKDIR 等；

- ·-m，--message=「」：提交消息；

- ·-p，--pause=true：提交时暂停容器运行。

## [保存镜像](https://docs.docker.com/engine/reference/commandline/save/)

`docker save [OPTIONS] IMAGE [IMAGE...]`

- --output , -o：导出镜像到指定的文件中

`docker save -o ubuntu_18.04.tar ubuntu:18.04`

## [载入镜像](https://docs.docker.com/engine/reference/commandline/load/)

`docker load [OPTIONS]`可以将导出的 tar 文件再导入到本地镜像库。

- -i、-input string 选项，从指定文件中读入镜像内容。

`docker load -i ubuntu_18.04.tar`

## [上传镜像](https://docs.docker.com/engine/reference/commandline/push/)

`docker push [OPTIONS] NAME[:TAG]`上传镜像到仓库

[关于 Docker 镜像的操作，看完这篇就够啦 !（上）](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247483734&idx=1&sn=f8355c8fb41be191934bdeeedc09097e&chksm=fd54d1d0ca2358c67c49a1c61895982dca43d732f9dd11839200987e62546a904cedb19e1057&scene=21#wechat_redirect)

[关于 Docker 镜像的操作，看完这篇就够啦 !（下）| 文末福利](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ%3D%3D&mid=2247483740&idx=1&sn=a43b68937f795774809af07539e38292&chksm=fd54d1daca2358ccb582c1a0e2e86b0ca02180e06c61d8375ddde8d6cee095b9874e143c5285&token=1865589019&lang=zh_CN)

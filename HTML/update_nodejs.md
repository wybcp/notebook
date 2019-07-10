# update node.js

引用[Windows/Linux 下 Node 更新](http://mp.weixin.qq.com/s?src=3&timestamp=1464871223&ver=1&signature=M7kiAJ69wjYck5vlMU0Ktv3VxxY5PtQiUER8yZHFIvh-4uT*kOwoVUqkdFYY9kNb7SeIyaPiCcRnD2Jb4bYCJ3-FOqcqQWpCnOgf19BtxV*AhVSmQxHlph8MxUN6esGi30UYfcSvMw20uOlEQQT5eyca7aIg7OuXpxfZNnJQcVM=)

## 关于 node 版本号

江湖人称版本帝，release 如下：

| 版本号          | release date      |
| --------------- | ----------------- |
| latest/         | 05-Apr-2016 23:31 |
| latest-argon/   | 01-Apr-2016 01:39 |
| latest-v0.10.x/ | 01-Apr-2016 04:31 |
| latest-v0.12.x/ | 01-Apr-2016 00:10 |
| latest-v4.x/    | 01-Apr-2016 01:39 |
| latest-v5.x/    | 05-Apr-2016 23:31 |

因为 node 在 v0.x 的时候，出现了另一个分支：io.js，其版本号从 v1.0.0 开始后来更新到 v4.x，而此时 node 本体是 v0.12.x，然后本体与 io.js 合体出现了 v4.0，再经过一段时间的更新后推出了代号（codename）为 argon 的 LTS（Long-term Support，长期支持版本），即 v4.x，有点冒险的新特性不能放在 LTS 里，但新特性的开发还得继续，就出现了 v5.x，即 Stable

所以：

| 版本号          | notes                                                     |
| --------------- | --------------------------------------------------------- |
| latest/         | 表示 latest Stable release，比 LTS 新一些，不建议线上使用 |
| latest-argon/   | 表示代号为 argon 的 LTS，可以在线上使用                   |
| latest-v0.10.x/ | 历史痕迹，偶数稳定，奇数不稳定                            |
| latest-v0.12.x/ | 同上                                                      |
| latest-v4.x/    | 合体后的各个版本                                          |
| latest-v5.x/    | Stable，比 LTS 新一些，不建议线上使用                     |

LTS 表示长期支持版本，更注重稳定性和安全性，适合线上使用。至于 Stable，其实不像名字那样稳定，6 个月后进化成 LTS，然后 LTS 的保质期是 30 个月。至于 Nightly 版本。。。能有什么用啊

P.S.关于 Node 版本的更多信息，请查看 nodejs/node

## Windows 更新 Node

windows 下安装 Node 一般选择 Windows Installer (.msi)或者 Windows Binary (.exe)，更新的方式就是覆盖安装：直接下载目标版本的 msi 或者 exe，在原安装目录覆盖安装即可

## Linux 更新 Node

linux 下一般选择手动编译源码安装，npm 有开源模块提供了版本管理工具：n，先全局安装（npm install -g n），然后直接： `n lts` 就可以安装最新的 LTS 了，但笔者今天遇到了奇怪错误，最后直接安装了 Stable，其它可能有用的命令如下：

    n latest #安装最新版本
    n stable #安装最新稳定版本
    n #查看已通过n安装的各个版本
    n rm 0.9.4 #移除0.9.4版本

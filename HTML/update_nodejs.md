# update node.js
引用[Windows/Linux下Node更新](http://mp.weixin.qq.com/s?src=3&timestamp=1464871223&ver=1&signature=M7kiAJ69wjYck5vlMU0Ktv3VxxY5PtQiUER8yZHFIvh-4uT*kOwoVUqkdFYY9kNb7SeIyaPiCcRnD2Jb4bYCJ3-FOqcqQWpCnOgf19BtxV*AhVSmQxHlph8MxUN6esGi30UYfcSvMw20uOlEQQT5eyca7aIg7OuXpxfZNnJQcVM=)

##关于node版本号

江湖人称版本帝，release如下：

|版本号 | release date |
| -- | -- |
|  latest/                         |                 05-Apr-2016 23:31                   
| latest-argon/                                  |    01-Apr-2016 01:39                  
|latest-v0.10.x/                                 |   01-Apr-2016 04:31                  
|latest-v0.12.x/                                |    01-Apr-2016 00:10                   
|latest-v4.x/                                   |    01-Apr-2016 01:39                   
|latest-v5.x/                        |               05-Apr-2016 23:31                  


因为node在v0.x的时候，出现了另一个分支：io.js，其版本号从v1.0.0开始后来更新到v4.x，而此时node本体是v0.12.x，然后本体与io.js合体出现了v4.0，再经过一段时间的更新后推出了代号（codename）为argon的LTS（Long-term Support，长期支持版本），即v4.x，有点冒险的新特性不能放在LTS里，但新特性的开发还得继续，就出现了v5.x，即Stable

所以：

|版本号|notes|
|--|--|
|latest/       | 表示latest Stable release，比LTS新一些，不建议线上使用
|latest-argon/   |表示代号为argon的LTS，可以在线上使用
|latest-v0.10.x/ |历史痕迹，偶数稳定，奇数不稳定
|latest-v0.12.x/ |同上
|latest-v4.x/    |合体后的各个版本
|latest-v5.x/    |Stable，比LTS新一些，不建议线上使用

LTS表示长期支持版本，更注重稳定性和安全性，适合线上使用。至于Stable，其实不像名字那样稳定，6个月后进化成LTS，然后LTS的保质期是30个月。至于Nightly版本。。。能有什么用啊

P.S.关于Node版本的更多信息，请查看nodejs/node

二.Windows更新Node

windows下安装Node一般选择Windows Installer (.msi)或者Windows Binary (.exe)，更新的方式就是覆盖安装：直接下载目标版本的msi或者exe，在原安装目录覆盖安装即可

三.Linux更新Node

linux下一般选择手动编译源码安装，npm有开源模块提供了版本管理工具：n，先全局安装（npm install -g n），然后直接：

n lts

就可以安装最新的LTS了，但笔者今天遇到了奇怪错误，最后直接安装了Stable，其它可能有用的命令如下：
```
n latest #安装最新版本
n stable #安装最新稳定版本
n #查看已通过n安装的各个版本
n rm 0.9.4 #移除0.9.4版本```
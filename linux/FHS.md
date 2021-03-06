# Filesystem Hierarchy Standard （FHS）标准

Linux 目录配置的依据

<https://www.kancloud.cn/wizardforcel/vbird-linux-basic-4e/152235>

## 目录树架构

- / （root, 根目录）：与开机系统有关；
- /usr （unix software resource）：与软件安装/执行有关；
- /var （variable）：与系统运行过程有关。

### 根目录 （/）

根目录是整个系统最重要的一个目录，因为不但所有的目录都是由根目录衍生出来的，同时根目录也与开机/还原/系统修复等动作有关。 由于系统开机时需要特定的开机软件、核心文件、开机所需程序、函数库等等文件数据，若系统出现错误时，根目录也必须要包含有能够修复文件系统的程序才行。

FHS 标准建议：根目录（/）所在分区应该越小越好， 且应用程序所安装的软件最好不要与根目录放在同一个分区内，保持根目录越小越好。 如此不但性能较佳，根目录所在的文件系统也较不容易发生问题。

### /usr 的意义与内容

usr 是 Unix Software Resource 的缩写

### /var 的意义与内容

如果/usr 是安装时会占用较大硬盘容量的目录，那么/var 就是在系统运行后才会渐渐占用硬盘容量的目录。 因为/var 目录主要针对常态性变动的文件，包括高速缓存（cache）、登录文件（log file）以及某些软件运行所产生的文件， 包括程序文件（lock file, run file），或者例如 MySQL 数据库的文件等等。

### 绝对路径与相对路径

路径（path）定义为绝对路径（absolute）与相对路径（relative）。

- 绝对路径：由根目录（/）开始写起的文件名或目录名称；
- 相对路径：相对于目前路径的文件名写法。反正开头不是 / 就属于相对路径的写法

特别注意这两个特殊的目录：

- . ：代表当前的目录，也可以使用 ./ 来表示；
- .. ：代表上一层目录，也可以 ../ 来代表。

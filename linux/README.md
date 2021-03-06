# linux

## 目录

- [操作系统概述](https://github.com/xianyunyh/PHP-Interview/tree/master/Linux#%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%A6%82%E8%BF%B0)
- [Linux 历史](https://github.com/xianyunyh/PHP-Interview/tree/master/Linux#gnu%E5%92%8Cgpl)
- [Linux 基本命令](https://github.com/xianyunyh/PHP-Interview/blob/master/Linux/Linux%E5%91%BD%E4%BB%A4.md)
- [Linux(磁盘网络相关命令)](https://github.com/xianyunyh/PHP-Interview/blob/master/Linux/Linux%E5%91%BD%E4%BB%A42.md)
- [Crontab 计划任务](https://github.com/xianyunyh/PHP-Interview/blob/master/Linux/crontab.md)
- [shell](https://github.com/xianyunyh/PHP-Interview/blob/master/Linux/shell.md)

- [AWK 命令](https://github.com/xianyunyh/PHP-Interview/blob/master/Linux/AWK%E7%BB%83%E4%B9%A0.md)
- [SED 命令](https://github.com/xianyunyh/PHP-Interview/blob/master/Linux/Sed%E7%BB%83%E4%B9%A0.md)

## 操作系统概述

操作系统，英文名称 Operating System，简称 OS，是计算机系统中必不可少的基础系统软件，它是应用程序运行以及用户操作必备的基础环境支撑，是计算机系统的核心。

操作系统的作用是管理和控制计算机系统中的硬件和软件资源，例如，它负责直接管理计算机系统的各种硬件资源，如对 CPU、内存、磁盘等的管理，同时对系统资源所需的优先次序进行管理。操作系统还可以控制设备的输入、输出以及操作网络与管理文件系统等事务。同时，它也负责对计算机系统中各类软件资源的管理。例如各类应用软件的安装、设置运行环境等。操作系统与计算机硬件软件关系图如下。

![img](https://images2015.cnblogs.com/blog/1066162/201611/1066162-20161130112310443-1027054412.png)

## Linux 和 Unix

Unix 系统于 1969 年在 AT&T 的贝尔实验室诞生，20 世纪 70 年代，它逐步盛行，这期间，又产生了一个比较重要的分支，就是大约 1977 年诞生的 BSD（Berkeley Software Distribution）系统。从 BSD 系统开始，各大厂商及商业公司开始了根据自身公司的硬件架构，并以 BSD 系统为基础进行 Unix 系统的研发，从而产生了各种版本的 Unix 系统.

70 年代中后期，由于各厂商和商业公司开发的 Unix 及内置软件都是针对自己公司特定的硬件，因此在其他公司的硬件上基本无法直接运行，而且当时没有人对开发基于 x86 架构的 CPU 的系统感兴趣。另外，70 年代末，Unix 又面临了突如其来的被 AT&T 回收版权的重大问题，特别是要求禁止对学生群体提供 Unix 系统源代码，这样的问题一度引起了当时 Unix 业界的恐慌，也因此产生了商业纠纷。

Linux 系统的诞生开始于 1991 年芬兰赫尔辛基大学的一位计算机系的学生，名字为**Linus Torvalds**。在大学期间，他接触到了学校的 Unix 系统，但是当时的 Unix 系统仅为一台主机，且对应了多个终端，使用时存在操作等待时间很长等一些不爽的问题，无法满足年轻的 Linus Torvalds 的使用需求。因此他就萌生了自己开发一个 Unix 的想法，于是不久，他就找到了前文提到的谭邦宁教授开发的用于教学的 Minix 操作系统，他把 Minix 安装到了他的 I386 个人计算机上。此后，Torvalds 又开始陆续阅读了 Minix 系统的源代码，从 Minix 系统中学到了很多重要的系统核心程序设计理念和设计思想，从而逐步开始了 Linux 系统雏形的设计和开发。

## GNU 和 GPL

GNU 的全称为**GNU's not unix**，意思是"GNU 不是 UNIX"，GNU 计划，又称革奴计划，是由 Richard Stallman 在 1984 年公开发起的，是 FSF 的主要项目。这个项目的目标是建立一套完全自由的和可移植的类 Unix 操作系统。

​ GNU 类 Unix 操作系统是由一系列应用程序、系统库和开发工具构成的软件集合，例如：Emacs 编辑软件、gcc 编译软件、bash 命令解释程序和编程语言，以及 gawk（GNU's awk）等，并加上了用于资源分配和硬件管理的内核。

​ 到 1991 年 Linux 内核发布的时候，GNU 项目已经完成了除系统内核之外的各种必备软件的开发。在 Linux Torvalds 和其他开发人员的努力下，GNU 项目的部分组件又运行到了 Linux 内核之上，例如：GNU 项目里的 Emacs、gcc、bash、gawk 等，至今都是 Linux 系统中很重要的基础软件。所以 linux 又叫**GNU/Linux**

GPL 全称为 General Public License，中文名为通用公共许可，是一个最著名的开源许可协议，开源社区最著名的 Linux 内核就是在 GPL 许可下发布的。GPL 许可是由自由软件基金会（Free Software foundation）创建的。

- ~ 符号代表的是“使用者的主文件夹”
- 提示字符方面，在 Linux 当中，默认 root 的提示字符为 # ，而一般身份使用者的提示字符为 $ 。

## Linux远程桌面连接

[VNC_Viewer](http://www.tightvnc.com/download/1.3.10/tightvnc-1.3.10_x86_viewer.zip?spm=5176.10731542.0.0.21ed7c8e6MdXr4&file=tightvnc-1.3.10_x86_viewer.zip)

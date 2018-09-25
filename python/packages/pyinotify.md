# pyinotify

一个 Python 模块，用来监测文件系统的变化。

pyinotify 依赖于 Linux 内核 inotify 功能。inotify 是一个事件驱动的通知器，其通知接口从内核空间到用户空间通过三个系统调用。 pyinotify 结合这些系统调用，并提供一个顶级的抽象和一个通用的方式来处理这些功能。

pyinotify 依赖 Linux 的 inotify 功能，而 Linux 在 2.6.13 版本以后才提供了 inotify。因此，pyinotify 需要在 Linux2.6.13 或更高版本的 Linux 系统上运行。

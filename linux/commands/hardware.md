# 磁盘管理

## lsblk

列出系统上的所有磁盘列表“ list block device ”的缩写

    [root@study ~]# lsblk [-dfimpt] [device]
    选项与参数：
    -d  ：仅列出磁盘本身，并不会列出该磁盘的分区数据
    -f  ：同时列出该磁盘内的文件系统名称
    -i  ：使用 ASCII 的线段输出，不要使用复杂的编码 （再某些环境下很有用）
    -m  ：同时输出该设备在 /dev 下面的权限数据 （rwx 的数据）
    -p  ：列出该设备的完整文件名！而不是仅列出最后的名字而已。
    -t  ：列出该磁盘设备的详细数据，包括磁盘伫列机制、预读写的数据量大小等

## blkid

列出设备的 UUID 等参数, UUID 是全域单一识别码 （universally unique identifier），Linux 会将系统内所有的设备都给予一个独一无二的识别码

## parted

列出磁盘的分区表类型与分区信息

`parted device_name print`

范例一：列出 /dev/vda 磁盘的相关数据

```bash
parted /dev/vda print
```

## 磁盘分区

MBR 分区表请使用 fdisk 分区， GPT 分区表请使用 gdisk 分区

要通过 lsblk 或 blkid 先找到磁盘，再用 parted /dev/xxx print 来找出内部的分区表类型，之后才用 gdisk 或 fdisk 来操作系统。

## 磁盘格式化

make filesystem, mkfs

## 文件系统检验

### xfs_repair

处理 XFS 文件系统

    [root@study ~]# xfs_repair [-fnd] 设备名称
    选项与参数：
    -f  ：后面的设备其实是个文件而不是实体设备
    -n  ：单纯检查并不修改文件系统的任何数据 （检查而已）
    -d  ：通常用在单人维护模式下面，针对根目录 （/） 进行检查与修复的动作！很危险！不要随便使用

    范例：检查一下刚刚创建的 /dev/vda4 文件系统
    [root@study ~]# xfs_repair /dev/vda4
    Phase 1 - find and verify superblock...
    Phase 2 - using internal log
    Phase 3 - for each AG...
    Phase 4 - check for duplicate blocks...
    Phase 5 - rebuild AG headers and trees...
    Phase 6 - check inode connectivity...
    Phase 7 - verify and correct link counts...
    done
    # 共有 7 个重要的检查流程！详细的流程介绍可以 man xfs_repair 即可！

    范例：检查一下系统原本就有的 /dev/centos/home 文件系统
    [root@study ~]# xfs_repair /dev/centos/home
    xfs_repair: /dev/centos/home contains a mounted filesystem
    xfs_repair: /dev/centos/home contains a mounted and writable filesystem

    fatal error -- couldn't initialize XFS library

xfs_repair 可以检查/修复文件系统，不过，因为修复文件系统是个很庞大的任务！因此，修复时该文件系统不能被挂载！ 若可以卸载，卸载后再处理即可。

### fsck.ext4

处理 EXT4 文件系统 [root@study ~]# fsck.ext4 [-pf][-b superblock] 设备名称选项与参数： -p ：当文件系统在修复时，若有需要回复 y 的动作时，自动回复 y 来继续进行修复动作。 -f ：强制检查！一般来说，如果 fsck 没有发现任何 unclean 的旗标，不会主动进入细部检查的，如果您想要强制 fsck 进入细部检查，就得加上 -f 旗标啰！ -D ：针对文件系统下的目录进行最优化配置。 -b ：后面接 superblock 的位置！一般来说这个选项用不到。但是如果你的 superblock 因故损毁时，通过这个参数即可利用文件系统内备份的 superblock 来尝试救援。一般来说，superblock 备份在： 1K block 放在 8193, 2K block 放在 16384, 4K block 放在 32768

## 文件系统挂载与卸载

    [root@study ~]# mount -a
    [root@study ~]# mount [-l]
    [root@study ~]# mount [-t 文件系统] LABEL='' 挂载点
    [root@study ~]# mount [-t 文件系统] UUID='' 挂载点 # 鸟哥近期建议用这种方式喔！
    [root@study ~]# mount [-t 文件系统] 设备文件名 挂载点选项与参数：
    -a ：依照配置文件 [/etc/fstab](../Text/index.html#fstab) 的数据将所有未挂载的磁盘都挂载上来
    -l ：单纯的输入 mount 会显示目前挂载的信息。加上 -l 可增列 Label 名称！
    -t ：可以加上文件系统种类来指定欲挂载的类型。常见的 Linux 支持类型有：xfs, ext3, ext4, reiserfs, vfat, iso9660（光盘格式）, nfs, cifs, smbfs （后三种为网络文件系统类型）
    -n ：在默认的情况下，系统会将实际挂载的情况实时写入 /etc/mtab 中，以利其他程序的运行。但在某些情况下（例如单人维护模式）为了避免问题会刻意不写入。此时就得要使用 -n 选项。
    -o ：后面可以接一些挂载时额外加上的参数！比方说帐号、密码、读写权限等：

- async, sync: 此文件系统是否使用同步写入 （sync） 或非同步 （async） 的 内存机制，请参考[文件系统运行方式](../Text/index.html#harddisk-filerun)。默认为 async。
- atime,noatime: 是否修订文件的读取时间（atime）。为了性能，某些时刻可使用 noatime ro,
- rw: 挂载文件系统成为只读（ro） 或可读写（rw）
- auto, noauto: 允许此 filesystem 被以 mount -a 自动挂载（auto） dev,
- nodev: 是否允许此 filesystem 上，可创建设备文件？ dev 为可允许 suid,
- nosuid: 是否允许此 filesystem 含有 suid/sgid 的文件格式？
- exec, noexec: 是否允许此 filesystem 上拥有可执行 binary 文件？
- user, nouser: 是否允许此 filesystem 让任何使用者执行 mount ？一般来说， mount 仅有 root 可以进行，但下达 user 参数，则可让一般 user 也能够对此 partition 进行 mount 。
- defaults: 默认值为：rw, suid, dev, exec, auto, nouser, and async remount: 重新挂载，这在系统出错，或重新更新参数时，很有用！

### umount

（将设备文件卸载） [root@study ~]# umount [-fn] 设备文件名或挂载点选项与参数： -f ：强制卸载！可用在类似网络文件系统 （NFS） 无法读取到的情况下； -l ：立刻卸载文件系统，比 -f 还强！ -n ：不更新 /etc/mtab 情况下卸载。

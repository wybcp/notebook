## Linux 系统常见的压缩指令
    *.Z         compress 程序压缩的文件；
    *.zip       zip 程序压缩的文件；
    *.gz        gzip 程序压缩的文件；
    *.bz2       bzip2 程序压缩的文件；
    *.xz        xz 程序压缩的文件；
    *.tar       tar 程序打包的数据，并没有压缩过；
    *.tar.gz    tar 程序打包的文件，其中并且经过 gzip 的压缩
    *.tar.bz2   tar 程序打包的文件，其中并且经过 bzip2 的压缩
    *.tar.xz    tar 程序打包的文件，其中并且经过 xz 的压缩
### gzip, zcat/zmore/zless/zgrep
gzip 应用度最广的压缩指令

    [dmtsai@study ~]$ gzip [-cdtv#] 文件名
    [dmtsai@study ~]$ zcat 文件名.gz
    选项与参数：
    -c  ：将压缩的数据输出到屏幕上，可通过数据流重导向来处理；
    -d  ：解压缩的参数；
    -t  ：可以用来检验一个压缩文件的一致性～看看文件有无错误；
    -v  ：可以显示出原文件/压缩文件的压缩比等信息；
    -#  ：# 为数字的意思，代表压缩等级，-1 最快，但是压缩比最差、-9 最慢，但是压缩比最好！默认是 -6
### bzip2, bzcat/bzmore/bzless/bzgrep
gzip 是为了取代 compress 并提供更好的压缩比而成立的，那么 bzip2 则是为了取代 gzip 并提供更佳的压缩比而来的

    [dmtsai@study ~]$ bzip2 [-cdkzv#] 文件名
    [dmtsai@study ~]$ bzcat 文件名.bz2
    选项与参数：
    -c  ：将压缩的过程产生的数据输出到屏幕上！
    -d  ：解压缩的参数
    -k  ：保留原始文件，而不会删除原始的文件喔！
    -z  ：压缩的参数 （默认值，可以不加）
    -v  ：可以显示出原文件/压缩文件的压缩比等信息；
    -#  ：与 gzip 同样的，都是在计算压缩比的参数， -9 最佳， -1 最快！
    
    范例一：将刚刚 gzip 范例留下来的 /tmp/services 以 bzip2 压缩
    [dmtsai@study tmp]$ bzip2 -v services
      services:  5.409:1,  1.479 bits/Byte, 81.51% saved, 670293 in, 123932 out.
    [dmtsai@study tmp]$ ls -l services*
    -rw-r--r--. 1 dmtsai dmtsai 123932 Jun 30 18:40 services.bz2
    -rw-rw-r--. 1 dmtsai dmtsai 135489 Jun 30 18:46 services.gz
    # 此时 services 会变成 services.bz2 之外，你也可以发现 bzip2 的压缩比要较 gzip 好喔！！
    # 压缩率由 gzip 的 79% 提升到 bzip2 的 81% 哩！
    
    范例二：将范例一的文件内容读出来！
    [dmtsai@study tmp]$ bzcat services.bz2
    
    范例三：将范例一的文件解压缩
    [dmtsai@study tmp]$ bzip2 -d services.bz2
    
    范例四：将范例三解开的 services 用最佳的压缩比压缩，并保留原本的文件
    [dmtsai@study tmp]$ bzip2 -9 -c services &gt; services.bz2

### xz, xzcat/xzmore/xzless/xzgrep

xz 这个压缩比更高

    [dmtsai@study ~]$ xz [-dtlkc#] 文件名
    [dmtsai@study ~]$ xcat 文件名.xz
    选项与参数：
    -d  ：就是解压缩啊！
    -t  ：测试压缩文件的完整性，看有没有错误
    -l  ：列出压缩文件的相关信息
    -k  ：保留原本的文件不删除～
    -c  ：同样的，就是将数据由屏幕上输出的意思！
    -#  ：同样的，也有较佳的压缩比的意思！
## 打包指令： tar

    将多个文件或目录包成一个大文件的指令功能，是一种“打包指令”啦！
    
    [dmtsai@study ~]$ tar [-z&#124;-j&#124;-J] [cv] [-f 待创建的新文件名] filename... &lt;==打包与压缩
    [dmtsai@study ~]$ tar [-z&#124;-j&#124;-J] [tv] [-f 既有的 tar文件名]             &lt;==察看文件名
    [dmtsai@study ~]$ tar [-z&#124;-j&#124;-J] [xv] [-f 既有的 tar文件名] [-C 目录]   &lt;==解压缩
    选项与参数：
    -c  ：创建打包文件，可搭配 -v 来察看过程中被打包的文件名（filename）
    -t  ：察看打包文件的内容含有哪些文件名，重点在察看“文件名”就是了；
    -x  ：解打包或解压缩的功能，可以搭配 -C （大写） 在特定目录解开
          特别留意的是， -c, -t, -x 不可同时出现在一串命令行中。
    -z  ：通过 gzip  的支持进行压缩/解压缩：此时文件名最好为 *.tar.gz
    -j  ：通过 bzip2 的支持进行压缩/解压缩：此时文件名最好为 *.tar.bz2
    -J  ：通过 xz    的支持进行压缩/解压缩：此时文件名最好为 *.tar.xz
          特别留意， -z, -j, -J 不可以同时出现在一串命令行中
    -v  ：在压缩/解压缩的过程中，将正在处理的文件名显示出来！
    -f filename：-f 后面要立刻接要被处理的文件名！建议 -f 单独写一个选项啰！（比较不会忘记）
    -C 目录    ：这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项。
    
    其他后续练习会使用到的选项介绍：
    -p（小写） ：保留备份数据的原本权限与属性，常用于备份（-c）重要的配置文件
    -P（大写） ：保留绝对路径，亦即允许备份数据中含有根目录存在之意；
    --exclude=FILE：在压缩的过程中，不要将 FILE 打包！ 
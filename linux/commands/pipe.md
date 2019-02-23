# 管线命令（pipe）

使用的是“ | ”界定符号！

管线后面接的第一个数据必定是“指令”！而且这个指令必须要能够接受 standard input 的数据，这样的指令才可以是为“管线命令”，例如 less, more, head, tail 等

## 选取命令

将一段数据经过分析后，取出我们所想要的。

### cut

    [dmtsai@study ~]$ cut -d'分隔字符' -f fields ==用于有特定分隔字符
    [dmtsai@study ~]$ cut -c 字符区间            ==用于排列整齐的讯息
    选项与参数：
    -d  ：后面接分隔字符。与 -f 一起使用；
    -f  ：依据 -d 的分隔字符将一段讯息分区成为数段，用 -f 取出第几段的意思；
    -c  ：以字符 （characters） 的单位取出固定字符区间；
    [dmtsai@study ~]$ echo ${PATH} | cut -d ':' -f 3,5

cut 主要的用途在于将“同一行里面的数据进行分解！”最常使用在分析一些数据或文字数据的时候！

### grep

    [dmtsai@study ~]$ grep [-acinv] [--color=auto] '搜寻字串' filename
    选项与参数：
    -a ：将 binary 文件以 text 文件的方式搜寻数据
    -c ：计算找到 '搜寻字串' 的次数
    -i ：忽略大小写的不同，所以大小写视为相同
    -n ：顺便输出行号
    -v ：反向选择，亦即显示出没有 '搜寻字串' 内容的那一行！
    --color=auto ：可以将找到的关键字部分加上颜色的显示喔！

    范例一：将 last 当中，有出现 root 的那一行就取出来；
    [dmtsai@study ~]$ last | grep 'root'

## 排序命令

### sort

    [dmtsai@study ~]$ sort [-fbMnrtuk] [file or stdin]
    选项与参数：
    -f  ：忽略大小写的差异，例如 A 与 a 视为编码相同；
    -b  ：忽略最前面的空白字符部分；
    -M  ：以月份的名字来排序，例如 JAN, DEC 等等的排序方法；
    -n  ：使用“纯数字”进行排序（默认是以文字体态来排序的）；
    -r  ：反向排序；
    -u  ：就是 uniq ，相同的数据中，仅出现一行代表；
    -t  ：分隔符号，默认是用 [tab] 键来分隔；
    -k  ：以那个区间 （field） 来进行排序的意思

### uniq

    [dmtsai@study ~]$ uniq [-ic]
    选项与参数：
    -i  ：忽略大小写字符的不同；
    -c  ：进行计数

    范例一：使用 last 将帐号列出，仅取出帐号栏，进行排序后仅取出一位；
    [dmtsai@study ~]$ last | cut -d ' ' -f1 | sort | uniq

    范例二：承上题，如果我还想要知道每个人的登陆总次数呢？
    [dmtsai@study ~]$ last | cut -d ' ' -f1 | sort | uniq -c

（1）先将所有的数据列出；（2）再将人名独立出来；（3）经过排序；（4）只显示一个

### wc

计算输出的讯息的整体数据
[dmtsai@study ~]$ wc [-lwm]
选项与参数：
-l ：仅列出行；
-w ：仅列出多少字（英文单字）；
-m ：多少字符；
  
 范例一：那个 /etc/man_db.conf 里面到底有多少相关字、行、字符数？
[dmtsai@study ~]$ cat /etc/man_db.conf | wc
131 723 5171 # 输出的三个数字中，分别代表： “行、字数、字符数”

## 双向重导向： tee

tee 会同时将数据流分送到文件去与屏幕 （screen）

## 字符转换命令

### tr

tr 可以用来删除一段讯息当中的文字，或者是进行文字讯息的替换！
[dmtsai@study ~]$ tr [-ds] SET1 ...
选项与参数：
-d ：删除讯息当中的 SET1 这个字串；
-s ：取代掉重复的字符！
  
 范例一：将 last 输出的讯息中，所有的小写变成大写字符：
[dmtsai@study ~]$ last | tr '[a-z]' '[A-Z]' # 事实上，没有加上单引号也是可以执行的，如：“ last | tr [a-z][a-z] ”
  
 范例二：将 /etc/passwd 输出的讯息中，将冒号 （:） 删除
[dmtsai@study ~]$ cat /etc/passwd | tr -d ':'

### join

join 在处理两个文件之间的数据， 而且，主要是在处理“两个文件当中，有 "相同数据" 的那一行，才将他加在一起”的意思。

### paste

paste 就直接“将两行贴在一起，且中间以 [tab] 键隔开”而已！简单的使用方法：

    [dmtsai@study ~]$ paste [-d] file1 file2
    选项与参数：
    -d  ：后面可以接分隔字符。默认是以 [tab] 来分隔的！
    -   ：如果 file 部分写成 - ，表示来自 standard input 的数据的意思。

    范例一：用 root 身份，将 /etc/passwd 与 /etc/shadow 同一行贴在一起
    [root@study ~]# paste /etc/passwd /etc/shadow

## 分区命令

split 可以帮你将一个大文件，依据文件大小或行数来分区，就可以将大文件分区成为小文件了！
[dmtsai@study ~]$ split [-bl] file PREFIX
选项与参数：
-b ：后面可接欲分区成的文件大小，可加单位，例如 b, k, m 等；
-l ：以行数来进行分区。
PREFIX ：代表前置字符的意思，可作为分区文件的前导文字。
  
 范例一：我的 /etc/services 有六百多 K，若想要分成 300K 一个文件时？
[dmtsai@study ~]$ cd /tmp; split -b 300k /etc/services services
[dmtsai@study tmp]$ ll -k services*
-rw-rw-r--. 1 dmtsai dmtsai 307200 Jul 9 22:52 servicesaa
-rw-rw-r--. 1 dmtsai dmtsai 307200 Jul 9 22:52 servicesab
-rw-rw-r--. 1 dmtsai dmtsai 55893 Jul 9 22:52 servicesac # 那个文件名可以随意取的啦！我们只要写上前导文字，小文件就会以 # xxxaa, xxxab, xxxac 等方式来创建小文件的！
  
 范例二：如何将上面的三个小文件合成一个文件，文件名为 servicesback
[dmtsai@study tmp]$ cat services* | servicesback # 很简单吧？就用数据流重导向就好啦！简单！

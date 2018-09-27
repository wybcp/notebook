# pexpect

expect 是一个用来处理交互场景的命令，借助 expect，我们可以将交互过程进行向动化。 expect 的思路非常简单，就是启动一个进程，然后监视进程的输出，如果进程的输出和当前期望得到的字符串匹配，则将输入发送给该进程。expect 一般用于 ssh、 ftp、 passwd、 telnet 等需要交互式处理的命令 。
pexpect 是 expect 命令的 Python 封装，有了 pexpect，我们就可以在 Python 代码中行远程服务器交互式处理 。

```bash
pip install pexpect
```

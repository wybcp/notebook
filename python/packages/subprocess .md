# subprocess

创建和管理子进程，调用计算机其他程序

## Popen()

`subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, s tderr=None, preexec_fn=None, close_fds=<object object at 0x101da81c0>, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, s tart_new_session=False, pass_fds=(), *, encoding=None, errors=None)`

Python 程序可以启动计算机中的其他程序，将程序的文件名传递给 subprocess.Popen()。

args 是需要执行的命令，可以是一个命令字符串，也可以是一个字符串列表。

如果这个进程在 poll()调用时仍在运行，poll()方法就返回 None。如果该程序已经终止， 它会返回该进程的整数退出代码。

wait()方法将阻塞，直到启动的进程终止。如果你希望你的程序暂停，直到用户完成 与其他程序，这非常有用。wait()的返回值是进程的整数退出代码。

## call

`subprocess.call(*popenargs, timeout=None, **kwargs)`

Run command with arguments. Wait for command to complete or
timeout, then return the returncode attribute.

The arguments are the same as for the Popen constructor. Example:

`return_code = subprocess.call(["ls", "-l"])`

可以通过退出状态码判断命令是否执行成功。如果成功返回 0，否则返回非 0。

## check_call

`subprocess.check_call(*popenargs, **kwargs)`

Run command with arguments. Wait for command to complete.

check_call 函数的作用与 call 函数类似，区别在于异常情况下返回的形式不同 。对于 check_call 函数，如果执行命令成功，返回 0，如果执行失败，抛出 subprocess. CalledProcessError 异常。

## check_output

`subprocess.check_output(*popenargs, timeout=None, **kwargs)`
check_output 函数通过返回值来返回命令的执行结果， check_output 函数通过抛出一个 subprocess. CalledProcessError 异常来表示命令执行出错 。

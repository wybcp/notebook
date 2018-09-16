# Virtualenv

一个工具，创建一个独立(隔离)的 Python 环境。

```bash
$ virtualenv myproject
$ source myproject/bin/activate
```

执行第一个命令在 myproject 文件夹创建一个隔离的 virtualenv 环境，第二个命令激活这个隔离的环境(virtualenv)。

virtualenv 使用系统全局模块，请使用`--system-site-packages` 参数创建你的 virtualenv，例如：
`virtualenv --system-site-packages mycoolproject`

以退出这个 virtualenv:
`$ deactivate`

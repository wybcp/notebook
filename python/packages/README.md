# 包

## 更新 packages

`pipdate`

```python
import pip
from subprocess import call
for package in pip.get_installed_distributions():
   call('pip install -i https://mirrors.aliyun.com/pypi/simple/ -U ' + package.project_name)
```

[来源](https://www.zhihu.com/question/63202629/answer/206646542)

## 包知识

### 读取位于包中的数据文件

`pkgutil.get_data()`函数是一个读取数据文件的高级工具，不用管包是如何安装以及安装在哪。它只是工作并将文件内容以字节字符串返回给你

`get_data()`的第一个参数是包含包名的字符串。你可以直接使用包名，也可以使用特殊的变量，比如**package**。第二个参数是包内文件的相对名称。如果有必要，可以使用标准的 Unix 命名规范到不同的目录，只要最后的目录仍然位于包中。

## 验证安装

- python shell 尝试进行 import 导入即可。
- 使用 Python 解释器的 -c 参数快速地执行 import 语句，如下所示:

  ```bash
  python -c "import paramik"
  ```

## 目录

### 内建模块

- [shutil 处理文件夹](shutil.md)
- [copy 复制列表](copy.md)
- [logging 日志](logging.md)
- [pathlib 处理路径](pathlib.md)
- [subprocess 调用外部程序](subprocess.md)
- [time 时间模块](time.md)
- [collections 容器](collections.md)

### 常见包

- [Ansible](Ansible.md)
- [Zulip 实时聊天](zulip.md)
- [virtualenv 虚拟环境](virtualenv.md)

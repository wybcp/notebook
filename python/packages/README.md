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

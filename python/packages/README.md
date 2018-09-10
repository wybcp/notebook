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
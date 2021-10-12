# anaconda

## 更新所有包

```bash
#先把conda更新到最新版
conda update conda
#把anaconda更新的新版
conda update anaconda
#配置环境也更新到最新版的Anaconda
conda update --all
```



## 查看安装的库

`conda list`

## 查看配置

`conda config --show`

## conda换国内源

### 查看源

`conda config --show-sources`

这里有两个源，一个是清华的源，另一个是默认的源

### 添加源

`conda config --add channels`

```bash
# 中科大的源
conda config –add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
# 清华的源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
# 阿里云的源
conda config --add channels https://mirrors.aliyun.com/pypi/simple/
```

### 移除源

`conda config --remove channels`

操作

`conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkg`
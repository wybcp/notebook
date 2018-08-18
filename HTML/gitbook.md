# Gitbook

##上传电子书

###首次上传

在本地新建一个文件夹，并通过 Git 命令把新建的远程项目抓取到本地，如下所示：
```
$ mkdir MyFirstBook-Git
$ cd MyFirstBook-Git
$ git init
$ git pull https://git.gitbook.com/wybcp/myfirstbook.git
```

使用 Git 命令把本地的项目上传到远程，如下所示：
```
$ git add -A
$ git commit -m "提交说明"
$ git remote add gitbook https://git.gitbook.com/wybcp/myfirstbook.git
$ git push -u gitbook master
```
期间需要输入你的 GitBook 用户名和密码（[设置](https://www.gitbook.com/@wybcp/settings)，在个人的profile设置password）。

###再次提交
修改内容后只需要输入以下 Git 命令即可：
```
$ git add [修改的文件]
$ git commit -m "提交说明"
$ git push -u gitbook master
```
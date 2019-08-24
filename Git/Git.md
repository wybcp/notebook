# Git

- 创建 git 仓库

  当前目录下多了一个`.git` 的目录，这个目录是 Git 来跟踪管理版本库的

  ```sh
  git init
  ```

- 工作区状态

  ```sh
  git status //查看状态
  git diff //比较差异
  ```

- 版本回退

  HEAD 指向的版本就是当前版本，因此，Git 允许我们在版本的历史之间穿梭

  ```sh
  git log //查看提交的记录
  git reflog //查看命令操作的记录
  git reset --hard HEAD//回退到Head的工作区
  ```

- 工作区、暂存区

  工作区就是当前操作的目录。当你使用 git add 的时候就是把文件加到暂存区。commit 之后就是把暂存区的文件提交到分支中

  版本库记录着差异。

  ![image](https://www.liaoxuefeng.com/files/attachments/001384907720458e56751df1c474485b697575073c40ae9000/0)

- 撤销修改

  命令 `git checkout -- readme.txt` 意思就是，把 readme.txt 文件在工作区的修改全部撤销，这里有两种情况：

  一种是 readme.txt 自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

  一种是 readme.txt 已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

  用命令

  ```sh
  git reset HEAD file
  ```

  可以把暂存区的修改撤销掉（unstage），重新放回工作区。使用 HEAD 表示最新的状态

  放弃所有文件修改可以使用 `git checkout .`

- 删除文件

  使用 `git rm file` 可以删除版本库中的文件

  ```sh
  git rm read.txt

  git checkout -- read.txt //从版本库中恢复
  ```

- 远程仓库

  添加远程仓库

  origin 是仓库名字。是 git 的默认的

  ```sh
  git remote  add origin 仓库地址
  git remote -v 查看远程仓库
  git push -u origin master //将本地master和orgin分支关联。
  git clone 仓库地址 //clone 一个远程仓库到本地
  git checkout -b branch-name origin/branch-name，//本地和远程分支的名称最好一致
  git branch --set-upstream branch-name origin/branch-name //建立本地分支和远程分支的关联，
  git pull  orgin master //从远程分支抓取
  ```

## git 分支

master 是 git 默认的分支，也叫主分支。每一次提交在分支上形成了一个时间线。HEAD 指向该分支

![image](https://www.liaoxuefeng.com/files/attachments/001384908811773187a597e2d844eefb11f5cf5d56135ca000/0)

- 创建分支

  ```sh
  git branch dev //创建分支
  git checkout dev //切换分支
  git branch  //命令会列出所有分支
  git checkout -b dev //创建并切换到dev分支
  ```

  HEAD 指针指向了 dev ![image](https://www.liaoxuefeng.com/files/attachments/00138490883510324231a837e5d4aee844d3e4692ba50f5000/0)

- 合并分支

  合并某分支到当前分支：`git merge <name>`

  ```sh
  git checkout master
  git merge dev
  ```

- 删除分支

  ```sh
  git branch -d dev
  git branch -D <name> //强行删除
  ```

## 工作区暂存

将工作区暂时保存起来 不提交到暂存区。

```sh
git stash //保存工作区

git stash list //查看保存的工作区
git stash pop
git stash apply //恢复保存的工作区
git stach drop //删除保存的工作区
```

## tag 标签

```sh
git tag v1.0 //打标签
git tag  // 列出所有的标签
git tag commit_id //给特定的commit_id打标签
git tag -a v1.0 -m "tag1" //打带说明的标签
```

- 删除标签

  ```sh
  git tag -d v1.0
  ```

- 推送标签到远程分支

  ```sh
  git push orgin v1.0
  git push origin --tags// 推送所有的标签到远程分支
  git push origin :refs/tags/v0.9 //删除远程分支的标签
  ```

### 配置 git

初次使用 需要配置自己的信息，

```sh
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

- 配置忽略文件

  .gitignore 文件本身要放到版本库里，并且可以对.gitignore 做版本管理！

  忽略文件的原则是：

  1. 忽略操作系统自动生成的文件，比如缩略图等；
  2. 、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如 Java 编译产生的.class 文件

  3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

- 设置别名

  别名就是把一些复杂的命令简化 类似 svn co 等之类的

  ```shell
  git config --global alias.co checkout
  git config --global alias.ci commit
  git config --global alias.br branch
  git config --global alias.unstage 'reset HEAD'
  git config --global alias.last 'log -1'
  git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
  ```

- 当前项目配置

  每个仓库的 Git 配置文件都放在.git/config 文件中：

  ```conf
  [core]
      repositoryformatversion = 0
      filemode = true
      bare = false
      logallrefupdates = true
      ignorecase = true
      precomposeunicode = true
  [remote "origin"]
      url = git@github.com:xianyunyh/PHP-Interview
      fetch = +refs/heads/*:refs/remotes/origin/*
  [branch "master"]
      remote = origin
      merge = refs/heads/master
  [alias]
      last = log -1
  ```

  当前用户的 Git 配置文件放在用户主目录下的一个隐藏文件.gitconfig 中

  ```conf
  [alias]
      co = checkout
      ci = commit
      br = branch
      st = status
  [user]
      name = Your Name
      email = your@email.com
  ```

## [git 指定 sshkey 访问远程仓库](https://segmentfault.com/a/1190000005349818)

置我们的 git 使用我们新创建的 key 来访问远程仓库啦

`vim ~/.ssh/config`
如果没有 config 这个文件，新建一个就好，然后在 config 文件追加如下内容：

```config
Host git.company.com
User git
IdentityFile /Users/guanliyuan/.ssh/test
IdentitiesOnly yes
```

其中

- git.company.com 是你的远程仓库域名
- User git 就这样配置就行了，表示这是给 git 命令使用的
- IdentityFile 这个表示私钥文件地址
- IdentitiesOnly 这个配置 yes，表示只使用这里的 key，防止使用默认的

# [git 的 index 被损坏](http://www.cnblogs.com/fuyanwen/p/3729387.html)

解决方法：

需要重新生成 index 文件，

```shell
rm -f .git/index
git reset --mixed HEAD
```

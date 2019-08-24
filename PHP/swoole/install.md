# 安装

MacOS

## pecl 方式

```shell
$ pecl install swoole
No releases available for package "pecl.php.net/swoole"
install failed
```

遇到上面的问题，直接打开[pecl swoole](https://pecl.php.net/package/swoole)，下载最新稳定版到本地

```shell
wget https://pecl.php.net/get/swoole-4.0.3.tgz
pecl install /path/swoole-4.0.3.tgz
```

`/private/tmp/pear/temp/swoole/include/swoole.h:427:10: fatal error: 'openssl/ssl.h' file not found`<https://blog.csdn.net/qq_34908844/article/details/79319054>找到你们的 openssl 文件夹，把它拷贝到 swoole 安装包下的 include 下面，技术是 openssl 的所有.h 文件，我的 openssl 文件的目录为`/usr/local/opt/openssl/include` 把这个路径下的 openssl 文件夹 copy 到安装文件夹中的 include 下就 ok 了。

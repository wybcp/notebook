# 安装

MacOS,

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

`/private/tmp/pear/temp/swoole/include/swoole.h:427:10: fatal error: 'openssl/ssl.h' file not found`https://blog.csdn.net/qq_34908844/article/details/79319054找到你们的openssl文件夹，把它拷贝到swoole安装包下的include下面，技术是openssl的所有.h文件，我的openssl文件的目录为/usr/local/opt/openssl/include 把这个路径下的openssl文件夹copy到安装文件夹中的include下就ok了。
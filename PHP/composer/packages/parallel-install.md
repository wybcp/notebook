# Composer 加速——hirak/prestissimo

我们使用 Composer 的时候回感觉安装的特别慢，可以采用下面两种方式加速。

## 镜像加速

网络问题是一个方面，我们可以使用一些国内的[中国镜像](../composer-mirror.md)来解决网络的问题。

## 并行下载加速

因为 Composer 是单进程方式下载的，也就是说 Composer 安装完一个依赖，才回去下载并安装另一个依赖，任何网络问题都会让这个进程卡住。

[hirak/prestissimo](https://github.com/hirak/prestissimo) 利用并行下载的思路来加速 Composer 的，看一下这个包的描述——composer parallel install plugin （Composer 并行安装插件）。

```shell
$ composer global require hirak/prestissimo
```

## 参考

https://laravel-china.org/courses/laravel-package/1695/hirakprestissimo

https://github.com/hirak/prestissimo

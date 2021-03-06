# 架构

## 压缩输出

在 php.ini 中开启 gzip 压缩：

```conf
zlib.output_compression = On
zlib.output_compression_level = (level)
```

`level`可能是`1-9`之间的数字，你可以设置不同的数字。

几乎所有的浏览器都支持 Gzip 的压缩方式，gzip 可以降低`80%`的输出.

付出的代价是，大概增加了 10%的 cpu 计算量,但是可以减少带宽，页面加载变快。

## [静态化页面](page-static.md)

Apache/Nginx 解析一个 PHP 脚本的时间，要比解析一个静态 HTML 页面慢`2`至`10`倍。

所以尽量使页面静态化或使用静态 HTML 页面。

## 将 PHP 升级到最新版

提高性能的最简单的方式是不断升级、更新 PHP 版本。

## 利用 PHP 的扩展

一直以来，大家都在抱怨 PHP 内容太过繁杂。

最近几年来，开发人员作出了相应的努力，移除了项目中的一些冗余特征。

即便如此，可用库以及其它扩展的数量还是很可观。

甚至一些开发人员开始考虑实施自己的扩展方案。

## PHP 缓存

一般情况下，PHP 脚本被 PHP 引擎编译后执行，会被转换成机器语言，也称为操作码。

如果 PHP 脚本反复编译得到相同的结果，为什么不完全跳过编译过程呢？

PHP 加速器缓存了编译后的机器码，允许代码根据要求立即执行，而不经过繁琐的编译过程。

对 PHP 开发人员而言，目前提供了两种可用的缓存方案。

一种是 APC（Alternative PHP Cache，可选 PHP 缓存），它是一个可以通过 PEAR 安装的开源加速器。

另一种流行的方案是 [OPCode](opcode.md)，也就是操作码缓存技术。

## 使用 NoSQL 缓存

Memchached 或者 Redis 都可以。

这些是高性能的分布式内存对象缓存系统，能提高动态网络应用程序性能，减轻数据库的负担。

这对运算码（OPcode）的缓存也很有用，使得脚本不必为每个请求重新编译。

## 使用 Json 替代 xml

`json_encode()`和 `json_decode()` 等 PHP 的内置方法，运行速度都非常快，所有应该优先使用 Json。

如果你无法避免使用 xml，那么请务必使用正则表达式而不是 DOM 操作来进行解析。

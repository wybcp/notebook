# composer 中国镜像

## Packagist / Composer 中国全量镜像

[Packagist / Composer 中国全量镜像](https://pkg.phpcomposer.com/)

在国内使用 Composer 下载特别慢,可以通过二个方法进行加速

```shell
composer config repo.packagist composer “https://packagist.phpcomposer.com“
```

编辑 composer.json

```json
"repositories": {
  "packagist": {
      "type": "composer",
      "url": "https://packagist.phpcomposer.com"
  }
}
```

## [阿里巴巴开源镜像](https://developer.aliyun.com/composer)

选项一、全局配置（推荐）

```shell
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

选项二、单独使用

如果仅限当前工程使用镜像，去掉 -g 即可，如下：

```shell
composer config repo.packagist composer https://mirrors.aliyun.com/composer/
```

composer 命令后面加上 -vvv （是 3 个 v）可以打印出调错信息，命令如下：

```shell
composer -vvv create-project laravel/laravel blog
composer -vvv require psr/log
```

使用 laravel new 命令创建工程， 这个命令会从下一个 zip 包，里面自带了 `composer.lock`，也无法使用镜像加速，解决方法：

方法一（推荐）：
不使用 `laravel new`，直接用 `composer create-project laravel/laravel xxx` 新建工程。

方法二：
运行 `laravel new xxx`，当看见屏幕出现 `- Installing doctrine/inflector`时，Ctrl + C 终止命令，cd xxx 进入，删除 composer.lock，再运行 `composer install`。

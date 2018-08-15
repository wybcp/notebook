# Composer 简介

## Packagist

Packagist 是 Composer 主要的一个包信息存储库，包开发者将具体代码托管到 Github 上，将包信息提交到 Packagist 上，这样使用者就可以通过 Composer 去使用。

Composer 根据本地定义的 `composer.json` 信息去查询 Packagist，Packagist 根据 `Composer.json/Package.json` 信息解析，最终对应到 github 仓库，Composer 最终下载代码的时候还要依赖于 Github 仓库上的 `Composer.json`，这里涉及到三种类型的 composer.json，含义是不一样的。

## Composer.json

这是 Composer 的核心，是 Composer 的规则。

## Composer 命令行工具

```shell
composer init
```

使用者可以在自己的项目下创建 `composer.json` 以便定义你项目的依赖包，也可以通过 `composer init` 交互式的创建 `composer.json`。

```shell
composer require
```

假如手动或者交互式创建 `composer.json` 文件，可以直接使用该命令来安装包

```shell
composer require  cerdic/css-tidy:1.5.2
composer require "ywdblog/phpcomposer:dev-master"
```

–prefer-source 和–prefer-dist 参数

```shell
composer require "ywdblog/phpcomposer:dev-master" --prefer-source
```

`–prefer-dist`：对于稳定的包来说，一般 Composer 安装默认使用该参数，这也能加快安装，比如有可能直接从 packagist 安装了相应的包，而不用实际去 Github 上下载包。

`–prefer-source`：假如使用该参数，则会直接从 Github 上安装，安装包后 vendor 目录下还含有`.git` 信息。

```shell
composer install
```

应该是最常用的命令，composer 会根据本地的`composer.json`安装包，将下载的包放入项目下的 vendor 目录下，同时将安装时候的包版本信息放入到`composer.lock`，以便锁定版本。

其实在 install 的时候，假如发现`composer.lock`版本和目前 vendor 目录下的代码版本是一致的，则 Composer 会什么也不做，`composer.lock`的目的就是让你安心在目前这个版本下工作，而不获取最新版本的包。

```shell
composer update
```

通过这个命令即可更新最新版本的包

```shell
composer config
```

全局的配置保存在`COMPOSER_HOME/config.json`，非全局的配置信息则存储在本项目目录下。

```shell
composer config --list -g
composer config -g notify-on-install false
composer global config bin-dir --absolute
composer create-project
```

这个命令不常用，但是个人觉得还是很重要的，使用普通的 install 命令是将项目所有的依赖包下载到本项目 vendor 目录下。而通过这个命令则是将所有的代码及其依赖的包放到一个目录下，相当于执行了一个 `git clone` 命令，一般是包的开发者可能为了修复 bug 会使用该命令。

```shell
composer global
```

这是一个全局的安装命令，它允许你在`COMPOSER_HOME`目录下执行 Composer 的命令，比如`install，update`。当然你的`COMPOSER_HOME`要在$PATH 环境下。

安装后想更新它，只需要运行

```shell
composer global update

composer dump-autoload
```

当你修改项目下的`composer.json`的文件，可以使用该命令来更新加载器。

## 语义版本方案

版本号由三个点（.）分数字组成：

1. 第一个数字是主版本号；
2. 第二个数字是次版本号，小幅更新；
3. 第三个是修订版本号，修正错误。

当使用者在本地配置 `composer.json` 的时候,可以指定需要包的特定版本,Composer 支持从 Github 仓库中下载 Tag 或者分支下的包。

对于 Github 上的 Tag 来说,Packagist 会创建对应包的版本,它符合`X.Y.Z,vX.Y.Z,X.Y.Z-`包类型,就是说 Github 上虽然只有一个特定版本的包,但 Composer 支持多种形式的引用方式,比如:

```shell
composer require monolog/monolog  1.0.0-RC1
composer require monolog/monolog  v1.0.0-RC1
composer require monolog/monolog  1.0.*
composer require monolog/monolog  ~1.10
```

对于 Github 上的分支来说,Packagist 会创建对应包的版本,假如分支名看起来像一个版本,将创建{分支名}-dev 的包版本号,如果分支名看起来不像一个版本号,它将会创建 dev-{分支名}形式的版本号

```shell
composer require monolog/monolog  master-dev
composer require monolog/monolog  master.x-dev
```

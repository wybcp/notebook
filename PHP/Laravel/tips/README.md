# 小技巧

## 分组计数 `groupby and count`

直接写查询语句执行

## 生成注册相关文件

`php artisan ui bootstrap --auth`

## 异常exception

如果无法查看异常，直接异常输出
`app/Exceptions/Handler.php`中`report`方法中添加`dd($e)`

## 打印SQL

<https://learnku.com/laravel/wikis/27707>

## 前端流程

手动编译

```bash
npm run dev
```

自动编译

```bash
npm run watch-poll
```

## 创建模型

如果需要在创建模型的同时顺便创建数据库迁移，则可以使用 --migration 或 -m 选项

```bash

php artisan make:model Models/Article -m
```

## artisan

查看命令列表
`php artisan list`

## Eloquent 表命名约定

默认情况下会使用类的「下划线命名法」与「复数形式名称」来作为数据表的名称生成规则。

BlogPost 数据模型类对应 blog_posts 表

如果需要指定自己的数据表，则可以通过 table 属性来定义`protected $table="";`

## 数据库迁移

### 重置数据库

`php artisan migrate:refresh`
refresh 的作用是重置数据库并重新运行所有迁移。

>注意：此命令会删除数据库数据，日常开发时请谨慎使用。

### 重置数据库并填充数据

`php artisan migrate:refresh --seed`

### 填充数据

`php artisan db:seed`

## 辅助函数

Laravel 提供了全局辅助函数 `old` 来帮助我们在 Blade 模板中显示旧输入数据。这样当我们信息填写错误，页面进行重定向访问时，输入框将自动填写上最后一次输入过的数据。
`{{ old('name') }}`

## restful

### delete方法

到用户退出登录的按钮实际上是一个表单的提交按钮，在点击退出按钮之后浏览器将向 `/logout` 地址发送一个 `POST` 请求。但由于 RESTful 架构中会使用 `DELETE` 请求来删除一个资源，当用户退出时，实际上相当于删除了用户登录会话的资源，因此退出操作需要使用 `DELETE` 请求来发送给服务器。

在 Blade 模板中，我们可以使用 method_field 方法来创建隐藏域。
`{{ method_field('DELETE') }}`

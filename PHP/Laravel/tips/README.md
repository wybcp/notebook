# 小技巧

base on laravel 7.x

## git

`git clean -f -d`命令`git clean` 作用是清理项目，`-f` 是强制清理文件的设置，`-d` 选项命令连文件夹一并清除。

## 初始化

### `config`

```php
'timezone' => 'Asia/Shanghai',
'locale' => 'zh-CN',//zh_CN
'faker_locale' => 'zh_CN',
```

## html

- 应用配置的语言设置`<html lang="{{ app()->getLocale() }}">`
- csrf-token 标签是为了方便前端的 JavaScript 脚本获取 CSRF 令牌。`<meta name="csrf-token" content="{{ csrf_token() }}">`
- 页面标题`<title>@yield('title', 'LaraBBS')</title>`
- 自动加载mix生成的文件`<link href="{{ mix('css/app.css') }}" rel="stylesheet">`

## 分组计数 `groupby and count`

直接写查询语句执行

## 异常exception

如果无法查看异常，直接异常输出
`app/Exceptions/Handler.php`中`report`方法中添加`dd($e)`

## 打印SQL

<https://learnku.com/laravel/wikis/27707>

## 前端

### 框架

1. 开发环境使用 Bootstrap 前端框架`composer require laravel/ui:^2.0 --dev`
1. 引入bootstrap`php artisan ui bootstrap`

### 生成注册相关文件

`php artisan ui bootstrap --auth`

### 流程

手动编译

```bash
npm run dev
```

自动编译

```bash
npm run watch-poll
```

### 浏览器缓存

Laravel Mix 给出的方案是为每一次的文件修改做哈希处理。

`webpack.mix.js`文件修改：

```js
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
   .sass('resources/sass/app.scss', 'public/css').version();
```

页面引用：
`<link href="{{ mix('css/app.css') }}" rel="stylesheet">`

### fontawesome字体图标库

Font Awesome 提供了可缩放的矢量图标，允许我们使用 CSS 所提供的所有特性对它们进行更改，包括：大小、颜色、阴影或者其它任何支持的效果。
`yarn add @fortawesome/fontawesome-free`
样式中载入：`resources/sass/app.scss`

```scss
// Fontawesome
@import '~@fortawesome/fontawesome-free/scss/fontawesome';
@import '~@fortawesome/fontawesome-free/scss/regular';
@import '~@fortawesome/fontawesome-free/scss/solid';
@import '~@fortawesome/fontawesome-free/scss/brands';
```

### 用户验证脚手架

`php artisan ui:auth`

```php
// 用户身份验证相关的路由
Route::get('login', 'Auth\LoginController@showLoginForm')->name('login');
Route::post('login', 'Auth\LoginController@login');
Route::post('logout', 'Auth\LoginController@logout')->name('logout');

// 用户注册相关路由
Route::get('register', 'Auth\RegisterController@showRegistrationForm')->name('register');
Route::post('register', 'Auth\RegisterController@register');

// 密码重置相关路由
Route::get('password/reset', 'Auth\ForgotPasswordController@showLinkRequestForm')->name('password.request');
Route::post('password/email', 'Auth\ForgotPasswordController@sendResetLinkEmail')->name('password.email');
Route::get('password/reset/{token}', 'Auth\ResetPasswordController@showResetForm')->name('password.reset');
Route::post('password/reset', 'Auth\ResetPasswordController@reset')->name('password.update');

// Email 认证相关路由
Route::get('email/verify', 'Auth\VerificationController@show')->name('verification.notice');
Route::get('email/verify/{id}/{hash}', 'Auth\VerificationController@verify')->name('verification.verify');
Route::post('email/resend', 'Auth\VerificationController@resend')->name('verification.resend');
```

### 本地化

Laravel 提供的本地化特性，使用 `__()` 函数来辅助实现。按照约定，本地化文件存储在 `resources/lang` 文件夹中，为 JSON 格式。

#### `overtrue/laravel-lang`

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

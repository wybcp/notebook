# 路由模型绑定

## 隐式绑定

此功能称为 [『隐性路由模型绑定』](http://d.laravel-china.org/docs/5.4/routing#隐式绑定)，是『约定优于配置』设计范式的体现，同时满足以下两种情况，此功能即会自动启用：

1. 路由声明时必须使用 Eloquent 模型的单数小写格式来作为路由片段参数，User 对应 `{user}`：

   ```php
   Route::get('/users/{user}', 'UsersController@show')->name('users.show');
   ```

   在使用资源路由 `Route::resource('users', 'UsersController');` 时，默认已经包含了上面的声明。

2. 控制器方法传参中必须包含对应的 Eloquent 模型类型声明，并且是有序的：

   ```php
   public function show(User $user)
   {
       return view('users.show', compact('user'));
   }
   ```

   当请求 http://sample.app/users/1 并且满足以上两个条件时，Laravel 将会自动查找 ID 为 1 的用户并赋值到变量 `$user` 中，如果数据库中找不到对应的模型实例，会自动生成 HTTP 404 响应。

   ```php
   return view('users.show', compact('user'));
   ```

   我们将用户对象 `$user` 通过 [`compact`](http://php.net/manual/zh/function.compact.php) 方法转化为一个关联数组，并作为第二个参数传递给 `view` 方法，将数据与视图进行绑定。

   `show` 方法添加完成之后，我们便能在视图中使用 `user` 变量来访问通过 `view` 方法传递给视图的用户数据。

### 自定义键名

如果你想要模型绑定在检索给定的模型类时使用除 `id` 之外的数据库字段，你可以在 Eloquent 模型上重写 `getRouteKeyName` 方法：

```php
/**
 * 为路由模型获取键名。
 *
 * @return string
 */
public function getRouteKeyName()
{
    return 'slug';
}
```

## 显式绑定

要注册显式绑定，使用路由器的 model 方法来为给定参数指定类。在 RouteServiceProvider 类中的 boot 方法内定义这些显式模型绑定：

```php
public function boot()
{
    parent::boot();

    Route::model('user', App\User::class);
}
```

接着，定义一个包含 {user} 参数的路由：

```php
Route::get('profile/{user}', function (App\User $user) {
    //
});
```

因为我们已经将所有 {user} 参数绑定至 App\User 模型，所以 User 实例将被注入该路由。例如，profile/1 的请求会注入数据库中 ID 为 1 的 User 实例。

## 参考

- [Laravel 教程 - Web 开发实战进阶](https://fsdhub.com/books/laravel-essential-training-5.5/584/according-to-the-users-information)

- [Laravel HTTP 路由功能](https://d.laravel-china.org/docs/5.5/routing#route-model-binding)

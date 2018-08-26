# [授权策略 (Policy)](http://d.laravel-china.org/docs/5.5/authorization#policies)

策略应该用在特定的模型或者资源中。

在 Laravel 中可以使用 [授权策略 (Policy)](http://d.laravel-china.org/docs/5.5/authorization#policies) 来对用户的操作权限进行验证，在用户未经授权进行操作时将返回 403 禁止访问的异常。

我们可以使用以下命令来生成一个名为 `UserPolicy` 的授权策略类文件，用于管理用户模型的授权。

```bash
$ php artisan make:policy UserPolicy
```

所有生成的授权策略文件都会被放置在 `app/Policies` 文件夹下。

让我们为默认生成的用户授权策略添加 `update` 方法，用于用户更新时的权限验证。

`app/Policies/UserPolicy.php`

```php
<?php

namespace App\Policies;

use App\Models\User;
use Illuminate\Auth\Access\HandlesAuthorization;

class UserPolicy
{
    use HandlesAuthorization;

    public function update(User $currentUser, User $user)
    {
        return $currentUser->id === $user->id;
    }
}
```

`update` 方法接收两个参数，第一个参数默认为当前登录用户实例，第二个参数则为要进行授权的用户实例。当两个 id 相同时，则代表两个用户是相同用户，用户通过授权，可以接着进行下一个操作。如果 id 不相同的话，将抛出 403 异常信息来拒绝访问。

使用授权策略需要注意以下两点：

1. 我们并不需要检查 `$currentUser` 是不是 NULL。未登录用户，框架会自动为其 **所有权限** 返回 `false`；
2. 调用时，默认情况下，我们 **不需要** 传递当前登录用户至该方法内，因为框架会自动加载当前登录用户（接着看下去，后面有例子）；

接下来我们还需要在 `AuthServiceProvider` 类中对授权策略进行注册。`AuthServiceProvider` 包含了一个 `policies` 属性，该属性用于将各种模型对应到管理它们的授权策略上。我们需要为用户模型 `User` 指定授权策略 `UserPolicy`。

`app/Providers/AuthServiceProvider.php`

```php
<?php

namespace App\Providers;
.
,
.
class AuthServiceProvider extends ServiceProvider
{
    /**
     * The policy mappings for the application.
     *
     * @var array
     */
    protected $policies = [
        'App\Model' => 'App\Policies\ModelPolicy',
        \App\Models\User::class  => \App\Policies\UserPolicy::class,
    ];
    .
    .
    .
}
```

授权策略定义完成之后，我们便可以在控制器中使用 `authorize` 方法来检验用户是否授权。默认的 `App\Http\Controllers\Controller` 控制器基类包含了 Laravel 的 `AuthorizesRequests` trait。此 trait 提供了 `authorize` 方法，它可以被用于快速授权一个指定的行为，当无权限运行该行为时会抛出 HttpException。`authorize` 方法接收两个参数，第一个为授权策略的名称，第二个为进行授权验证的数据。

我们需要为 `edit` 和 `update` 方法加上这行：

```php
$this->authorize('update', $user);
```

> 这里 `update` 是指授权类里的 `update` 授权方法，`$user` 对应传参 `update` 授权方法的第二个参数。正如上面定义 `update` 授权方法时候提起的，调用时，默认情况下，我们 **不需要** 传递第一个参数，也就是当前登录用户至该方法内，因为框架会 **自动** 加载当前登录用户。

书写的位置如下：

`app/Http/Controllers/UsersController.php`

```php
<?php

namespace App\Http\Controllers;
.
.
.
class UsersController extends Controller
{
    .
    .
    .

    public function edit(User $user)
    {
        $this->authorize('update', $user);
        return view('users.edit', compact('user'));
    }

    public function update(UserRequest $request, ImageUploadHandler $uploader, User $user)
    {
        $this->authorize('update', $user);
        $data = $request->all();

        if ($request->avatar) {
            $result = $uploader->save($request->avatar, 'avatars', $user->id, 362);
            if ($result) {
                $data['avatar'] = $result['path'];
            }
        }

        $user->update($data);
        return redirect()->route('users.show', $user->id)->with('success', '个人资料更新成功！');
    }
}
```

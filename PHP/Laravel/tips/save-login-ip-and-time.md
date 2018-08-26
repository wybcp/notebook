# 保存用户最后登陆的时间和 ip

## users 表

新建迁移表

```shell
php artisan make:migration add_login_fields_to_users_table --table=users
```

迁移表内容：

```php
class AddLoginFieldsToUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dateTime('last_login_at')->nullable()->comment('最后登录时间');
            $table->string('last_login_ip')->nullable()->comment('最后登录IP');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('last_login_at');
            $table->dropColumn('last_login_ip');
        });
    }
}
```

迁移文件

```shell
php artisan migrate
```

## 功能实现

修改 User 模型

```php
 protected $fillable = [
        'email',
        'password',
        'name',
        'last_login_at',
        'last_login_ip',
    ];
```

登录验证时调用`authenticated()` 方法,位于`AuthenticatesUsers` trait。`LoginController` 重写`authenticated`

```php
function authenticated(Request $request,User $user)
{
    $user->update([
        'last_login_at' => Carbon::now()->toDateTimeString(),
        'last_login_ip' => $request->getClientIp()
    ]);
}
```

## 增加用户登录日志

```php
php artisan make:migration create_user_login_logs_table
```

user_login_logs

```php
Schema::create('user_login_logs', function (Blueprint $table) {
    $table->increments('id');
    $table->integer('user_id')->index();
    $table->dateTime('login_at')->nullable()->comment('登录时间');
    $table->string('login_ip')->nullable()->comment('登录IP');
});
```

迁移文件

```shell
php artisan migrate
php artisan make:model Models/UserLoginLog
```

UserLoginLog

```php
public $timestamps = false;
```

```php
public function authenticated(Request $request,User $user)
{
    $now=Carbon::now()->toDateTimeString();
    $ip=$request->getClientIp();
    $user->update([
        'last_login_at' =>$now ,
        'last_login_ip' => $ip
    ]);
    $user_login=new UserLoginLog();
    $user_login->user_id=$user->id;
    $user_login->login_at=$now;
    $user_login->login_ip=$ip;
    $user_login->save();
}
```

## 参考

- [How to Save User’s Last Login Time and IP Address](http://laraveldaily.com/save-users-last-login-time-ip-address/)

# carbon 组件

[Carbon](https://github.com/briannesbitt/Carbon) 是 PHP DateTime 的一个简单扩展，Laravel 将其默认集成到了框架中。

对 Carbon 进行本地化的设置很简单，只在 `AppServiceProvider` 中调用 Carbon 的 `setLocale` 方法即可。

`app/Providers/AppServiceProvider.php`

```php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Carbon\Carbon;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        Carbon::setLocale('zh');
    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        //
    }
}
```

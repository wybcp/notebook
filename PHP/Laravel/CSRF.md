# CSRF

Laravel 默认是开启了CSRF功能，需要关闭此功能有两种方法：

## 关闭 CSRF

### 方法一

打开文件：`app\Http\Kernel.php`

把这行注释掉：

```php
'App\Http\Middleware\VerifyCsrfToken'
```

### 方法二

打开文件：`app\Http\Middleware\VerifyCsrfToken.php`

修改为：

```php
<?php namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier {

    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        // 使用CSRF
        //return parent::handle($request, $next);
        // 禁用CSRF
        return $next($request);
    }

}
```

## 使用方法

CSRF 的使用有两种，一种是在 HTML 的代码中加入：

```html
<input type="hidden" name="_token" value="{{ csrf_token() }}" />
```

另一种是使用cookie方式。

使用cookie方式，需要把app\Http\Middleware\VerifyCsrfToken.php修改为：

```php
<?php namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier {

    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        return parent::addCookieToResponse($request, $next($request));
    }

}
```

使用cookie方式的CSRF，可以不用在每个页面都加入这个input的hidden标签。

当然，也可以对指定的表单提交方式使用CSRF，如：

```php
<?php namespace App\Http\Middleware;

use Closure;
use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier {

    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        // Add this:
        if($request->method() == 'POST')
        {
            return $next($request);
        }

        if ($request->method() == 'GET' || $this->tokensMatch($request))
        {
            return $next($request);
        }
        throw new TokenMismatchException;
    }

}
```

只对GET的方式提交使用CSRF，对POST方式提交表单禁用CSRF

## 修改CSRF的cookie名称方法

通常使用CSRF时，会往浏览器写一个cookie，如：

![img](https://images0.cnblogs.com/blog2015/6088/201506/051826451136010.png)

要修改这个名称值，可以到打开这个文件：`vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\VerifyCsrfToken.php`

找到”XSRF-TOKEN“，修改它即可。

当然，你也可以在`app\Http\Middleware\VerifyCsrfToken.php`文件中，重写`addCookieToResponse(...)`方法做到。

另外，如需要对指定的页面不使用CSRF，可以参考如下文章：

<http://www.camroncade.com/disable-csrf-for-specific-routes-laravel-5/>

## 参考

[[PHP] - Laravel - CSRF token禁用方法](http://www.cnblogs.com/HD/p/4555369.html)：http://www.cnblogs.com/HD/p/4555369.html
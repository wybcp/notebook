# [helper 辅助方法](https://laravel-china.org/docs/laravel/5.5/helpers/1320)

## Str::start() 辅助方法

我想下面的代码我可能已经写了不下一百次了。我们假设你有一个 API baseUrl，你通常需要移除尾部的斜杠来规范 URL：

```php
<?php

return [
    'my_api' => [
        'base_url' => rtrim(env('MY_API_BASE_URL'), '/'),
    ],
];
```

之后，当你需要规范路径避免出现多个斜杠的时候，可能需要执行以下操作：

```php
<?php

return config('my_api.base_url') . '/' . ltrim($path, '/')
```

现在，通过 Str::start() 及其辅助方法 str_start()，你可以这样规范路径：

```php
<?php

$path = '//example';

config('my_api.base_url') . str_start($path, '/');

// -> https://my-api.com/example
```

## Str::before() 辅助方法

假设你想得到邮箱地址最开始的部分：

```php
<?php

str_before('jane@example.com', '@');
// -> jane
```

## Str::after() 辅助方法

Str::after() 会返回字符串中给定某个值之后的所有内容。还是用邮箱地址的例子来说，假设我们只想获取邮箱地址的主机名：

```php
<?php

str_after('jane@example.com', '@')
// -> example.com
```

## 参考

- [Laravel 5.4 及 5.5 中新的字符串辅助方法介绍](https://9iphp.com/web/laravel/new-laravel-string-helpers-in-laravel-55.html)

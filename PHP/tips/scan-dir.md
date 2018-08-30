# 遍历目录

```php
<?php

/**
 * PHP 非递归实现查询该目录下所有文件
 * @param string $dir
 * @return mixed
 */
function scanFiles($dir)
{
    if (!is_dir($dir)) {
        return [];
    }

// 兼容各操作系统
    $dir = rtrim(str_replace('\\', '/', $dir), '/') . '/';

// 栈，默认值为传入的目录
    $dirs = [$dir];
//    var_dump($dirs);
// 放置所有文件的容器
    $rt = [];

    do {
// 弹栈
        $dir = array_pop($dirs);
        var_dump($dir);
// 扫描该目录
        $tmp = scandir($dir);

        foreach ($tmp as $f) {
// 过滤. ..
            if ($f == '.' || $f == '..') {
                continue;
            }

// 组合当前绝对路径
            $path = $dir . $f;

// 如果是目录，压栈。
            if (is_dir($path)) {
                array_push($dirs, $path . '/');
            } else {
                if (is_file($path)) { // 如果是文件，放入容器中
                    $rt [] = $path;
                }
            }
        }

    } while ($dirs); // 直到栈中没有目录

    return $rt;
}
```

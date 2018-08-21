# 从指定数字中获取随机组合

```php
<?php
/**
 * 获取指定数字的随机数字组合
 * 例如：给定数字100，需要随机获取3个组成这个数字的组合，例如70，20，10
 * @param  Int $var 数字
 * @param  Int $num 组合这个数字的数量
 * @return array
 */

function getNumGroups($var, $num)
{
    // 数量不正确
    if ($var < $num) {
        return [];
    }
    $total = 0;
    $result = [];
    for ($i = 1; $i < $num; $i++) {
        $tmp = mt_rand(1, $var - ($num - $i) - $total);
        $total += $tmp;
        $result[] = $tmp;
    }
    $result[] = $var - $total;
    return $result;

}
$result = getNumGroups(100, 3);
print_r($result);
```

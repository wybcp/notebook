# 二分查找

如何在有序的数组中找到一个数的位置

```php
/**
 * 二分查找
 * @param  array $array 数组
 * @param  int $n 数组数量
 * @param  int $value 要寻找的值
 * @return int
 */
function binary_search($array, $n, $value)
{
    $left = 0;
    $right = $n - 1;

    while ($left <= $right) {
        $mid = intval(($left + $right) / 2);
        if ($value > $array[$mid]) {
            $right = $mid + 1;
        } elseif ($value < $array[$mid]) {
            $left = $mid - 1;
        } else {
            return $mid;
        }
    }

    return -1;
}
```

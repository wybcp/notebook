# 删除指定数组元素

```php
<?php
$array = [1, 2, 5, 8, 9, 5, 6];

/**
 * 删除指定数组元素
 * @param      $array
 * @param      $deleteItem
 * @param bool $useOldKeys
 * @return array
 */
function deleteFromArray($array, $deleteItem, $useOldKeys = false)
{
    $key = array_search($deleteItem, $array, true);
    while ($key !== false) {
        unset($array[$key]);
        $key = array_search($deleteItem, $array, true);
    }
    if (!$useOldKeys) {
        $array = array_values($array);
    }
    return $array;

}

var_dump(deleteFromArray($array, 5, true));
// array(5) {
//   [0] =>
//   int(1)
//   [1] =>
//   int(2)
//   [3] =>
//   int(8)
//   [4] =>
//   int(9)
//   [6] =>
//   int(6)
// }
```

# 快速排序

```php
<?php
$data = [1, 43, 54, 62, 21, 66, 32, 78, 36, 76, 39];
function quickSort($data)
{
    //先判断是否需要继续进行
    $length = count($data);
    if ($length <= 1) {
        return $data;
    }
    //如果没有返回，说明数组内的元素个数多余1个，需要排序
    //选择一个标尺
    //选择第一个元素
    $base_num = $data[0];
    //遍历 除了标尺外的所有元素，按照大小关系放入两个数组内
    //初始化两个数组
    $left_array = [];//小于标尺的
    $right_array = [];//大于标尺的
    for ($i = 1; $i < $length; $i++) {
        if ($base_num > $data[$i]) {
            array_push($left_array,$data[$i]);
        } else {
            array_push($right_array,$data[$i]);
        }
    }
    //再分别对左边和右边的数组进行相同的排序处理方式
    //递归调用这个函数,并记录结果
    $left_array = quickSort($left_array);
    $right_array = quickSort($right_array);
    //合并左边 标尺 右边
    return array_merge($left_array, array($base_num), $right_array);
}
var_dump(quickSort($data));
```

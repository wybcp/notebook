# 数组

##关联数组
遍历并打印关联数组中的所有值，您可以使用 foreach 循环，如下所示：
```
<?php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");

foreach($age as $x=>$x_value)
{
echo "Key=" . $x . ", Value=" . $x_value;
echo "<br>";
}
?>
```
##数组排序
+ sort() - 对数组进行升序排列
+ rsort() - 对数组进行降序排列
+ asort() - 根据关联数组的值，对数组进行升序排列
+ ksort() - 根据关联数组的键，对数组进行升序排列
+ arsort() - 根据关联数组的值，对数组进行降序排列
+ krsort() - 根据关联数组的键，对数组进行降序排列

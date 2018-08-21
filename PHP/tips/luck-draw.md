# 等级抽奖概率

```php
<?php
/**
 * 一等奖、二等奖
 * 简单的抽奖概率函数
 * @param array $rewardArray 概率,如：$rewardArray = array(10, 20, 20, 30, 10, 10)，对应各奖品的概率
 * @return int    概率数组的下标
 */
function luckDraw(array $rewardArray)
{
    if (array_sum($rewardArray) !== 100) {
        return 'Error:The sum of values in $rewardArray Must be equal to 100!';
    }
    //获取随机数
    $reward_num = mt_rand(0, 99);
    $total_num = count($rewardArray);
    for ($i = 0; $i < $total_num; $i++) {
        if ($i == 0) {
            if ($rewardArray[$i] > $reward_num) {
                return $i;
            }
        } else {
            $max = $min = 0;
            for ($j = 0; $j <= $i; $j++) {
                $max = $max + $rewardArray[$j];
            }
            for ($k = 0; $k < $i; $k++) {
                $min = $min + $rewardArray[$k];
            }
            if ($max > $reward_num && $reward_num >= $min) {
                return $i;
            }
        }
    }
}
$rewardArray = array(10, 20, 20, 30, 10, 10);//10+20+20+30+10+10=100
echo luckDraw($rewardArray);
```

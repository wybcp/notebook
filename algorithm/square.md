# 矩形

给你四个坐标点，判断它们能不能组成一个矩形，如判断([0,0],[0,1],[1,1],[1,0])能组成一个矩形。

解题思路：以一个点为参考点。分别计算出到任意三点的距离，最长的距离的一个一个点是对角线的点。如果两条对角线相等，判断任意一个角是不是直角。即可判断是不是矩形了。

[php 实现](https://github.com/xianyunyh/arithmetic-php/blob/master/package/Other/Square.php)

```php
<?php
/**
 * Created by PhpStorm.
 * User: 南丞
 * Date: 2018/3/19
 * Time: 15:03
 * Facebook 面试题之 判断四个点能否组成正方形
 */
class Square
{
    protected $point = [];
    public function __construct(array $point)
    {
        $this->point = $point;
    }
    public function check()
    {
        $result = [];
        if (count($this->point) != 4) return false;
        for ($i = 0; $i < 4; $i++) {
            for ($j = $i + 1; $j < 4; $j++) {
                $result[]=$this->_calculation($i,$j);
            }
        }
        sort($result);
        if ($result[0] == $result[1] && $result[4] == $result[5] && $result[4] > $result[1]) {
            return true;
        }
        return false;
    }
    private function _calculation($i, $j)
    {
        return pow($this->point[$i][0] - $this->point[$j][0],2) + pow($this->point[$i][1] - $this->point[$j][1] ,2);
    }
}
$obj = new Square([[0, 0], [1, 0], [1, 1], [0, 1]]);
var_dump($obj->check());
```
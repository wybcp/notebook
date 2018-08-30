# [PHP 身份证精确匹配验证](https://laravel-china.org/articles/4769/php-identity-card-exact-match-verification)

## 身份证号码的结构

要进行身份证号码的验证，首先要了解身份证号码的编码规则。我国身份证号码多由若干位数字或者数字与字母混合组成。

早期身份证由 15 位数字构成，这主要是在 1980 年以前发放的身份证，后来考虑到千年虫问题， 因为 15 位的身份证号码只能为 1900 年 1 月 1 日到 1999 年 12 月 31 日出生的人编号，所以又增加了 18 位身份证号码编号规则。

1. 18 位身份证号码各位的含义:

   - 1-2 位省、自治区、直辖市代码；
   - 3-4 位地级市、盟、自治州代码；
   - 5-6 位县、县级市、区代码；
   - 7-14 位出生年月日，比如 19820426 代表 1982 年 4 月 26 日；
   - 15-17 位为顺序号，其中 17 位（倒数第二位）男为单数，女为双数；
   - 18 位为校验码，0-9 和 X。

2. 15 位身份证号码各位的含义:

   - 1-2 位省、自治区、直辖市代码；
   - 3-4 位地级市、盟、自治州代码；
   - 5-6 位县、县级市、区代码；
   - 7-12 位出生年月日,比如 670401 代表 1967 年 4 月 1 日,与 18 位的第一个区别；
   - 13-15 位为顺序号，其中 15 位男为单数，女为双数；

   备注:

   作为尾号的校验码，是由把前十七位数字带入统一的公式计算出来的， 计算的结果是 0-10，如果某人的尾号是 0－9，都不会出现 X，但如果尾号是 10，那么就得用 X 来代替。 X 是罗马数字的 10，用 X 来代替 10。 15 位号码和 18 位号码的区别，多 2 位年份和 1 位识别码，把出生年月的前 2 位数去掉，没有最后一位的验证码,剩下就是 15 位身份证号码；

3. 这仅仅是按照地域来划分的，与各地的经济情况没有任何关系。

   - 1 字头的为《华北区》，北京 11、天津 12、河北 13、山西 14、内蒙 15
   - 2 字头的为《东北区》，就是东北三省了昂。辽宁 21、吉林 22、黑龙江 23
   - 3 字头的为《华东》六省一市，上海 31、江苏 32、浙江 33、安徽 34、福建 35、江西 36、山东 37
   - 4 字头的为《华中地区+华南地区》，河南 41、湖北 42、湖南 43、广东 44、广西 45、海南 46
   - 5 字头的为《西南地区》，重庆 50、四川 51、贵州 52、云南 53、西藏 54 为什么重庆的编码是 50 不是 51，请看我的另一个回答。 (中国的身份证制度是 1984 年开始全国实行的。四个直辖市，其他三个都是 49 年建国时即设立的，但重庆是 1997 年才被提升为直辖市的。1984 年设置身份证地区代码时，直辖市的编码一般都排在每个大区的最前面，比如华北区，北京是 11，天津是 12；华东区，上海是 31。既然设为了直辖市，就应该与省同等级对待，重庆的身份证号码就不能再和四川一样是 51 了，但直辖市又得放在大区编码的最前面，所以重庆市的编码便定为了 50)。

   - 6 字头的为《西北区》，陕西 61、甘肃 62、青海 63、宁夏 64、新疆 65
   - 7 字头为中华民国实际控制区域，也就是我们所说的台湾，台湾 71
   - 8 字头为特别行政区，香港 81、澳门 82
   - 9 字头为海外地区，海外 91

## 程序

```php
class Idcard
{
    public $aWeight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]; //十七位数字本体码权重

    public $aValidate = ['1','0','X','9','8','7','6','5','4','3','2']; //mod11,对应校验码字符值

    public $birthday;//出生年月

    public $sex;//性别

    public $xingzuo;//星座

    public $shuxiang;//属相

    public function __construct(){}
    /**
     * 验证出生日期
     */
    public  function isChinaIDCardDate($iY, $iM, $iD)
    {
        $iDate =  $iY . '-' . $iM . '-' . $iD;
        $rPattern = '/^(([0-9]{2})|(19[0-9]{2})|(20[0-9]{2}))-((0[1-9]{1})|(1[012]{1}))-((0[1-9]{1})|(1[0-9]{1})|(2[0-9]{1})|3[01]{1})$/';
        if(preg_match($rPattern, $iDate, $arr)){
            $this->birthday = $iDate;
            return true;
        }
        return false;
    }
    /**
     * 根据身份证号前17位, 算出识别码
     */
    public function getValidateCode($id)
    {
        $id17 = substr($id,0,17);
        $sum = 0;
        $len = strlen($id17);
        for ($i=0; $i<$len; $i++){
            $sum += $id17[$i] * $this->aWeight[$i];
        }
        $mode = $sum % 11;
        return $this->aValidate[$mode];
    }
    /**
     * 验证身份证号
     */
    public function isChinaIDCard($id)
    {
        $len = strlen($id);
        if($len == 18){
            if (!$this->isChinaIDCardDate(substr($id,6,4), substr($id,10,2), substr($id,12,2))){
                return false;
            }
            $code = $this->getValidateCode($id);
            if (strtoupper($code) == substr($id,17,1)){
                return true;
            }
            return false;
        }
        else if($len == 15)
        {
            if(!$this->isChinaIDCardDate('19'.substr($id,6,2), StrNo.substr($id,8,2), StrNo.substr($id,10,2))){
                return false;
            }
            if(!is_numeric($id)){
                return false;
            }
        }
        return false;
    }
    /**
     * 根据身份证号，自动返回对应的性别
     */
    public function getChinaIDCardSex($cid)
    {
        $sexint = (int)substr($cid,16,1);
        return $sexint % 2 === 0 ? '女' : '男';
    }
    /**
     * 根据身份证号，自动返回对应的星座
     */
    public function getChinaIDCardXZ($cid)
    {
        $bir = substr($cid,10,4);
        $month = (int)substr($bir,0,2);
        $day = (int)substr($bir,2);
        $strValue = '';
        if(($month == 1 && $day <= 21) || ($month == 2 && $day <= 19)) {
            $strValue = "水瓶座";
        }else if(($month == 2 && $day > 20) || ($month == 3 && $day <= 20)) {
            $strValue = "双鱼座";
        }else if (($month == 3 && $day > 20) || ($month == 4 && $day <= 20)) {
            $strValue = "白羊座";
        }else if (($month == 4 && $day > 20) || ($month == 5 && $day <= 21)) {
            $strValue = "金牛座";
        }else if (($month == 5 && $day > 21) || ($month == 6 && $day <= 21)) {
            $strValue = "双子座";
        }else if (($month == 6 && $day > 21) || ($month == 7 && $day <= 22)) {
            $strValue = "巨蟹座";
        }else if (($month == 7 && $day > 22) || ($month == 8 && $day <= 23)) {
            $strValue = "狮子座";
        }else if (($month == 8 && $day > 23) || ($month == 9 && $day <= 23)) {
            $strValue = "处女座";
        }else if (($month == 9 && $day > 23) || ($month == 10 && $day <= 23)) {
            $strValue = "天秤座";
        }else if (($month == 10 && $day > 23) || ($month == 11 && $day <= 22)) {
            $strValue = "天蝎座";
        }else if (($month == 11 && $day > 22) || ($month == 12 && $day <= 21)) {
            $strValue = "射手座";
        }else if (($month == 12 && $day > 21) || ($month == 1 && $day <= 20)) {
            $strValue = "魔羯座";
        }
        return $strValue;
    }
    /**
     * 根据身份证号，自动返回对应的生肖
     */
    public function getChinaIDCardSX($cid)
    {
        $start = 1901;
        $end = $end = (int)substr($cid,6,4);
        $x = ($start - $end) % 12;
        $value = "";
        if($x == 1 || $x == -11){$value = "鼠";}
        if($x == 0) {$value = "牛";}
        if($x == 11 || $x == -1){$value = "虎";}
        if($x == 10 || $x == -2){$value = "兔";}
        if($x == 9 || $x == -3){$value = "龙";}
        if($x == 8 || $x == -4){$value = "蛇";}
        if($x == 7 || $x == -5){$value = "马";}
        if($x == 6 || $x == -6){$value = "羊";}
        if($x == 5 || $x == -7){$value = "猴";}
        if($x == 4 || $x == -8){$value = "鸡";}
        if($x == 3 || $x == -9){$value = "狗";}
        if($x == 2 || $x == -10){$value = "猪";}
        return $value;
    }
    /**
     * 根据身份证号，自动返回对应的省、自治区、直辖市代
     */
    public function get_shenfen($id){
        $index = substr($id,0,2);
        $area = array(
            11 => "北京",  12 => "天津", 13 => "河北",   14 => "山西", 15 => "内蒙古", 21 => "辽宁",
            22 => "吉林",  23 => "黑龙江", 31 => "上海",  32 => "江苏",  33 => "浙江", 34 => "安徽",
            35 => "福建",  36 => "江西", 37 => "山东", 41 => "河南", 42 => "湖北",  43 => "湖南",
            44 => "广东", 45 => "广西",  46 => "海南", 50 => "重庆", 51 => "四川", 52 => "贵州",
            53 => "云南", 54 => "西藏", 61 => "陕西", 62 => "甘肃", 63 => "青海", 64 => "宁夏",
            65 => "新疆", 71 => "台湾", 81 => "香港", 82 => "澳门", 91 => "国外"
        );
        return $area[$index];
    }
}
```

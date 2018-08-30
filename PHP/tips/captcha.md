# 验证码

```php
<?php
session_start();

$width=100;
$height=30;
$image=imagecreatetruecolor($width, $height);//创建黑底 框架
$bgcolor=imagecolorallocate($image, 255, 255, 255);//配置颜色,white
imagefill($image,0,0,$bgcolor);//区域填充


$captpha_code="";
// /*四位随机数  */
// for ($i=0;$i<4;$i++){
//     $fontsize=6;
//     /* 0~120 随机生成彩色（深色） */
//     $red=rand(0, 120);
//     $green=rand(0, 120);
//     $blue=rand(0, 120);
//     $fontColor=imagecolorallocate($image, $red, $green, $blue);
//     $x=$width/4*$i+rand(5, 10);//随机平均水平分布
//     $y=rand(8, 16);
//     $string=rand(0, 9);//生成0~9之间的随机数
//     $captpha_code.=$string;
//     imagestring($image, $fontsize, $x, $y, $string, $fontColor);//水平描绘字符串
// }

/*四位随机字符  */
for ($i=0;$i<4;$i++){
    $fontsize=6;
    /* 0~120 随机生成彩色（深色） */
    $red=rand(0, 120);
    $green=rand(0, 120);
    $blue=rand(0, 120);
    $fontColor=imagecolorallocate($image, $red, $green, $blue);
    $x=$width/4*$i+rand(5, 10);//随机平均水平分布
    $y=rand(8, 16);

    /* 制作字典，随机截取一个字符;为了方便用户识别，建议去除容易混淆的字符：0和O，1和l，2和z */
    $data="qwertyuipasdfghjkzxcvbnm3456789";
    $string=substr($data, rand(0, strlen($data)),1);
    $captpha_code.=$string;
    imagestring($image, $fontsize, $x, $y, $string, $fontColor);//水平描绘字符串
}
$_SESSION['authcode']=$captpha_code;

/*干扰元素之点干扰  */
for ($i = 0; $i < 200; $i++) {
    /* 100~200 随机生成彩色（前深色） */
    $red=rand(100, 200);
    $green=rand(100, 200);
    $blue=rand(100, 200);
    $color=imagecolorallocate($image, $red, $green, $blue);
    $x=rand(0, $width);//随机平均水平分布
    $y=rand(0, $height);
    imagesetpixel($image, $x, $y, $color);//生成像素点
}
/*干扰元素之线干扰  */
for ($i = 0; $i < 3; $i++) {
    /* 100~200 随机生成彩色（前深色） */
    $red=rand(100, 200);
    $green=rand(100, 200);
    $blue=rand(100, 200);
    $color=imagecolorallocate($image, $red, $green, $blue);
    $x=rand(0, $width);//随机平均水平分布
    $y=rand(0, $height);
    $x1=rand(0, $width);//随机平均水平分布
    $y1=rand(0, $height);
    imageline($image, $x, $y, $x1, $y1, $color);//水平地画一行字符串
}

header("content-type:image/png");
imagepng($image);//生成图片

imagedestroy($image);
```

## 图片

```php
<?php
session_start();

$table=array(
    'pic0'=>'dog',
    'pic1'=>'cat',
    'pic2'=>'bird',
    'pic3'=>'fish',
);
$index=rand(0, 3);
$value=$table['pic'.$index];
$_SESSION['authcode']=$value;

$filename=dirname(__FILE__).'\\pic'.$index.'jpg';
$content=file_get_contents($filename);

header('content-type:image/jpg');
echo($content);
```

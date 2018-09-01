# [采集百度图片](http://blog.csdn.net/fdipzone/article/details/54604708)

1.根据关键字采集百度搜寻结果
根据关键字采集百度搜寻结果，可以使用 curl 实现，代码如下：

```php
<?php
function doCurl($url, $data=array(), $header=array(), $timeout=30){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);

    $response = curl_exec($ch);
    if($error=curl_error($ch)){
        die($error);
    }

    curl_close($ch);

    return $response;
}

$wd = '仙剑奇侠传';
$url = 'http://www.baidu.com/s?wd='.urlencode($wd);
$data = array();
$header = array();

$response = doCurl($url, $data, $header, 5);
echo $response;
```

输出后发现有部分图片不能显示

这里写图片描述

2.采集后的图片不显示原因分析
直接在百度中搜寻，页面是可以显示图片的。使用 firebug 查看图片路径，发现采集的图片域名与在百度搜寻的图片域名不同。

采集返回的图片域名 t11.baidu.com

这里写图片描述

正常搜寻的图片域名 ss1.baidu.com

这里写图片描述

查看采集与正常搜寻的 html，发现有个域名转换的 js 是不一样的

采集

```js
var list = {
"graph.baidu.com": "http://graph.baidu.com",
"t1.baidu.com":"http://t1.baidu.com",
"t2.baidu.com":"http://t2.baidu.com",
"t3.baidu.com":"http://t3.baidu.com",
"t10.baidu.com":"http://t10.baidu.com",
"t11.baidu.com":"http://t11.baidu.com",
"t12.baidu.com":"http://t12.baidu.com",
"i7.baidu.com":"http://i7.baidu.com",
"i8.baidu.com":"http://i8.baidu.com",
"i9.baidu.com":"http://i9.baidu.com",
};
```

正常搜寻

```php
var list = {
"graph.baidu.com": "https://sp0.baidu.com/-aYHfD0a2gU2pMbgoY3K",
"t1.baidu.com":"https://ss0.baidu.com/6ON1bjeh1BF3odCf",
"t2.baidu.com":"https://ss1.baidu.com/6OZ1bjeh1BF3odCf",
"t3.baidu.com":"https://ss2.baidu.com/6OV1bjeh1BF3odCf",
"t10.baidu.com":"https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq",
"t11.baidu.com":"https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq",
"t12.baidu.com":"https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq",
"i7.baidu.com":"https://ss0.baidu.com/73F1bjeh1BF3odCf",
"i8.baidu.com":"https://ss0.baidu.com/73x1bjeh1BF3odCf",
"i9.baidu.com":"https://ss0.baidu.com/73t1bjeh1BF3odCf",
};
```

因此可以断定是，百度根据来源地址、IP、header 等参数，判断如果是采集的，则返回不同的 js。

3.采集后图片不显示的解决方法
把采集到的 html，根据定义的域名做一次批量转换即可。

```php
<?php
function doCurl($url, $data=array(), $header=array(), $timeout=30){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);

    $response = curl_exec($ch);
    if($error=curl_error($ch)){
        die($error);
    }

    curl_close($ch);

    return $response;
}

// 域名转换
function cdomain($str){
    $baidu_domain = '{
        "http://graph.baidu.com": "https://sp0.baidu.com/-aYHfD0a2gU2pMbgoY3K",
        "http://p.qiao.baidu.com":"https://sp0.baidu.com/5PoXdTebKgQFm2e88IuM_a",
        "http://vse.baidu.com":"https://sp3.baidu.com/6qUDsjip0QIZ8tyhnq",
        "http://hdpreload.baidu.com":"https://sp3.baidu.com/7LAWfjuc_wUI8t7jm9iCKT-xh_",
        "http://lcr.open.baidu.com":"https://sp2.baidu.com/8LUYsjW91Qh3otqbppnN2DJv",
        "http://kankan.baidu.com":"https://sp3.baidu.com/7bM1dzeaKgQFm2e88IuM_a",
        "http://xapp.baidu.com":"https://sp2.baidu.com/yLMWfHSm2Q5IlBGlnYG",
        "http://dr.dh.baidu.com":"https://sp0.baidu.com/-KZ1aD0a2gU2pMbgoY3K",
        "http://xiaodu.baidu.com":"https://sp0.baidu.com/yLsHczq6KgQFm2e88IuM_a",
        "http://sensearch.baidu.com":"https://sp1.baidu.com/5b11fzupBgM18t7jm9iCKT-xh_",
        "http://s1.bdstatic.com":"https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K",
        "http://olime.baidu.com":"https://sp0.baidu.com/8bg4cTva2gU2pMbgoY3K",
        "http://app.baidu.com":"https://sp2.baidu.com/9_QWsjip0QIZ8tyhnq",
        "http://i.baidu.com":"https://sp0.baidu.com/74oIbT3kAMgDnd_",
        "http://c.baidu.com":"https://sp0.baidu.com/9foIbT3kAMgDnd_",
        "http://sclick.baidu.com":"https://sp0.baidu.com/5bU_dTmfKgQFm2e88IuM_a",
        "http://nsclick.baidu.com":"https://sp1.baidu.com/8qUJcD3n0sgCo2Kml5_Y_D3",
        "http://sestat.baidu.com":"https://sp1.baidu.com/5b1ZeDe5KgQFm2e88IuM_a",
        "http://eclick.baidu.com":"https://sp3.baidu.com/-0U_dTmfKgQFm2e88IuM_a",
        "http://api.map.baidu.com":"https://sp2.baidu.com/9_Q4sjOpB1gCo2Kml5_Y_D3",
        "http://ecma.bdimg.com":"https://ss1.bdstatic.com/-0U0bXSm1A5BphGlnYG",
        "http://ecmb.bdimg.com":"https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG",
        "http://t1.baidu.com":"https://ss0.baidu.com/6ON1bjeh1BF3odCf",
        "http://t2.baidu.com":"https://ss1.baidu.com/6OZ1bjeh1BF3odCf",
        "http://t3.baidu.com":"https://ss2.baidu.com/6OV1bjeh1BF3odCf",
        "http://t10.baidu.com":"https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq",
        "http://t11.baidu.com":"https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq",
        "http://t12.baidu.com":"https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq",
        "http://i7.baidu.com":"https://ss0.baidu.com/73F1bjeh1BF3odCf",
        "http://i8.baidu.com":"https://ss0.baidu.com/73x1bjeh1BF3odCf",
        "http://i9.baidu.com":"https://ss0.baidu.com/73t1bjeh1BF3odCf",
        "http://b1.bdstatic.com":"https://ss0.bdstatic.com/9uN1bjq8AAUYm2zgoY3K",
        "http://ss.bdimg.com":"https://ss1.bdstatic.com/5aV1bjqh_Q23odCf",
        "http://opendata.baidu.com":"https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv",
        "http://api.open.baidu.com":"https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv",
        "http://tag.baidu.com":"https://sp1.baidu.com/6LMFsjip0QIZ8tyhnq",
        "http://f3.baidu.com":"https://sp2.baidu.com/-uV1bjeh1BF3odCf",
        "http://s.share.baidu.com":"https://sp0.baidu.com/5foZdDe71MgCo2Kml5_Y_D3",
        "http://bdimg.share.baidu.com":"https://ss1.baidu.com/9rA4cT8aBw9FktbgoI7O1ygwehsv",
        "http://1.su.bdimg.com":"https://ss0.bdstatic.com/k4oZeXSm1A5BphGlnYG",
        "http://2.su.bdimg.com":"https://ss1.bdstatic.com/kvoZeXSm1A5BphGlnYG",
        "http://3.su.bdimg.com":"https://ss2.bdstatic.com/kfoZeXSm1A5BphGlnYG",
        "http://4.su.bdimg.com":"https://ss3.bdstatic.com/lPoZeXSm1A5BphGlnYG",
        "http://5.su.bdimg.com":"https://ss0.bdstatic.com/l4oZeXSm1A5BphGlnYG",
        "http://6.su.bdimg.com":"https://ss1.bdstatic.com/lvoZeXSm1A5BphGlnYG",
        "http://7.su.bdimg.com":"https://ss2.bdstatic.com/lfoZeXSm1A5BphGlnYG",
        "http://8.su.bdimg.com":"https://ss3.bdstatic.com/iPoZeXSm1A5BphGlnYG"
    }';

    $domain = json_decode($baidu_domain, true);
    foreach($domain as $k=>$v){
        $str = str_replace($k, $v, $str);
    }

    return $str;
}


$wd = '仙剑奇侠传';
$url = 'http://www.baidu.com/s?wd='.urlencode($wd);
$data = array();
$header = array();

$response = doCurl($url, $data, $header, 5);
echo cdomain($response); // 调用域名转换
```

增加域名转换后，所有的图片都可以正常显示。

这里写图片描述

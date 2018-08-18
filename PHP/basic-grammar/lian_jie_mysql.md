# 连接 MySQL

# 连接 MySQL
PHP 5 及以上版本建议使用以下方式连接 MySQL :
+ MySQLi extension ("i" 意为 improved)
+ PDO (PHP Data Objects)
在 PHP

早起版本中我们使用 MySQL 扩展。但该扩展在 2012 年开始不建议使用。


PDO 应用在 12 种不同数据库中， MySQLi 只针对 MySQL 数据库。

两者都是面向对象, 但 MySQLi 还提供了 API 接口。

两者都支持预处理语句。 预处理语句可以防止 SQL 注入，对于 web 项目的安全性是非常重要的。

个人建议PDO

[PDO 安装](http://php.net/manual/zh/pdo.installation.php)

[MySQLi 安装](http://php.net/manual/zh/mysqli.installation.php)

通过 phpinfo() 查看是否安装成功。

## MySQLi - 面向对象


```
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// 创建连接
$conn = new mysqli($servername, $username, $password);

// 检测连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
echo "连接成功";

$conn->close();
?>
```

## MySQLi - 面向过程

```
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// 创建连接
$conn = mysqli_connect($servername, $username, $password);

// 检测连接
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "连接成功";

mysqli_close($conn);
?>
```
## PDO

```
<?php
$servername = "localhost";
$username = "username";
$password = "password";

try {
    $conn = new PDO("mysql:host=$servername;dbname=myDB", $username, $password);
    echo "连接成功"; 
}
catch(PDOException $e)
{
    echo $e->getMessage();
}

$conn = null;
?>


```

PDO 在连接过程需要设置数据库名。如果没有指定，则会抛出异常。



连接在脚本执行完后会自动关闭。也可以使用代码来关闭连接。
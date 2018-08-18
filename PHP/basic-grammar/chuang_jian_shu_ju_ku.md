# 创建数据库



CREATE DATABASE 语句用于在 MySQL 中创建数据库。

## MySQLi 

### 面向对象


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

// 创建数据库
$sql = "CREATE DATABASE myDB";
if ($conn->query($sql) === TRUE) {
    echo "数据库创建成功";
} else {
    echo "Error creating database: " . $conn->error;
}

$conn->close();
?>
```

### 面向过程


```
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// 创建连接
$conn = mysqli_connect($servername, $username, $password);
// 检测连接
if (!$conn) {
    die("连接失败: " . mysqli_connect_error());
}

// 创建数据库
$sql = "CREATE DATABASE myDB";
if (mysqli_query($conn, $sql)) {
    echo "数据库创建成功";
} else {
    echo "Error creating database: " . mysqli_error($conn);
}

mysqli_close($conn);
?>

```

## PDO

使用 PDO 的最大好处是在数据库查询过程出现问题时可以使用异常类来 处理问题。如果 try{ } 代码块出现异常，脚本会停止执行并会跳到第一个 catch(){ } 代码块执行代码。
```
<?php 
$servername = "localhost"; 
$username = "username"; 
$password = "password"; 

try { 
    $conn = new PDO("mysql:host=$servername;dbname=myDB", $username, $password); 

    // 设置 PDO 错误模式为异常 
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); 
    $sql = "CREATE DATABASE myDBPDO"; 

    // 使用 exec() ，因为没有结果返回 
    $conn->exec($sql); 

    echo "数据库创建成功<br>"; 
} 
catch(PDOException $e) 
{ 
    echo $sql . "<br>" . $e->getMessage(); 
} 

$conn = null; 
?>
```

##命令行

```
mysql> CREATE DATABASE books;
```
创建数据库。




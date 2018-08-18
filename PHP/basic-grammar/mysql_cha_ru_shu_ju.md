# MySQL 插入数据
mysqli_multi_query() 函数可用来执行多条SQL语句。

语法规则：
+ PHP 中 SQL 查询语句必须使用引号
+ 在 SQL 查询语句中的字符串值必须加引号
+ 数值的值不需要引号
+ NULL 值不需要引号

INSERT INTO 语句通常用于向 MySQL 表添加新的记录：
`INSERT INTO table_name (column1, column2, column3,...)
VALUES (value1, value2, value3,...)`

指定的值按照出现的顺序添加到表的列。

需要添加部分或者不同的顺序添加，则在列部分给出指定的列。也可以使用一下语法：

```
insert into customers set name="wang", address="daxuecehng",city="cq";
```

## 面向对象
```
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// 检测连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', 'john@example.com')";

if ($conn->query($sql) === TRUE) {
    echo "新记录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

## 面向过程
```
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建连接
$conn = mysqli_connect($servername, $username, $password, $dbname);
// 检测连接
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', 'john@example.com')";

if (mysqli_query($conn, $sql)) {
    echo "新记录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
```
## PDO
```
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDBPDO";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // 设置 PDO 错误模式，用于抛出异常
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "INSERT INTO MyGuests (firstname, lastname, email)
    VALUES ('John', 'Doe', 'john@example.com')";
    // 使用 exec() ，没有结果返回 
    $conn->exec($sql);
    echo "新记录插入成功";
}
catch(PDOException $e)
{
    echo $sql . "<br>" . $e->getMessage();
}

$conn = null;
?>
```
## 修改数据表
添加一列
```

mysql> ALTER TABLE tb-name ADD column
```

删除列：
```

mysql> ALTER TABLE tb-name DROP column
```


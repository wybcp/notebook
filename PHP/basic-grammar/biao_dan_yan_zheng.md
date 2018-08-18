# 表单验证

## 

`$_SERVER["PHP_SELF"]`是超级全局变量，返回当前正在执行脚本的文件名，与 document root相关。

` $_SERVER["PHP_SELF"] `会发送表单数据到当前页面，而不是跳转到不同的页面。

什么是 `htmlspecialchars()`方法?

`htmlspecialchars() `函数把一些预定义的字符转换为 HTML 实体。

预定义的字符是：

+ & （和号） 成为 &amp;
+ " （双引号） 成为 &quot;
+ ' （单引号） 成为 &#039;
+ < （小于） 成为 &lt;
+ > （大于） 成为 &gt;


`$_SERVER["PHP_SELF"] `可以通过 `htmlspecialchars() `函数来避免被hacker利用。

当用户提交表单时，我们将做以下两件事情，：
+ 使用 PHP trim() 函数去除用户输入数据中不必要的字符 (如：空格，tab，换行)。
+ 使用PHP stripslashes()函数去除用户输入数据中的反斜杠 (\\)

`test_input()`函数来检测` $_POST` 中的所有变量, 脚本代码如下所示：
实例
```<?php
// 定义变量并默认设置为空值
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST")
{
  $name = test_input($_POST["name"]);
  $email = test_input($_POST["email"]);
  $website = test_input($_POST["website"]);
  $comment = test_input($_POST["comment"]);
  $gender = test_input($_POST["gender"]);
}

function test_input($data)
{
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>
```

### PHP - 验证名称

检测 name 字段是否包含字母和空格，如果 name 字段值不合法，将输出错误信息：
```
$name = test_input($_POST["name"]);
if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
  $nameErr = "只允许字母和空格"; 
}
```
#### preg_match — 进行正则表达式匹配。

语法：
`
int preg_match ( string $pattern , string $subject [, array $matches [, int $flags ]] )`

在 subject 字符串中搜索与 pattern 给出的正则表达式相匹配的内容。如果提供了 matches ，则其会被搜索的结果所填充。$matches[0] 将包含与整个模式匹配的文本，$matches[1] 将包含与第一个捕获的括号中的子模式所匹配的文本，以此类推。

### PHP - 验证邮件
检测 e-mail 地址是否合法：
```
$email = test_input($_POST["email"]);
if (!preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/",$email)) {
  $emailErr = "非法邮箱格式"; 
}
```

### PHP - 验证 URL
将检测URL地址是否合法 (以下正则表达式运行URL中含有破折号:"-")：
```
$website = test_input($_POST["website"]);
if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)) {
  $websiteErr = "非法的 URL 的地址"; 
}
```
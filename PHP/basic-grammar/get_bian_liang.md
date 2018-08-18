# $_GET 变量

## $_GET 变量

预定义的 $_GET 变量用于收集来自 method="get" 的表单中的值。

从带有 GET 方法的表单发送的信息，对任何人都是可见的（会显示在浏览器的地址栏），并且对发送信息的量也有限制。

当用户点击 "Submit" 按钮时，发送到服务器的 URL 如下所示：
`http://www.runoob.com/welcome.php?fname=Runoob&age=3`

表单域的名称(name)会自动成为 $_GET 数组中的键.

注释：HTTP GET 方法不适合大型的变量值。它的值是不能超过 2000 个字符的。
# JSON

JavaScript object notation

一种结构化数据格式，表示三种类型的值：

- 简单值：字符串、数值、布尔值、null
- 对象：一组无序的键值对
- 数组：一组有序的值的列表。

JSON 字符串必须使用双引号。

对象的属性必须加双引号。

早版本浏览器使用[shim](https://github.com/douglascrockford/JSON-js)解析 JSON.

JSON.stringify()将 JavaScript 对象序列化，可以接受两个参数：第一个参数是过滤器（数组和函数);第二个参数是字符串缩进，数值或者字符串，换行显示。

JSON.parse()解析。

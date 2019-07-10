# 引用类型

## Object 类型

两种方式创建 Object：

- 使用 new 操作符后跟 Object 构造函数：`var person = new Object();person.name="wyb"`；
- 对象字面量表示法（推荐）：`var person={name:"wyb",age:27}`。

访问对象属性时可使用点表示法(常用)或者方括号表示法（特殊情况下使用，通过变量访问属性）。

## Array 类型

数组可以保存任何类型的数据，大小动态调节。

### 检测数组检测数组

`Array.isArray()`;

`instanceof（）`检测位于一个网页或者一个全局作用域的数组。

### 转换方法数组继承的

`toLocaleString()`,`toString()`,`valueOf()`方法，在默认情况下以逗号分隔的字符串形式返回数组项，而使用`join（）`方法，可以使用不同的分隔符构建字符串。

### 栈方法 LIFO

`push（）`方法接受任意数量的参数，并添加到数组尾部，返回修改后数组的长度；`pop（）`删除最后一个，返回移除项。

### 队列方法

FIFO

shift（）方法移除数组第一项并返回该值。

unshift（）方法在数组前端添加任意个项并返回新数组的长度。

### 重排序方法

reverse（）方法反转数组项的顺序。

sort（）方法按升序排列数组项，调用每个数组项的 toString（）方法，比较数组项的字符串大小。

### 操作方法

concat（）

slice（）

splice（）

### 位置方法

indexOf（）

lastIndexOf（）

### 迭代方法

every（）

filter(()

forEach()

map()

some()

### 归并方法

reduce（）

reduceRight（）

## Date（）

在调用 Date 构造函数而不传递参数的情况下，新创建的对象自动获得当前日期和时间。

## RegExp 类型

var expression=/pattern/falgs

pattern 表示正则表达式；

flags：

- g（global）：全局模式
- i（ingoreCase）:忽略大小写
- m：多行模式

## Number 类型

调用 Number 构造函数传递相应的数值。

toString（）：传递一个表示基数的参数，返回几进制的字符串。

toFixed（）：按指定的小数位返回数值的字符串。

toExponential（）:返回指数表示法，传参指定输出小数位。

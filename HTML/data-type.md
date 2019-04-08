# 数据类型

Undefined、null、Boolean、number、string 五种基本数据类型和一种复杂数据类型 object。

Object 本质上是一组无序的名值对组成。

## typeof（）

使用 typeof 操作符检测变量的数据类型。

对于尚未声明的变量，只能使用 typeof 操作符检测数据类型这一项操作，其返回值为 undefined。未初始化和未声明的变量返回相同的值，这是应为虽然技术上有本质的区别，但是无论哪种变量都不能执行真正的操作。

## undefined

null 表示一个空对象指针（检测 null 返回 object 的原因）。如果定义的变量在将来用于保存对象，最好将变量初始化为 null。undefined 派生自 null，所以它们之间相等操作返回 true。

## Boolean

使用转换函数 Boolean()转换为对应的 Boolean 值。

| 数据类型  | 转换为 true | 转换为 false   |
| --------- | ----------- | -------------- |
| Boolean   | true        | false          |
| string    | 非空字符串  | ""（空字符串） |
| Number    | 非零        | 0 和 NaN       |
| Object    | 任何对象    | null           |
| undefined | 不适用      | undefined      |

## Number

### 八进制

第一位必须是零，然后是八进制数字序列（0~7），如果数值超出范围，则前导零将被忽略，后面的数值作为十进制解析。八进制在严格模式下是无效的，抛出错误。

### 十进制

十进制前面两位必须是 0x。

### 浮点数值

所谓的浮点数值，就是该数值中必须包括一个小数点，且小数点后面必须有一个数字。由于保存浮点数值需要的空间是整数数值的两倍，因此有时会将浮点数值转换为整数值，例如浮点数值本身是一个整数值（如 1.0）。浮点数值的最高精度是 17 位小数。

最小数值为 Number.MIN_VALUE =5e-324，最大数值为 Number.MAX_VALUE=1.7976931348623157e+308。Number.NEGATIVE_INFINITY 负无穷-infinity，Number.POSITIVE_INFINITY 正无穷 Infinity。

通过 isFinite（）函数判断一个数值是否有穷的。

### NaN

NaN:not a number,一个特殊的数值，用于表示一个本来要返回数值的操作数未返回数值的情况。其本身有两个特点：

- 任何涉及 NaN 的操作都返回 NaN；
- NaN 与任何值不相等。

isNaN（）函数，接受一个参数，确定该参数是否“不是数值”。不能被转换为数值的值返回 true。

### 数制转换

- Number（）
- parseInterface（）
- parseFloat（）

## String

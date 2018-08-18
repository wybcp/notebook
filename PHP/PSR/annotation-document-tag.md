# 注释文档标记

文档标记的使用范围是指该标记可以用来修饰的关键字，或其他文档标记。
所有的文档标记都是在每一行的 \* 后面以@开头。如果在一段话的中间出来@的标记，这个标记将会被当做普通内容而被忽略掉。

## @access

使用范围：class,function,var,define,module

该标记用于指明关键字的存取权限：private、public 或 proteced

## @author

该标记用于指明编码作者

## @copyright

使用范围：class，function，var，define，module，use

该标记用于指明版权信息

## @deprecated

使用范围：class，function，var，define，module，constent，global，include

该标记用于指明不用或者废弃的关键字

## @example

该标记用于解析一段文件内容，并将他们高亮显示。Phpdoc 会试图从该标记给的文件路径中读取文件内容

## @const

使用范围：define

该标记用来指明 php 中 define 的常量

## @final

使用范围：class,function,var

该标记用于指明关键字是一个最终的类、方法、属性，禁止派生、修改。

## @filesource

该标记和 example 类似，只不过该标记将直接读取当前解析的 php 文件的内容并显示。

## @global

该标记用于指明在此函数中引用的全局变量

## @ingore

该标记用于在文档中忽略指定的关键字

## @license

该标记相当于 html 标签中的,首先是 URL，接着是要显示的内容

例如`[url=http://blog.emtalk.net/ "http://blog.emtalk.net"]PHP 入门学习[/url]`
可以写作 `@license http://blog.emtalk.net PHP 入门学习`

## @link

该标记类似于 license
但还可以通过 link 指到文档中的任何一个关键字

## @name

该标记为关键字指定一个别名。

## @package

使用范围：页面级别的-> define，function，include

类级别的->class，var，methods

该标记用于逻辑上将一个或几个关键字分到一组。

## @abstrcut

该标记用于说明当前类是一个抽象类

## @param

该标记用于指明一个函数的参数

## @return

该标记用于指明一个方法或函数的返回指

## @static

该标记用于指明关建字是静态的。

## @var

该标记用于指明变量类型

## @version

该标记用于指明版本信息

## @todo

该标记用于指明应该改进或没有实现的地方

## @throws

该标记用于指明此函数可能抛出的错误异常,极其发生的情况

上面提到过，普通的文档标记标记必须在每行的开头以@标记，除此之外，还有一种标记叫做 inline tag,用{@}表示，具体包括以下几种：

`{@link}`用法同@link

`{@source}`显示一段函数或方法的内容

范例：

```php
/**
 * @author Author Name [<author@email.com>] 代码编写人(负责人)
 * @version xx.xx 当前版本号
 * @param datatype $v_name[,...] description 函数相关联的参数，含有,...表示可传入不定数量的其他参数
 * @return datatype description 函数或方法的返回值类型
 * @global datatype description 全局变量的说明(仅对 phpDocumentor 解析器起作用)
 * @var datatype 在类中说明类变量(属性)的类型
 * @example [path|url] description 举一个例子，以阐释使用方法
 * @todo description 待完成的工作信息或待解决的问题信息
 */
```

# HTML5 display definitions

为所有的浏览器添加HTML5添加样式。

1. 大多数浏览器默认将无法识别的元素作为行内元素处理，所以强制定义block。
```
/* ::: HTML5 display definitions ::: */
/**
 * Correct `block` display not defined in IE 8/9.
 */
article,
aside,
figcaption,
figure,
footer,
header,
main,
nav,
section {
  display: block;
}```
2. [HTML5 shiv](https://github.com/aFarkas/html5shiv/)
  1. 在每个页面的head元素中添加以下代码：
  ```
  <!--[if lt IE 9]>
		<script src="html5shiv.js"></script>
	<![endif]-->
  ```
  注意html5 shiv 是少有的必须在head中加载的js文件。
  
  
  
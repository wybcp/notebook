# float

## 属性

### 改变display

float会隐式改变display的计算值，具体如下表：

指定值  |计算值
---------|-
inline|block
inline-block | block
inline-table | block
table_row | block

## 清除浮动
浮动可能造成后面的元素布局紊乱，需要清除浮动影响，使用下面方法：

1. clear属性`{clear:both;}`;

2. overflow属性：应用于浮动元素父元素或者祖先元素
	
	在具有浮动元素的父容器中设置`overflow`的属性值为`auto`，这样父容器获得一个高度。

	在IE6里面，父容器是需要设置一个`width`和`height`。因为高度可能是一个变量，宽度为100%，他们将能正常的工作。使用`overflow:auto;`,在IE浏览器中会给元素添加滚动条，最好是直接使用`overflow:hidden;`来清除浮动。

		{
		  width:100%;
		  overflow:auto(or hidden);
		  zoom:1;//兼容IE6
		}
3. [clearfix技巧](http://www.w3cplus.com/css/advanced-html-css-lesson2-detailed-css-positioning.html)：让容器自身具有清除浮动的能力，复杂但更好，应用于浮动元素父元素或者祖先元素。

	`clearfix`技巧是基于在父元素上使用`:before`和`:after`两个伪类。使用这些伪类，我们可以在浮动元素的父容器前面和后面创建隐藏元素。`:before`伪类是用来防止子元素顶部的外边距塌陷，使用`display: table`创建一个匿名的`table-cell`元素。这也确保在IE6和IE7下具有一致性。`:after`伪类是用来防止子元素的底部的外边距塌陷，以及用来清除元素的浮动。
	
	在IE6和7的浏览器中，加上`*zoom`属性来触发父元素的hasLayout的机制。决定了元素怎样渲染内容，以及元素与元素之间的相互影响。
	
		.box-set:before,
		.box-set:after {
		  content: "";
		  display: table;
		}
		.box-set:after {
		  clear: both;
		}
		.box-set {
		  *zoom: 1;
		}

添加box-set类。





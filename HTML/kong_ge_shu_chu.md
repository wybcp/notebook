# 空格输出

因为浏览器显示机制，对手动敲入的空格，将连续多个空格显示成 1 个空格。解决方法:

1. 使用输出 html 标签&nbsp;来解决 `document.write("&nbsp;&nbsp;"+"1"+"&nbsp;&nbsp;&nbsp;&nbsp;"+"23");` 结果:<pre> 1 23</pre>
2. 使用 CSS 样式来解决<pre> `document.write("<span style='white-space:pre;'>"+" 1 2 3 "+"</span>");`</pre>

结果: <pre>`1 2 3`

 </pre>
 在输出时添加`“white-space:pre;”`样式属性。这个样式表示"空白会被浏览器保留"

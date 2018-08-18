# user-select
https://www.qianduan.net/user-select/

保护版权内容的简单方案：使用 user-select 这个CSS属性。
```
 .control-select {
    user-select: none; /* 禁止选择 */
    user-select: auto; /* 浏览器来决定是否允许选择 */
    user-select: all; /* 可以选择任何内容 */
    user-select: text; /* 只能选择文本 */
    user-select: contain; /* 选择绑定的元素以内的内容 */
  }
```

不过，这个属性还并没有被各浏览器以标准的行为来实现，所以使用的适合还是要加上各种前缀：
.no-select {
  -moz-user-select: none; 
  -ms-user-select: none; 
  -webkit-user-select: none; 
}


注意： IE 9 才开始支持，IE 8 及更早期的版本不支持

##Javascript方案

当然也可以用 javascript 来实现类似的行为：
```
//禁用选择
function disableSelection() {  
   document.onselectstart = function() {return false;} // IE 浏览器
   document.onmousedown = function() {return false;} // 其它浏览器
}
//启用选择
function enableSelection() {  
   document.onselectstart = null; // IE 浏览器
   document.onmousedown = null; // 其它浏览器
}
```

当然，js方案可以兼容到低版本 IE 浏览器。

注意：当然对于爬虫和略懂 web 开发的人来说，这些限制完全没有用


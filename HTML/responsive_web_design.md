# responsive web design

##可伸缩图像的创建
1. 在HTML中的img标签省略width和height属性；
2. img应用`max-width:100%`；

HTML5视频及其他媒体可伸缩可使用相同的设置。

##创建弹性布局

设置相对的max-width。

##媒体查询
指向外部样式表的链接：
```
<link rel="stylesheet" media="logic type and(feature value)" 
href=""/>
```
位于样式表中的媒体查询：
```
@media logic type and(feature value){

}
```
+ logic部分可选，其值为only或not
+ type部分是媒体类型

##viewport
设备像素和视觉区域不一致的情况下，在页面的head部分添加视觉区域meta元素。
```
<meta name="viewport" content=’width=device-width，initial-scale=1"/>
```

##移动优先，渐进增强

[HTML5 shiv](https://github.com/aFarkas/html5shiv/)

[respond.js](https://github.com/scottjehl/Respond)
```
<head>
<!--[if lt IE 9]>
		<script src="js/html5shiv.js"></script>
		<script src="js/respond.min.js"></script>
	<![endif]-->
</head>
```

```
/* ===================== MEDIA QUERIES ===================== */

/* 320+ 
------------------------------------------ */
@media only screen and (min-width: 20em) {
 
}


/* 480+ 
------------------------------------------ */
@media only screen and (min-width: 30em) {
 
}


/* 480-767-only 
------------------------------------------ */
@media only screen and (min-width: 30em) and (max-width: 47.9375em) {
  
}


/* 600-767-only 
------------------------------------------ */
@media only screen and (min-width: 37.5em) and (max-width: 47.9375em) {
 
}


/* 768+ 
------------------------------------------- */
@media only screen and (min-width: 48em) {
 
}
/* --- end media queries ---- */


/* html5boilerplate.com Clearfix
--------------------------------- */
.clearfix:before,
.clearfix:after {
  content: " ";
  display: table;
}

.clearfix:after {
  clear: both;
}

/*
 * For IE 6/7 only
 * Include this rule to trigger hasLayout and contain floats.
 */
.clearfix {
  *zoom: 1;
}
```

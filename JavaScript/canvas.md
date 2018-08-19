# Canvas

在页面中设置一个区域（width 和 height），通过 JavaScript 动态在这份区域绘制图形。

取得绘图上下文

```
 var drawing = document.getElementById("drawing");

//make sure <canvas> is completely supported
if (drawing.getContext){
    var context = drawing.getContext("2d");
}
```

##2D 上下文

fillStyle 填充

strokeStyle 描边 ###绘制矩形
矩形是唯一一种可以直接在 2D 上下文中绘制的图形。

fillRect(), strokeRect() ,clearReact()：接受四个参数（单位像素）
矩形 X，坐标 Y，坐标宽度和高度。

strokeRect()使用指定的颜色描边。使用 lineWidth 属性控制描边线条的宽度，lineCap 属性控制线条的末端的形状“butt”、“round”、“square”，通过 lineJoin 控制线条的相交方式“round”、“bevel”、“miter”。

rect(x, y, width, height)：绘制一个左上角坐标为（x,y），宽高为 width 以及 height 的矩形。

###绘制路径

图形的基本元素是路径。路径是通过不同颜色和宽度的线段或曲线相连形成的不同形状的点的集合，是闭合的。路径绘制图形的步骤：

1. 要创建路径起始点;
2. 画出路径;
3. 路径封闭;
4. 通过描边或填充路径区域来渲染图形。

以下是所要用到的函数：

- beginPath():新建一条路径，生成之后，图形绘制命令被指向到路径上生成路径。
- closePath():闭合路径之后图形绘制命令又重新指向到上下文中。
- stroke():通过线条来绘制图形轮廓。
- fill():通过填充路径的内容区域生成实心的图形。
- moveTo(x, y):移动到指定的坐标 x 以及 y 上,通常用于设置起点，绘制一些不连续的路径。
- lineTo(x, y)：绘制一条从当前位置到指定 x 以及 y 位置的直线。

本质上，路径是由很多子路径构成，这些子路径都是在一个列表中，所有的子路径（线、弧形、等等）构成图形。

注意：当你调用 fill()函数时，所有没有闭合的形状都会自动闭合，所以你不需要调用 closePath()函数。但是调用 stroke()时不会自动闭合。

####圆弧
arc(x, y, radius, startAngle, endAngle, anticlockwise)：画一个以（x,y）为圆心的以 radius 为半径的圆弧（圆），从 startAngle 开始到 endAngle 结束，参数 anticlockwise 为一个布尔值，默认为顺时针 false， 逆时针方向 true。

arc()函数中的角度单位是弧度，不是度数。角度与弧度的 js 表达式:radians=(Math.PI/180)\*degrees。

####贝塞尔（bezier）

二次以及三次贝塞尔曲线都十分有用，一般用来绘制复杂有规律的图形。

- quadraticCurveTo(cp1x, cp1y, x, y)：绘制二次贝塞尔曲线，x,y 为结束点，cp1x,cp1y 为控制点。
- bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)：绘制三次贝塞尔曲线，x,y 为结束点，cp1x,cp1y 为控制点一，cp2x,cp2y 为控制点二。

##colors
fillStyle = color：设置图形的填充颜色。

strokeStyle = color：设置图形轮廓的颜色。

默认情况下，线条和填充颜色都是黑色（CSS 颜色值 #000000）。而设置了 strokeStyle 或者 fillStyle 的值，那么这个新值就会成为新绘制的图形的默认值。

##绘制文本

- fillText(text, x, y [, maxWidth])：在指定的(x,y)位置填充指定的文本，绘制的最大宽度是可选的.
- strokeText(text, x, y [, maxWidth])：在指定的(x,y)位置绘制文本边框，绘制的最大宽度是可选的.
- font = value：用来绘制文本的样式。
- textAlign = value ：文本对齐选项. 可选的值包括：start, end, left, right or center. 默认值是 start。
- textBaseline = value：基线对齐选项. 可选的值包括：top, hanging, middle, alphabetic, ideographic, bottom。默认值是 alphabetic。
- direction = value：文本方向。可能的值包括：ltr, rtl, inherit。默认值是 inherit
- measureText()：将返回一个 TextMetrics 对象的宽度、所在像素等体现文本特性的属性。

##变换
save()：Canvas 状态是以堆（stack）的方式保存的，每一次调用 save 方法，当前的状态就会被推入堆中保存起来。

restore()：每一次调用 restore 方法，上一个保存的状态就从堆中弹出，所有设定都恢复。

save 和 restore 方法是用来保存和恢复 canvas 状态的，都没有参数。Canvas 的状态就是当前画面应用的所有样式和变形的一个快照。

translate(x, y)：x 是左右偏移量，y 是上下偏移量。

rotate(angle)：旋转的角度(angle)，它是顺时针方向的，以弧度为单位的值。

scale(scaleX, scaleY)：scaleX, scaleY 分别是横轴和纵轴的缩放因子，必须是正值。值比 1.0 小表示缩小，比 1.0 大则表示放大，值为 1.0 时什么效果都没有。

transform(m11, m12, m21, m22, dx, dy)：直接修改变换矩阵，即乘以如下矩阵

```
m11 m21 dx
m12 m22 dy
0 	0 	1
```

##[绘制图像](https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial/Using_images)
drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)：
其中 image 是 image 或者 canvas 对象；x 和 y 是其在目标 canvas 里的起始坐标；sWidth 和 sHeight，表示目标宽度和高度，用于缩放；后四个用于切片目标的位置和大小。

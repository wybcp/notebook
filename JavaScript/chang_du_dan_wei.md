# 长度单位

1. em：相对单位，参考物是父元素的font-size，具有继承的特点。如果字体大小是16px（浏览器的默认值），那么 1em = 16px。简化换算（1em = 10px ）：
```
body {
  font-size:62.5%;
}
```

2. 百分比：百分比一般宽泛的讲是相对于父元素，但并不十分准确。
  + 对于普通定位元素就是我们理解的父元素
  + 对于position: absolute;的元素是相对于已定位的父元素（offset parent）
  + 对于position: fixed;的元素是相对于 ViewPort

3. rem：rem支持IE9及以上，意思是相对于根元素html（网页）
```
html {
  font-size:62.5%;/**10 ÷ 16 × 100% = 62.5%    1rem = 10px   **/
  }   
body {
  font-size:1.4rem;/**1.4 × 10px = 14px **/
  }
h1 { 
  font-size:2.4rem;/**2.4 × 10px = 24px**/
  }
```

4. vh 和 vw：
  vw Viewport宽度， 1vw 等于viewport宽度的1%；
  vh Viewport高度， 1vh 等于viewport高的的1%。

5. vmin和vmax：IE10+ 和现代浏览器都已经支持vmin，
  webkit浏览器之前不支持vmax，新版已经支持，所有现代浏览器已经支持，但是IE全部不支持vmax，
 +  vmin vw和vh中比较小的值
  + vmax vw和vh中比较大的值

6. ch和ex：IE9+ 和现代浏览器都已经支持,这两个单位时根据 当前font-family 的相对单位。
  + ch 字符0的宽度
 + ex 小写字符x的高度

7.line-height百分比
  
  行高带单位和不带单位的区别：
  line-height:26px;表示行高为26个像素
  line-heigth:120%;表示行高为当前字体大小的120%
  line-height:2.6em;表示行高为当前字体大小的2.6倍
  带单位的行高都有继承性，其子元素继承的是计算值，如父元素的字体大小为14px，定义行高line-height:2em;则计算值为 28px，不会因其子元素改变字体尺寸而改变行高。(例如：父元素14px，子元素12px,那么行高就是28px，子元素虽然字体是12，行高还是父元素的行高)
  line-height:2.6;表示行高为当前字体大小的2.6倍
  不带单位的行高是直接继承，而不是计算值，如父元素字体尺寸为14px，行高line-height:2;他的行高为28px;子元素尺寸为12px，不需要再定义行高，他默认的行高为24px。（例如：子元素12px，他的行高是24,不会继承父元素的28）

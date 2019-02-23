# flexbox

## Flexbox 简介

flexbox 为了解决复杂的 web 布局布局方式很灵活。容器的子元素可以任意方向进行排列。此属性目前处于非正式标准，以下是各浏览器对 flexbox 的支持程度，在较新的浏览器中基本可以使用该属性。

![浏览器支持情况](https://sfault-image.b0.upaiyun.com/271/600/2716002657-56fde33ed34c2_articlex)

## Flexbox 模型

flex 布局依赖于 flex directions.简单的说：Flexbox 是布局模块，而不是一个简单的属性，它包含父元素(flex container)和子元素(flex items)的属性。

- 主轴、主轴方向(main axis |main dimension)：用户代理沿着一个伸缩容器的主轴配置伸缩项目，主轴是主轴方向的延伸。
- 主轴起点、主轴终点(main-start |main-end)：伸缩项目的配置从容器的主轴起点边开始，往主轴终点边结束。
- 主轴长度、主轴长度属性(main size |main size property)：伸缩项目的在主轴方向的宽度或高度就是项目的主轴长度，伸缩项目的主轴长度属性是 width 或 height 属性，由哪一个对着主轴方向决定。
- 侧轴、侧轴方向(cross axis |cross dimension)：与主轴垂直的轴称作侧轴，是侧轴方向的延伸。
- 侧轴起点、侧轴终点(cross-start |cross-end)：填满项目的伸缩行的配置从容器的侧轴起点边开始，往侧轴终点边结束。
- 侧轴长度、侧轴长度属性(cross size |cross size property)：伸缩项目的在侧轴方向的宽度或高度就是项目的侧轴长度，伸缩项目的侧轴长度属性是"width"或"height"属性，由哪一个对着侧轴方向决定。

![Flexbox model](https://segmentfault.com/image?src=http://img.blog.csdn.net/20150614222502311&objectId=1190000002910324&token=fa57b0c157bd4d74243425778f0b707e)

## Flexbox 使用示例

### 水平竖直居中

在 Flex 容器中，当项目边距设置为“auto”时，设置自动的垂直边距将使该项目完全集中两个轴。

```css
.child {
  margin: auto;
}
```

## Flexbox 属性

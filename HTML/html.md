#HTML5

`small`元素：In HTML5, this element is repurposed to represent side-comments and small print, including copyright and legal text, independent of its styled presentation.免责声明、注解、署名、版权。

搜索引擎可能根据`lang`属性指定语言区分搜索结果。

`title`属性：搜索引擎会将title作为判断页面的指标，并建立相关的索引。

创建分级从高到低标题时，避免跳过某些级别。副标题使用段落。

不能在header里面嵌套footer或者另一个header。

nav使用准则：对文档或网站重要的链接群。

一个页面只用一次main。

article元素表示文档、页面、应用或网站中的一个独立的容器。

section标记的是页面中的特定区域，而div不传达语义。

div与span都是无语义容器。

img元素同时拥有title和alt属性，提示框采用title属性的内容。

strong标记重要文本（粗体），重要程度；em标示内容的着重点，强调作用。

blockquote引述块级文本，q引述行内文本，不同语言用lang设置。

time包含datetime属性，文本内容可以任何形式表示时间，否则必须是合法的日期或时间格式。机器可读的时间格式：YYYY-MM-DDThh:mm:ss，当地时间；YYYY-MM-DDThh:mm:ssZ，世界时。小时采用24小时制。时间段的表现形式：nh nm ns

abbr标记缩写词，同时应该在缩写词的括号放入全称。

sub创建下表，sup创建上标。上下标会轻微的要乱行间距。
```
/*防止sub和sup对line-height的影响*/
sub,sup{
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup{
  top:-0.5em;
}
sub{
  bottom: -0.25em;
}
```

address定义与玉面相关的作者、相关人士、组织的联系方式。

ins添加内容，del删除内容。主要用于展示内容的变化。

pre预处理化的文本可以保持文本固有的换行和空格，可以用于计算机代码展示。等宽字体显示。

如果图像是页面设计的一部分，而不是内容的一部分，使用background-image引入图像。

favorites icon收藏夹图标：16*16.favicon.ico放入网站的根目录。




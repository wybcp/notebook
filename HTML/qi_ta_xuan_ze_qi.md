# 其他选择器

## 伪元素选择器

伪元素是 HTML 中并不存在的元素注意与伪类学则器的区分。

- `::first-letter`IE6+(第一个字母前面的标点符号会被当成第一个字母的一部分，一同格式化)
- `::first-line` IE6+
- `::before{content: "before"}` 需与 content 一同使用 IE8+
- `::after{content: "after"}`需与 content 一同使用 IE8+
- `::selection`被用户选中的内容（鼠标选择高亮属性）IE9+ Firefox 需用 -moz 前缀

## 组合选择器

- 后代选择器`.main h2 {...}`，使用 表示 IE6+
- 子选择器`.main>h2 {...}`，使用>表示 IE7+
- 兄弟选择器`h2+p {...}`，使用+表示 IE7+
- `h2~p {...}`，使用~表示（此标签无需紧邻）IE7+

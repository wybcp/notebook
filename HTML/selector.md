# 简单选择器

- 标签选择器
- 类选择器：`.className`以 `.`开头，名称可包含字母，数字，`-`，`_`，但必须以字母开头。
- id 选择器:#idName 以 # 开头且只可出现一次;
- 通配符选择器:`*`;
- 属性选择器

  - [attr] 或 [attr=val] 来选择相应的元素。IE7+
  - [attr~=val] 可选用与选择包含 val 属性值的元素， IE7+
  - [attr|=val] 可以选择 val-开头的属性值。IE7+
  - [attr^=val] 可选择以 val 开头的属性值对应的元素，如果值为符号或空格则需要使用引号 ""。IE7+
  - [attr$=val] 可选择以 val 结尾的属性值对应的元素。IE7+
  - [attr*=val] 可选择以包含 val 属性值对应的元素。IE7+

- 伪类选择器
  - :link IE6+
  - :visited IE7+
  - :hover IE6 中仅可用于链接
  - :active IE6/7 中仅可用于链接
  - :enabled IE9+
  - :disabled IE9+
  - :checked IE9+
  - :first-child IE8+
  - :last-child IE9+
  - :nth-child(even) 可为 odd even 或数字 IE9+;指父元素下第 n 个元素且元素为 element，若不是，选择失败。
  - :nth-last-child(n) n 从 0 开始计算 IE9+
  - :only-child 仅选择唯一的元素 IE9+
  - :only-of-type IE9+
  - :first-of-type IE9+
  - :last-of-type IE9+
  - :nth-of-type(even) IE9+指父元素下第 n 个 element 元素
  - :nth-last-of-type(2n) IE9+

[选择符](https://li-xinyang.gitbooks.io/frontend-notebook/content/chapter1/04_02_selector.html)

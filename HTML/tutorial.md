# [tutorial](http://www.sass.hk/sass-course.html)

<!--atoc-->

##变量

sass 的一个重要特性就是它为 css 引入了变量。你可以把反复使用的 css 属性值定义成变量，然后通过变量名来引用它们。或者，对于仅使用过一次的属性值，你可以赋予其一个易懂的变量名，让人一眼就知道这个属性值的用途。

sass 使用$符号来标识变量。为什么选择$ 符号呢？因为它好认、更具美感，且在 CSS 中并无他用，不会导致与现存或未来的 css 语法冲突。

### 变量声明

sass 变量的声明和 css 属性的声明很像，例如：
`$highlight-color: #F90;`

与 CSS 属性不同，变量可以在 css 规则块定义之外存在。当变量定义在 css 规则块内，那么该变量只能在此规则块内使用：

````
$nav-color: #F90;
nav {
  $width: 100px;
  width: $width;
  color: $nav-color;
}

//编译后

nav {
  width: 100px;
  color: #F90;
}```
在这段代码中，$nav-color这个变量定义在了规则块外边，所以在这个样式表中都可以像 nav规则块那样引用它。$width这个变量定义在了nav的{ }规则块内，所以它只能在nav规则块内使用。

### 变量引用

凡是css属性的标准值（比如说1px或者bold）可存在的地方，变量就可以使用。

在声明变量时，变量值也可以引用其他变量。当你通过粒度区分，为不同的值取不同名字时，这相当有用。下例在独立的颜色值粒度上定义了一个变量，且在另一个更复杂的边框值粒度上也定义了一个变量：

###变量名用中划线还是下划线分隔;

sass的变量名可以与css中的属性名和选择器名称相同，包括中划线和下划线。使用中划线的方式更为普遍，这也是compass和本文都用的方式。

## 嵌套CSS 规则;

sass用了两步，每一步都是像打开俄罗斯套娃那样把里边的嵌套规则块一个个打开。

首先，把#content（父级）这个id放到article选择器（子级）和aside选择器（子级）的前边：
````

#content {
article {
h1 { color: #333 }
p { margin-bottom: 1.4em }
}
aside { background-color: #EEE }
}
/_ 编译后 _/
#content article h1 { color: #333 }
#content article p { margin-bottom: 1.4em }
#content aside { background-color: #EEE }

```
然后，#content article里边还有嵌套的规则，sass重复一遍上边的步骤，把新的选择器添加到内嵌的选择器前边。

大多数情况下这种简单的嵌套都没问题，但是有些场景下不行，比如你想要在嵌套的选择器里边立刻应用一个类似于：hover的伪类。为了解决这种以及其他情况，sass提供了一个特殊结构&。

###父选择器的标识符&

在使用嵌套规则时，父选择器能对于嵌套规则如何解开提供更好的控制。它就是一个简单的&符号，且可以放在任何一个选择器可出现的地方，比如h1放在哪，它就可以放在哪。
```

article a {
color: blue;
&:hover { color: red }
}

```
当包含父选择器标识符的嵌套规则被打开时，它不会像后代选择器那样进行拼接，而是&被父选择器直接替换：
```

article a { color: blue }
article a:hover { color: red }

```
在为父级选择器添加：hover等伪类时，这种方式非常有用。同时父选择器标识符还有另外一种用法，你可以在父选择器之前添加选择器。

###群组选择器的嵌套

sass的嵌套特性在这种场景下也非常有用。当sass解开一个群组选择器规则内嵌的规则时，它会把每一个内嵌选择器的规则都正确地解出来：
```

.container {
h1, h2, h3 {margin-bottom: .8em}
}

```
首先sass将.container和h1.container和h2.container和h3分别组合，然后将三者重新组合成一个群组选择器，生成你前边看到的普通css样式。
```

.container h1, .container h2, .container h3 {
margin-bottom: .8em; }

```
对于内嵌在群组选择器内的嵌套规则，处理方式也一样：
nav, aside {
  a {color: blue}
}
首先sass将nav和aaside和a分别组合，然后将二者重新组合成一个群组选择器：
```

nav a, aside a {color: blue}

```
###子组合选择器和同层组合选择器：>、+和~

上边这三个组合选择器必须和其他选择器配合使用，以指定浏览器仅选择某种特定上下文中的元素。
```

article section { margin: 5px }
article > section { border: 1px solid #ccc }

```
你可以用子组合选择器>选择一个元素的直接子元素。上例中，第一个选择器会选择article下的所有命中section选择器的元素。第二个选择器只会选择article下紧跟着的子元素中命中section选择器的元素。
在下例中，你可以用同层相邻组合选择器+选择header元素后紧跟的p元素：
```

header + p { font-size: 1.1em }

````
你也可以用同层全体组合选择器~，选择所有跟在article后的同层article元素：

```article ~ article { border-top: 1px dashed #ccc }```

这些组合选择器可以应用到sass的规则嵌套中。可以把它们放在外层选择器后边，或里层选择器前边：
````

article {
~ article { border-top: 1px dashed #ccc }

> section { background: #eee }
> dl > {

    dt { color: #333 }
    dd { color: #555 }

}
nav + & { margin-top: 0 }
}

```
sass会如你所愿地将这些嵌套规则一一解开组合在一起：
```

article ~ article { border-top: 1px dashed #ccc }
article > footer { background: #eee }
article dl > dt { color: #333 }
article dl > dd { color: #555 }
nav + article { margin-top: 0 }

```
###嵌套属性

在sass中，除了CSS选择器，属性也可以进行嵌套。
```

nav {
border: {
style: solid;
width: 1px;
color: #ccc;
}
}

```
嵌套属性的规则是这样的：把属性名从中划线-的地方断开，在根属性后边添加一个冒号:，紧跟一个{ }块，把子属性部分写在这个{ }块中
```

nav {
border-style: solid;
border-width: 1px;
border-color: #ccc;
}

```
##导入SASS文件

css有一个特别不常用的特性，即@import规则，它允许在一个css文件中导入其他css文件。然而，后果是只有执行到@import时，浏览器才会去下载其他css文件，这导致页面加载起来特别慢。

sass也有一个@import规则，但不同的是，sass的@import规则在生成css文件时就把相关文件导入进来。这意味着所有相关的样式被归纳到了同一个css文件中，而无需发起额外的下载请求。

使用sass的@import规则并不需要指明被导入文件的全名。你可以省略.sass或.scss文件后缀。

### 使用SASS部分文件

当通过@import把sass样式分散到多个文件时，你通常只想生成少数几个css文件。那些专门为@import命令而编写的sass文件，并不需要生成对应的独立css文件，这样的sass文件称为局部文件，sass局部文件的文件名以下划线开头。这样，sass就不会在编译时单独编译这个文件输出css，而只把这个文件用作导入。当你@import一个局部文件时，还可以不写文件的全名，即省略文件名开头的下划线。

局部文件可以被多个不同的文件引用。

### 默认变量值

一般情况下，你反复声明一个变量，只有最后一处声明有效且它会覆盖前边的值。sass的!default标签，像css属性中!important标签的对立面，不同的是!default用于变量，含义是：如果这个变量被声明赋值了，那就用它声明的值，否则就用这个默认值。
```

$fancybox-width: 400px !default;
.fancybox {
width: $fancybox-width;
}```
在上例中，如果用户在导入你的 sass 局部文件之前声明了一个$fancybox-width 变量，那么你的局部文件中对$fancybox-width 赋值 400px 的操作就无效。如果用户没有做这样的声明，则$fancybox-width 将默认为 400px。

###嵌套导入

跟原生的 css 不同，sass 允许@import 命令写在 css 规则内。这种导入方式下，生成对应的 css 文件时，局部文件会被直接插入到 css 规则内导入它的地方。举例说明，有一个名为\_blue-theme.scss 的局部文件，内容如下：

````
aside {
  background: blue;
  color: white;
}```
然后把它导入到一个CSS规则内，如下所示：

`.blue-theme {@import "blue-theme"}`
````

.blue-theme {
aside {
background: blue;
color: #fff;
}
}```
被导入的局部文件中定义的所有变量和混合器，也会在这个规则范围内生效。这些变量和混合器不会全局有效，这样我们就可以通过嵌套导入只对站点中某一特定区域运用某种颜色主题或其他通过变量配置的样式。

### 原生的 CSS 导入

由于 sass 兼容原生的 css，所以它也支持原生的 CSS@import。尽管通常在 sass 中使用@import 时，sass 会尝试找到对应的 sass 文件并导入进来，但在下列三种情况下会生成原生的 CSS@import，尽管这会造成浏览器解析 css 时的额外下载：

- 被导入文件的名字以.css 结尾；
- 被导入文件的名字是一个 URL 地址；
- 被导入文件的名字是 CSS 的 url()值。

这就是说，你不能用 sass 的@import 直接导入一个原始的 css 文件，因为 sass 会认为你想用 css 原生的@import。但是，因为 sass 的语法完全兼容 css，所以你可以把原始的 css 文件改名为.scss 后缀，即可直接导入了。

### 静默注释;

sass 另外提供了一种不同于 css 标准注释格式/_ ... _/的注释语法，即静默注释，其内容不会出现在生成的 css 文件中。静默注释的语法跟 JavaScriptJava 等类 C 的语言中单行注释的语法相同，它们以//开头，注释内容直到行末。

```
body {
  color: #333; // 这种注释内容不会出现在生成的css文件中
  padding: 0; /* 这种注释内容会出现在生成的css文件中 */
}
```

实际上，css 的标准注释格式/_ ... _/内的注释内容亦可在生成的 css 文件中抹去。当注释出现在原生 css 不允许的地方，如在 css 属性或选择器中，sass 将不知如何将其生成到对应 css 文件中的相应位置，于是这些注释被抹掉。

## 混合器

通过 sass 的混合器实现大段样式的重用。混合器使用@mixin 标识符定义。

```
@mixin rounded-corners {
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
}
```

然后就可以在你的样式表中通过@include 来使用这个混合器，放在你希望的任何地方。@include 调用会把混合器中的所有样式提取出来放在@include 被调用的地方：

````
notice {
  background-color: green;
  border: 2px solid #00aa00;
  @include rounded-corners;
}

//sass最终生成：

.notice {
  background-color: green;
  border: 2px solid #00aa00;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
}```

###何时使用混合器

判断一组属性是否应该组合成一个混合器，一条经验法则就是你能否为这个混合器想出一个好的名字。如果你能找到一个很好的短名字来描述这些属性修饰的样式，比如rounded-cornersfancy-font或者no-bullets，那么往往能够构造一个合适的混合器。


###混合器中的CSS规则

混合器中不仅可以包含属性，也可以包含css规则，包含选择器和选择器中的属性，如下代码:
@mixin no-bullets {
  list-style: none;
  li {
    list-style-image: none;
    list-style-type: none;
    margin-left: 0px;
  }
}
当一个包含css规则的混合器通过@include包含在一个父规则中时，在混合器中的规则最终会生成父规则中的嵌套规则。
````

ul.plain {
color: #444;
@include no-bullets;
}

```
sass的@include指令会将引入混合器的那行代码替换成混合器里边的内容。
```

ul.plain {
color: #444;
list-style: none;
}
ul.plain li {
list-style-image: none;
list-style-type: none;
margin-left: 0px;
}

```
### 给混合器传参

混合器并不一定总得生成相同的样式。可以通过在@include混合器时给混合器传参，来定制混合器生成的精确样式。当@include混合器时，参数其实就是可以赋值给css属性值的变量：
```

@mixin link-colors($normal, $hover, $visited) {
color: $normal;
&:hover { color: $hover; }
&:visited { color: $visited; }
}```
当混合器被@include 时，你可以把它当作一个 css 函数来传参：

```
a {
  @include link-colors(blue, red, green);
}

//Sass最终生成的是：

a { color: blue; }
a:hover { color: red; }
a:visited { color: green; }
```

当你@include 混合器时，有时候可能会很难区分每个参数是什么意思，参数之间是一个什么样的顺序。为了解决这个问题，sass 允许通过语法$name: value 的形式指定每个参数的值。这种形式的传参，参数顺序就不必再在乎了，只需要保证没有漏掉参数即可：

```
a {
    @include link-colors(
      $normal: blue,
      $visited: green,
      $hover: red
  );
}
```

###默认参数值

为了在@include 混合器时不必传入所有的参数，我们可以给参数指定一个默认值。参数默认值使用$name: default-value 的声明形式，默认值可以是任何有效的 css 属性值，甚至是其他参数的引用，如下代码：

```
@mixin link-colors(
    $normal,
    $hover: $normal,
    $visited: $normal
  )
{
  color: $normal;
  &:hover { color: $hover; }
  &:visited { color: $visited; }
}
```

###使用选择器继承来精简 CSS

使用 sass 的时候，最后一个减少重复的主要特性就是选择器继承。基于 Nicole Sullivan 面向对象的 css 的理念，选择器继承是说一个选择器可以继承为另一个选择器定义的所有样式。这个通过@extend 语法实现，如下代码:

```
//通过选择器继承继承样式
.error {
  border: 1px red;
  background-color: #fdd;
}
.seriousError {
  @extend .error;
  border-width: 3px;
}
```

```
.error, .seriousError {
  border: 1px red;
  background-color: #fdd; }

.seriousError {
  border-width: 3px; }
```

##继承

关于@extend 有两个要点你应该知道。

- 跟混合器相比，继承生成的 css 代码相对更少。因为继承仅仅是重复选择器，而不会重复属性，所以使用继承往往比混合器生成的 css 体积更小。如果你非常关心你站点的速度，请牢记这一点。
- 继承遵从 css 层叠的规则。当两个不同的 css 规则应用到同一个 html 元素上时，并且这两个不同的 css 规则对同一属性的修饰存在不同的值，css 层叠规则会决定应用哪个样式。相当直观：通常权重更高的选择器胜出，如果权重相同，定义在后边的规则胜出。

不要在 css 规则中使用后代选择器（比如.foo .bar）去继承 css 规则。如果你这么做，同时被继承的 css 规则有通过后代选择器修饰的样式，生成 css 中的选择器的数量很快就会失控：

```
.foo .bar { @extend .baz; }
.bip .baz { a: b; }
```

##小结

变量是 sass 提供的最基本的工具。通过变量可以让独立的 css 值变得可重用，无论是在一条单独的规则范围内还是在整个样式表中。变量、混合器的命名甚至 sass 的文件名，可以互换通用\_和-。同样基础的是 sass 的嵌套机制。嵌套允许 css 规则内嵌套 css 规则，减少重复编写常用的选择器，同时让样式表的结构一眼望去更加清晰。sass 同时提供了特殊的父选择器标识符&，通过它可以构造出更高效的嵌套。

你也已经学到了 sass 的另一个重要特性，样式导入。通过样式导入可以把分散在多个 sass 文件中的内容合并生成到一个 css 文件，避免了项目中有大量的 css 文件通过原生的 css @import 带来的性能问题。通过嵌套导入和默认变量值，导入可以构建更强有力的、可定制的样式。混合器允许用户编写语义化样式的同时避免视觉层面上样式的重复。你不仅学到了如何使用混合器减少重复，同时学习到了如何使用混合器让你的 css 变得更加可维护和语义化。最后，我们学习了与混合器相辅相成的选择器继承。继承允许你声明类之间语义化的关系，通过这些关系可以保持你的 css 的整洁和可维护性。

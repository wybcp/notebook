# compile

## 命令行编译

单文件转换命令:

`sass input.scss output.css`

单文件监听命令:

`sass --watch input.scss:output.css`

sass 监听整个目录：

`sass --watch app/sass:public/stylesheets`

## 命令行编译配置选项

命令行编译 sass 有配置选项，如编译过后 css 排版、生成调试 map、开启 debug 信息等，可通过使用命令 sass -v 查看详细。我们一般常用两种--style--sourcemap。

```
//编译格式
sass --watch input.scss:output.css --style compact

//编译添加调试map
sass --watch input.scss:output.css --sourcemap

//选择编译格式并添加调试map
sass --watch input.scss:output.css --style expanded --sourcemap

//开启debug信息
sass --watch input.scss:output.css --debug-info
```

### 四种编译排版演示

--style 表示解析后的 css 是什么排版格式;

sass 内置有四种编译格式:nested/expanded/compact/compressed。

--sourcemap 表示开启 sourcemap 调试。开启 sourcemap 调试后，会生成一个后缀名为.css.map 文件。

```CSS
//未编译样式
.box {
  width: 300px;
  height: 400px;
  &-title {
    height: 30px;
    line-height: 30px;
  }
}
```

### nested 编译排版格式

````CSS
/*命令行内容*/
sass style.scss:style.css --style nested

/*编译过后样式*/
.box {
  width: 300px;
  height: 400px; }
  .box-title {
    height: 30px;
    line-height: 30px; }```
###expanded 编译排版格式
````

/_命令行内容_/ sass style.scss:style.css --style expanded

/_编译过后样式_/ .box { width: 300px; height: 400px; } .box-title { height: 30px; line-height: 30px; }```

### compact 编译排版格式

```CSS
/*命令行内容*/
sass style.scss:style.css --style compact

/*编译过后样式*/
.box { width: 300px; height: 400px; }
.box-title { height: 30px; line-height: 30px; }
```

### compressed 编译排版格式

```CSS
/*命令行内容*/
sass style.scss:style.css --style compressed

/*编译过后样式*/
.box{width:300px;height:400px}.box-title{height:30px;line-height:30px}
```

# 页面静态化

1. 动态文件执行过程:语法分析-编译-运行
2. 静态文件，不需要编译，减少了服务器脚本运行的时间，降低了服务器的响应时间，直接运行，响应速度快；如果页面中一些内容不经常改动，动态页面静态化是非常有效的加速方法。（纯静态，伪静态还是需要 PHP 解释器的）
3. 生成静态 URL 利于 SEO，利于蜘蛛抓取和收录，有利于提升排名

## 开启 buffer

在 php.ini 中的 output_buffering 开启

```conf
; Default Value: Off
; Development Value: 4096
; Production Value: 4096
; 值为8的倍数
; http://php.net/output-buffering
output_buffering = 4096
implicit_flush=false
```

在 php 文件中使用 `ob_start()`函数开启

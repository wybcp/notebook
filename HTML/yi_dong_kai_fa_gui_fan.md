# 移动开发规范

http://alloyteam.github.io/Spirit/modules/Standard/

以下规范建议，均是 Alloyteam 在日常开发过程中总结提炼出的经验，规范具备较好的项目实践，强烈推荐使用 ##字体设置

使用无衬线字体
`body {font-family:"Helvetica Neue", Helvetica, STHeiTi, sans-serif;}`

iOS 4.0+ 使用英文字体 Helvetica Neue，之前的 iOS 版本降级使用 Helvetica。中文字体设置为华文黑体 STHeiTi。 需补充说明，华文黑体并不存在 iOS 的字体库中(http://support.apple.com/kb/HT5878)， 但系统会自动将华文黑体 STHeiTi 兼容命中系统默认中文字体黑体-简或黑体-繁

```
Heiti SC Light黑体-简细体 （iOS 7后废弃）

Heiti SC Medium黑体-简中黑Heiti TC Light黑体-繁细体Heiti TC Medium黑体-繁中黑
```

原生 Android 下中文字体与英文字体都选择默认的无衬线字体
4.0 之前版本英文字体原生 Android 使用的是 DroidSans，中文字体原生 Android 会命中 DroidSansFallback4.0 之后中英文字体都会使用原生 Android 新的 Roboto 字体其他第三方 Android 系统也一致选择默认的无衬线字体 ##基础交互

设置全局的 CSS 样式，避免图中的长按弹出菜单与选中文本的行为

```
a, img {
-webkit-touch-callout: none;/* 禁止长按链接与图片弹出菜单 */
}
html, body {
-webkit-user-select: none;/* 禁止选中文本（如无文本选中需求，此为必选项） */user-select: none;
}
```

##移动性能

要考虑 Android 低端机与 2G 网络场景下性能 注意！

发布前必要检查项

- 所有图片必须有进行过压缩
- 考虑适度的有损压缩，如转化为 80%质量的 jpg 图片
- 考虑把大图切成多张小图，常见在 banner 图过大的场景

加载性能优化, 达到打开足够快

- 数据离线化，考虑将数据缓存在 localStorage
- 初始请求资源数 < 4 注意！
- 图片使用 CSS Sprites 或 DataURI
- 外链 CSS 中避免 @import 引入
- 考虑内嵌小型的静态资源内容
- 初始请求资源 gzip 后总体积 < 50kb
- 静态资源(HTML/CSS/JS/Image)是否优化压缩？
- 避免打包大型类库
- 确保接入层已开启 Gzip 压缩（考虑提升 Gzip 级别，使用 CPU 开销换取加载时间） 注意！
- 尽量使用 CSS3 代替图片
- 初始首屏之外的静态资源（JS/CSS）延迟加载 注意！
- 初始首屏之外的图片资源按需加载（判断可视区域） 注意！
- 单页面应用(SPA)考虑延迟加载非首屏业务模块
- 开启 Keep-Alive 链路复用

运行性能优化, 达到操作足够流畅

- 避免 iOS 300+ms 点击延时问题 注意！
- 缓存 DOM 选择与计算
- 避免触发页面重绘的操作
- Debounce 连续触发的事件(scroll / resize / touchmove 等)，避免高频繁触发执行 注意！
- 尽可能使用事件代理，避免批量绑定事件
- 使用 CSS3 动画代替 JS 动画
- 避免在低端机上使用大量 CSS3 渐变阴影效果，可考虑降级效果来提升流畅度
- HTML 结构层级保持足够简单
- 尽能少的使用 CSS 高级选择器与通配选择器
- Keep it simple

在线性能检测评定工具使用指南

- 访问 Google PageSpeed 在线评定网站
- 在地址栏输入目标 URL 地址，点击分析按钮开始检测
- 按 PageSpeed 分析出的建议进行优化，优先解决红色类别的问题


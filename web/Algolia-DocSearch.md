# Algolia DocSearch

Algolia DocSearch,专门针对在线文档搜索。

## Algolia DocSearch 的基本原理和主要优势

相对于其它一些全文搜索方案，Algolia DocSearch 的主要优势在于它是专门针对在线文档搜索这一需求的。不需要繁琐的配置，也不需要自己有数据库等软硬件支持，而只需在自己网站中插入少量代码就可以实现强大的文档搜索功能了。

根据官方的说明，在你通过申请后，其服务器会定期抓取（免费用户抓取周期是 24 小时）你的网站内容并分析，对文档的各级标题、段落等内容建立索引，这样，在网站中加入搜索框之后，用户输入关键时是便可以请求 DocSearch 的接口并显示搜索结果了。这些请求、结果显示相关的逻辑都封装好了，你要做的只是要按要求插入代码、样式以及那个搜索框。

![img](https://ask.qcloudimg.com/http-save/yehe-2544533/1z1xkdinqn.jpeg?imageView2/2/w/1620)

实现步骤

\1. 在 Algolia DocSearch 官网 填写自己的文档网站的地址和邮箱进行申请

DocSearch 可以免费使用，而且不用注册，因为他们觉得，任何人都应该能够有能力构建方便搜索的文档（可以说相当有情怀吧）。当然，也有收费的服务可供选用，差异在于技术支持和请求频率限制等方面不同。

\2. 收到确认邮件并确认

提交申请之后不久，你所填写的邮箱就会收到一封询问邮件。里面说明你的网站技术上是否支持写用 DocSearch。如果支持，还会询问你是否能修改源码向其中注入需要的代码。你需要回复邮件进行确认。

\3. DocSearch 对你的文档网站首次爬取页面数据，并向你发送需要注入的代码及相关操作指导。

第 2 和 第 3 步都需要对方人工处理，而且根据你的网站复杂程序，需要等待的时间会有差异，不过就我个人经验而言还是很快的。前后不到两个小时。

邮件内容大致如下：

![img](https://ask.qcloudimg.com/http-save/yehe-2544533/2aspjs2lc6.jpeg?imageView2/2/w/1620)

\4. 根据第 3 步里收到的邮件提示，修改网站代码

可以看到，邮件主要包括 apiKey 等配置信息，而且对于如何使用也描述得非常清楚了。系统甚至分析出我网站 url 中使用了 v1_6 和 v2_0 区分不同版本的文档，并为此提供相关的参数 `algoliaOptions: {'facetFilters': ["version:$VERSION"]},` 以及详细使用例子说明，简直无微不至，催人尿下……

因为自己网站用 vue 单文件组件写的，所以我选择使用 npm 包，而并没有完全照着邮件里来，但这实质是一样的。

首先，安装 docsearch.js 包

```
1yarn add -D docsearch.js
```

然后，修改文档页面组件，加入搜索输入框和 docsearch 初始化代码

```
 1<template>
 2  <input
 3    v-show="$route.path.indexOf('/doc') === 0"
 4    type="text"
 5    class="search-input"
 6    id="search_input"
 7    placeholder="搜索文档"
 8  >
 9</template>
10
11<script>
12import 'docsearch.js/dist/cdn/docsearch.min.css'
13import docsearch from 'docsearch.js'
14export default {
15  mounted () {
16    docsearch({
17      apiKey: 'feb33c2506cdece7f0267859a856767a',
18      indexName: 'wevue',
19      inputSelector: '#search_input',
20      algoliaOptions: { 'facetFilters': ['version:v2_0'] },
21      debug: false // Set debug to true if you want to inspect the dropdown
22    })
23  }
24}
25</script>
```

> 注意：上面只是最简单的示例。实际上使用可以更灵活，例如装搜索框封装成一个组件，若有兴趣，可前往 we-vue查看实际使用情况。

最后根据自己的喜好及需要，调整下搜索框及搜索下拉弹出层的样式，就完工了。下面是最终效果。

![img](https://ask.qcloudimg.com/http-save/yehe-2544533/god43hdobh.jpeg?imageView2/2/w/1620)

## 总结

Algolia DocSearch 可以说真如其官网描述的那样，算是目前构建可在线搜索文档的最简单的方式之一了。你只需要关注文档本身，进行少量的配置，其它的 Algolia 全包了。另外，Algolia 还有一些其它优秀产品及服务，诸位可前往官网自行探索。

本文以自己的项目为例，但 Aloglia DocSearch 适合很多类型的网站，使用 Vue.js 官网这类用 HEXO 构建的静态站，又或者像 Easywechat 一样用 Laravel 开发的动态网站（事实上自己早前曾向超哥安利过 DocSearch, 然后竟然真被用上了 ? ）。有了搜索功能之后，用户能更方便有找到自己想要的信息，当然，网站的格调也极大的提升了！


https://cloud.tencent.com/developer/article/1156992
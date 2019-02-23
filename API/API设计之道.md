# 设计

## API 易用标准

Don’t make me think.

- 达标：词法和语法
  - 正确拼写
  - 准确用词
  - 注意单复数
  - 不要搞错词性
  - 处理缩写
  - 用对时态和语态
- 进阶：语义和可用性
  - 单一职责
  - 避免副作用
  - 合理设计函数参数
  - 合理运用函数重载
  - 使返回值可预期
  - 固化术语表
  - 遵循一致的 API 风格
- 卓越：系统性和大局观
  - 版本控制
  - 确保向下兼容
  - 设计扩展机制
  - 控制 API 的抽象级别
  - 收敛 API 集
  - 发散 API 集
  - 制定 API 的支持策略

## 达标：词法和语法

### 正确拼写

### 准确用词

- message：一般指双方通信的消息，是内容载体。而且经常有来有往、成对出现。比如 postMessage() 和 receiveMessage()。
- notification：经常用于那种比较短小的通知，现在甚至专指 iOS / Android 那样的通知消息。比如 new NotificationManager()。
- news：内容较长的新闻消息，比 notification 更重量级。比如 getTopNews()。
- feed：自从 RSS 订阅时代出现的一个单词，现在 RSS 已经日薄西山，但是 feed 这个词被用在了更多的地方。其含义只可意会不可言传。比如 fetchWeitaoFeeds()。

成对出现的正反义词不可混用，常见正反义词：

- in & out
- on & off
- previous & next
- forward & backward
- success & failure
- show & hide
- open & close

### 注意单复数

- 数组（Array）、集合（Collection）、列表（List）这样的数据结构，在命名时都要使用复数形式。
- 在复数的风格上保持一致，要么所有都是 -s，要么所有都是 -list。
- 字典（Dictionary）、表（Map）的时候，不要使用复数！

### 不要搞错词性

方法命名用动词、属性命名用名词、布尔值类型用形容词（或等价的表语）。

- n. 名词：success, failure
- v. 动词：succeed, fail
- adj. 形容词：successful, failed（无形容词，以过去分词充当）
- adv. 副词：successfully, fail to do sth.（无副词，以不定式充当）

### 处理缩写

首字母缩写词的所有字母均大写。

对长单词简写（shortened word），如 btn (button)、chk (checkbox)、tpl (template)。这要视具体的语言规范 / 开发框架规范而定。

### 用对时态和语态

由于我们在调用 API 时一般类似于「调用一条指令」，所以在语法上，一个函数命名是祈使句式，时态使用一般现在时。

但在某些情况下，我们需要使用其他时态（进行时、过去时、将来时）。比如，当我们涉及到生命周期、事件节点。

在一些组件系统中，必然涉及到生命周期，我们来看一下 React 的 API 是怎么设计的：

- 引入 before、after 这样的介词来简化时态：

```js
// will render
Component.on("beforeRender", function() {});
// now rendering
Component.on("rendering", function() {});
// has rendered
Component.on("afterRender", function() {});
```

- 另一方面是关于语态，即选用主动语态和被动语态的问题。其实最好的原则就是尽量避免使用被动语态。因为被动语态看起来会比较绕，不够直观，因此我们要将被动语态的 API 转换为主动语态。

  ```js
  // passive voice, make me confused
  object.beDoneSomethingBy(subject);

  // active voice, much more clear now
  subject.doSomething(object);
  ```

## 进阶：语义和可用性

确保 API 的可用性和语义才使 API 真正「可用」。

### 单一职责

单一职责是软件工程中一条著名的原则。

小到函数级别的 API，大到整个包，保持单一核心的职责都是很重要的一件事。

### 避免副作用

避免副作用:

1. 函数本身的运行稳定可预期。

1. 函数的运行不对外部环境造成意料外的污染。

对于无副作用的纯函数而言，输入同样的参数，执行后总能得到同样的结果，这种幂等性使得一个函数无论在什么上下文中运行、运行多少次，最后的结果总是可预期的 。

### 合理设计函数参数

函数名、参数设置、返回值类型，这三要素构成了完整的函数签名。参数设置对用户来说是接触最频繁，也最为关心的部分。

- 优化参数顺序。**相关性越高的参数越要前置**，**可省略的参数后置**，以及**为可省略的参数设定缺省值**。

  ```js
  // bad
  function renderPage(pageIndex, pageData) {}

  renderPage(0, {});
  renderPage(1, {});

  // good
  function renderPage(pageData, pageIndex = 0) {}

  renderPage({});
  renderPage({}, 1);
  ```

- 控制参数个数。参数能省略则省略，或更进一步，**合并同类型的参数**。

### 固化术语表

**产出术语表**包括对缩写词的大小写如何处理、是否有自定义的缩写词等等。一个术语表可以形如：

| 标准术语 | 含义     | 禁用的非标准词              |
| -------- | -------- | --------------------------- |
| pic      | 图片     | image, picture              |
| path     | 路径     | URL, url, uri               |
| on       | 绑定事件 | bind, addEventListener      |
| off      | 解绑事件 | unbind, removeEventListener |
| emit     | 触发事件 | fire, trigger               |
| module   | 模块     | mod                         |

对于一些创造出来的、业务特色的词汇，如果不能用英语简明地翻译，就直接用拼音。

### 遵循一致的 API 风格

## 参考：

- 阮一峰[《理解 RESTful 架构》](http://www.ruanyifeng.com/blog/2011/09/restful)
- 法海 [《从达标到卓越 —— API 设计之道》](http://taobaofed.org/blog/2017/02/16/a-guide-to-api-design/)

# json

从 MySQL 5.7 原生支持 json 格式。

## 使用

插入接送数据：

```sql
insert into user values(1,{'name':'xxx','age':20}),(2,{'name':'xx','age':21});
```

获取 key-value：

```sql
select id ,JSON_EXTRACT(context,'$.name') name,JSON_EXTRACT(context,'$.age') age from user;
```

获取所有的键：

```sql
select id,json_keys(context) from user;
```

增加 key-value：

```sql
update user set context=JSON_INSERT(context,'$.address','cd') where id =21;
```

更改 key-value：

```sql
update user set context=JSON_SET(context,'$.address','cq') where id =21;
```

删除 key-value：

```sql
update user set context=JSON_REMOVE(context,'$.address') where id =21;
```

## 从今天起，用好 JSON 数据类型！

[从今天起，用好 JSON 数据类型！ (qq.com)](https://mp.weixin.qq.com/s/SrQQ8Brufm5geVM9dmuQBA)

原创 破产码农 [InsideMySQL](javascript:void(0);) *今天*

收录于话题

\#数据库17

\#MySQL18

![图片](640)     

破产码农

IT圈最会讲故事的网红 · 南山彭于晏

# MySQL 5.7版本开始就已支持JSON类型，用以实现非结构数据的存储。 

很多同学认为JSON类型就是一个字符串类型，那是不对的。

MySQL的JSON本质上和MongoDB的BSON类型是一样的，都是原生的二进制JSON。

想要知道MySQL JSON类型的具体实现可以看官方的worklog：*WL#8132: JSON datatype and binary storage format*

虽然JSON类型已经推出有近6年的时间，然而大部分开发同学并不能充分利用JSON的优势。

今天，就由姜老师教大家如何用好JSON类型。

#  

1

JSON的使用



在几年前的文章[*文档数据库们已在厕所哭晕，MySQL 5.7原生支持JSON格式中*](http://mp.weixin.qq.com/s?__biz=MjM5MjIxNDA4NA==&mid=203995900&idx=1&sn=3589a9476fe57ea599f115e175753bea&chksm=2f75a7d718022ec1c49abe5a4cf6a310332b9729b974cac9bd3c722f3ff3cd4eb2e4dd7fe728&scene=21#wechat_redirect)，已经对JSON类型的使用和函数索引有过基本的介绍，这里不再赘述相关内容。

但我发现，很多开发同学在JSON类型中更新某个字段时，比如字段a更新为xx时，会写成类似下面这样的SQL：

- 
- 
- 

```
UPDATE t SET info = "{'a':'xx','b':'yy','c':'zz',...}"WHERE id = ?
```

这样的写法再次暴露出业务同学对于JSON类型的理解不到位，只是将其理解为一个很大的字符串。

即在更新时拼接出一个很大的字符串，然后用UPDATE去更新。这样在业务端的处理及其复杂。

对于更新JSON类型中的某个字段，只需按如下方式：

- 
- 
- 

```
UPDATE t SET info = JSON_SET(info,'a','xxx') WHERE id = ?
```

可以看到，通过函数JSON_SET可以方便的对某几个字段更新，充分利用JSON类型的优势。

除了JSON_SET，MySQL还提供了JSON_INSERT()、JSON_REPLACE()、JSON_ARRAY_APPEND等一些列JSON的更新函数。

**切记，不要再通过手工方式，通过字符串的方式更新JSON字段。**

#  

2

JSON的业务使用



在哪些场景中使用JSON类型，能更为充分的利用JSON的优势呢？

总的来说，以下几种场景非常适合：

1. 元数据存储
2. 用户画像

在做一些类似CMDB这样的系统时，一些数据并无法一开始就定义好固定的列，后续可能还会增加。

这时利用JSON类型的非结构化存储，可以非常方便的存储上述数据。

比如，存储服务器的元信息，其中每台服务器上有多块磁盘。

这个用关系型就不太好表达，但是用JSON类型就很好描述：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7yKicibPTeZhMgpJGCY5JlyY4WGP4Vhvyvl4AErP1XSWhLjatjIQRKBACA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

另外一个非常适合使用JSON类型的业务是用户画像，即给用户打标签。

之前很多业务同学会设计成类似如下的这种模式：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7ycqazHl4eGYMVyMEcOewiclGANyibib3WL6NPNNticcqibg65apUMlYYPiaibg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后呢，他们会要求DBA在标签列上创建全文索引，进行业务上的查询。

例如查询，80后，常看电影的用户有哪些。

这样的设计是非常错误的。

因为标签列有字符串分割的潜规则”；“，容易引入脏数据。

另外，标签的可维护性太差，更新还是插入都非常麻烦。

之前，若用关系型的方式，可以设计为类似如下的表结构形式：

 ![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7yEYwdB37uZN0D5OUJGOehofaGe7HJdAZ1KgiastQVorGCr5FTC85jGEA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

通过创建（userId，userTag）的联合主键，创建一张用户画像表。但这时你会发现，userId的冗余度非常高。

若用JSON类型的数组功能，则表结构就会非常优雅了：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7yQO5HN15Xqib2cTW9durmZRrSs55ZoeHDdqcNwOyIhFiaFrJDOQFUND2A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后利用MySQL 8.0提供的Multi-Valued Indexes，则可以方便的进行用户画像的查询。

如我们想查询都爱看电影的用户有哪些（userTags = 10）。

首先，创建Multi-Valued Indexs：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7yX986lwU8nj5a5sN9HJnuk4YVoXEavMbIwZQ925bYJ5U0wSebL9nwQQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后，利用函数MEMBER OF、JSON_CONTAINS、JSON_OVERLAP进行用户画像的搜索。如：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7yiciae7wS9WaKZWe5M9nw32lGXhzf7IeZzZhxOxE6C9q2gtephoVlibJYQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

上面这个SQL使用了函数MEMBER OF查询爱看电影的用户。

若想查询80后且爱看电影的用户，则可以使用函数JSON_CONTAINS：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7y0abMYYRrmbxhtBiciaJEE6FUYMCL19yFmI5HdWfVNRPZqxaukQCgWxJA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如果想要查询画像为 80 后、90 后，且常看电影的用户，则可以使用函数 JSON_OVERLAP：

![图片](https://mmbiz.qpic.cn/mmbiz_png/MEpoEwcicyJkLIH5pkhNeLrib1Y1G7Kq7ygsyjvibibYBsOLxcvZcqXH9gZDGqHfDjGiaPYY9xVq4TLpZRbTHkaxKZA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

可以看到使用JSON类型，一些都来的如此优雅。

#  

3

利器：JSON_TABLE



最后，介绍一下函数JSON_TABLE，他可以将非结构化的数据转化为结构化，打破关系型和非关系型的边界。

对于一些爬虫业务，后期想做一些分析就变得非常容易了。

这里不做具体展开，只是给一个简单的例子：

![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

上面这条SQL就是将表chatroomdetail中的JSON类型字段，转化为一张表进行查询。

MySQL的JSON_TABLE还支持JSON嵌套的转化，具体大家可以查看官方用户手册。

#  

4

总结与展望



今天姜老师给大家介绍了 MySQL JSON 类型的使用，以及具体业务中如何结合JSON非结构化的优势。

所写的内容都已更新在拉勾教育的专栏《姜承尧的MySQL实战宝典》，欢迎大家订阅。

在专栏中，我还描述了JSON类型的一种业务使用场景。

![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

最后我想说，这个世界依然是属于关系型的。

NoSQL已然完败，你还要坚持么？



直播预告



![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

*每周五、六，不定期直播，分享技术干货
*

![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)



IMG群是码农的交流社区，IMG微信群交流内容包括但不限于技术、经济、军事、八卦等话题。欢迎有态度的码农们加入IMG大家庭。

IMG目前有**少林群、武当群、峨眉群、华山群、M悦会（高端VIP群）**。

仅限码农入群，猎头或其他行业勿加，入群请加姜老师个人微信 ***82946772\***，并备注：**码农入IMG群**

\-----------------------

公众号：破产码农

视频号：破产码农

抖音号：**破产码农**

B站号：姜老师带你飞

长按下图二维码关注，将感受到一个有趣的灵魂，每篇文章都会有新惊喜。

![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

​      

往期推荐



[![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)MySQL崛起：缘起](http://mp.weixin.qq.com/s?__biz=MjM5MjIxNDA4NA==&mid=2649741286&idx=1&sn=db8b0dd8516e1a2a4f22e428f851f273&chksm=beb2cacd89c543db6ab3aae2ee39f27caaa1a7ebb2390e98244700178dd3a1a63f575da8472c&scene=21#wechat_redirect)



[![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)淘宝的数据库，主键是如何设计的？](http://mp.weixin.qq.com/s?__biz=MjM5MjIxNDA4NA==&mid=2649741272&idx=1&sn=e7fd56c468360525fc21332933125ed4&chksm=beb2caf389c543e5823c1aaa6b784164bba0d293f438ae4dbe308dc3af19f2ac8dc2e33da314&scene=21#wechat_redirect)



[![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)注意了！这个远古Bug，让你的 MySQL 8.0 性能下降2倍！](http://mp.weixin.qq.com/s?__biz=MjM5MjIxNDA4NA==&mid=2649741187&idx=1&sn=938216aa3bfca07e2ee1ac17e6bc9bb5&chksm=beb2caa889c543be489b08a1013402fcdced3e6dd9646b98077661c3ee8bedd1e781b4db8e9b&scene=21#wechat_redirect)



[![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)MySQL vs Redis，新时代王者的较量](http://mp.weixin.qq.com/s?__biz=MjM5MjIxNDA4NA==&mid=2649741090&idx=1&sn=d0a5c8ca139505f2605efbf9872c81f0&chksm=beb2ca0989c5431f9d066d96866a32114d87fdcb75d162ef500725e92cb127376d53c0eb2207&scene=21#wechat_redirect)



[![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)刚刚，MySQL 战胜了老大哥 Memcached！](http://mp.weixin.qq.com/s?__biz=MjM5MjIxNDA4NA==&mid=2649740991&idx=1&sn=49a1e18b4f509e291e7afc96e98c04be&chksm=beb2cb9489c54282c4cdf6a8fe324f8918388b5377415df084f0d10f009d7227a7d398176405&scene=21#wechat_redirect)



喜欢此内容的人还喜欢

[干货 | 全方位深度解读 Elasticsearch 分页查询干货 | 全方位深度解读 Elasticsearch 分页查询...铭毅天下Elasticsearch不喜欢不看的原因确定内容质量低 不看此公众号](javascript:void(0);)[Flink 最佳实践之使用 Canal 同步 MySQL 数据至 TiDBFlink 最佳实践之使用 Canal 同步 MySQL 数据至 TiDB...Flink 中文社区不喜欢不看的原因确定内容质量低 不看此公众号](javascript:void(0);)[ClickHouse 在日志存储与分析方面作为 ElasticSearch 和 MySQL 的替代方案ClickHouse 在日志存储与分析方面作为 ElasticSearch 和 MySQL 的替代方案...架构师不喜欢不看的原因确定内容质量低 不看此公众号
  ](javascript:void(0);)

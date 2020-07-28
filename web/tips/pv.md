# [不用 JavaScript，纯静态网站如何统计 PV？](https://mp.weixin.qq.com/s?__biz=MzIzNzA4NDk3Nw==&mid=2457739798&idx=2&sn=05c7bd22299c67659d89ce841db4b634&chksm=ff448a48c833035e007edea7e4b8a371c3c2b0f8be73ac44c3c2258dff385db69e840e11e70a&scene=126&sessionid=1593681506&key=eaa65f45ed778521e2ee175dd6a8c120719b160042388fcb7f2b72df547093a390fdc23410afdb12ef4a2588bb6707cba06e421416f01b15fe3cd1427b5d2c98bdefdf84e393e6bb378bc3a2d5de58b2&ascene=1&uin=MTY1NTc1OTU%3D&devicetype=Windows+10+x64&version=6209007b&lang=zh_CN&exportkey=AT3ltBkeqO4ThAfbTcERIQQ%3D&pass_ticket=8QzwtStGI7bQs%2BZt0qnbg%2Feww92j8yokgPZfIhjZj94%3D)

大家对访问统计pv/uv肯定不陌生，一般我们访问一些网站，会在网站的最下方看到某某页面已经被访问了多少次。如下图所示。

![img](https://mmbiz.qpic.cn/mmbiz_png/ohoo1dCmvqfjIC7ib4ItDkQnmeVicQ6x1AkrylicBcxXwOcGDUV2gMx9CIic997cnuFUyqIuXuUU3p5EHbQDLzDkaA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如果这个网站的前后端都是我自己开发的，那么实现这样一个访问统计功能，只需要短短的几行代码。

但如果我的网站是一个纯静态网站呢？例如我的博客使用的是Hexo，它没有后端，又该如何实现这个访问统计的功能呢？

可能有同学想到，使用 JavaScript 来实现。那么如果你只会 Python，不会 JavaScript 呢？

实际上，我们可以使用一种特殊的图片来实现这个功能。这就是 SVG 图片。SVG 图片本质上就是一段 XML 代码。大家复制下面这段 XML 代码：

```xml
<?xml version="1.0" encoding="utf-8" ?><svg baseProfile="full" height="200" version="1.1" width="200" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink"><defs /><g font-size="14"><text x="10" y="20">当前访问量：11</text></g></svg>
```

把它保存成`pv.svg`。然后，双击使用现代化的浏览器（Chrome/Firefox）打开它，你将会看到：

![img](https://mmbiz.qpic.cn/mmbiz_png/ohoo1dCmvqfjIC7ib4ItDkQnmeVicQ6x1AAJLjsNtoNWgnq51I6PRzeHsMstQcMSMic0kn6E2U3poOUysrfftoq1g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这上面的文字是可以选中、复制的。看起来跟`图片`完全没有什么关系。但是，如果我们在 HTML 的`img`标签中引用这个文件：

```html
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>测试访问量统计SVG</title></head><body>    <h2>访问量统计演示页面</h2>    <div>        <p>这是一个完全静态没有后端的 HTML 页面</p>        <img src="pv.svg">    </div>
</body></html>
```

可以看到，`pv.svg`就像图片一样被显示出来了：

![img](https://mmbiz.qpic.cn/mmbiz_png/ohoo1dCmvqfjIC7ib4ItDkQnmeVicQ6x1AznY8VpcsibCGuaOL8SLh1YyZKNAj35zMo8iax9PRFM7L5oS1oIVjOibtw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

所以，如果我们使用 FastApi/Flask/Django 这种后端框架，写一个实时统计访问量的接口，当用户访问这个接口的时候，返回一张 SVG 图片，这不就在完全不使用 JavaScript 的情况下实现了访问统计功能吗？

说干就干，我们使用 FastApi 来实现这个接口。Python 有一个库叫做`svgwrite`可以快速把一段文字生成 SVG 图片。

后端代码如下：

```python
import redisimport svgwritefrom fastapi
import FastAPIfrom starlette.responses
import FileResponse

app = FastAPI()client = redis.Redis()

def write_text(file_name, pv):
    dwg = svgwrite.Drawing(file_name, (200, 200))
    paragraph = dwg.add(dwg.g(font_size=14))
    paragraph.add(dwg.text(f"当前访问量：{pv}", (10, 20)))
    dwg.save()

@app.get('/')
def index():
    return {'success': True}

@app.get('/pv/{user_id}')
def calc_pv(user_id):
    pv = client.hincrby('pv_count', user_id, 1)
    file_name = f'{user_id}.svg'
    write_text(file_name, pv)
    return FileResponse(file_name)
```

关键的接口就是`/pv/{user_id}`，当浏览器访问了这个接口，就会返回一个 SVG 图片。对于相同的`user_id`，每次访问都会让访问量增加。不同`user_id`之间的访问量互不影响。由于`img`标签中的图片地址是不受跨域机制影响的，所以，通过这一个接口，我们可以给很多个不同的网站统计访问量。

接口写好以后，我们把它部署到服务器上，并把接口的完整地址改到原来的 HTML 文件中：

![img](https://mmbiz.qpic.cn/mmbiz_png/ohoo1dCmvqfjIC7ib4ItDkQnmeVicQ6x1ABibLYrkNNgpe1zzia85WgKh8a1hrCDZhJDUwhPj2icIjyO5Wh5H0pVzwQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

现在，当我们直接打开这个静态的 HTML，可以看到，每次刷新，访问量都会改变：

![img](https://mmbiz.qpic.cn/mmbiz_png/ohoo1dCmvqfjIC7ib4ItDkQnmeVicQ6x1AxtACF0KNA5EGJIa74gvbDrANiajJIUic2vJLnictksy949tA04aLwEwhw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

当然，这里统计的仅仅是页面访问量，你也可以在接口里面通过统计 IP 的方式来统计用户访问量，

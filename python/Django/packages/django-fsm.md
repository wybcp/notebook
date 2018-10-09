# 处理有限状态机：django-fsm

[django-fsm](https://github.com/viewflow/django-fsm) 给 Django 的模型添加了有限状态机的支持。如果你管理一个新闻网站，想用类似于“写作中”、“编辑中”、“已发布”来流转文章的状态，django-fsm 能帮你定义这些状态，还能管理状态变化的规则与限制。

Django-fsm 为模型提供了 FSMField 字段，用来定义模型实例的状态。用 django-fsm 的 `@transition` 修饰符，可以定义状态变化的方法，并处理状态变化的任何副作用。

虽然 django-fsm 文档很轻量，不过 [Django 中的工作流（状态）](https://gist.github.com/Nagyman/9502133) 这篇 GitHub Gist 对有限状态机和 django-fsm 做了非常好的介绍。
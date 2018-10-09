# django-extensions

[django-extensions](https://django-extensions.readthedocs.io/en/latest/) 这个 Django 包非常受欢迎，全是有用的工具，比如下面这些管理命令：

- `shell_plus` 打开 Django 的管理 shell，这个 shell 已经自动导入了所有的数据库模型。在测试复杂的数据关系时，就不需要再从几个不同的应用里做导入操作了。
- `clean_pyc` 删除项目目录下所有位置的 .pyc 文件
- `create_template_tags` 在指定的应用下，创建模板标签的目录结构。
- `describe_form` 输出模型的表单定义，可以粘贴到 `forms.py` 文件中。（需要注意的是，这种方法创建的是普通 Django 表单，而不是模型表单。）
- `notes` 输出你项目里所有带 TODO、FIXME 等标记的注释。

Django-extensions 还包括几个有用的抽象基类，在定义模型时，它们能满足常见的模式。当你需要以下模型时，可以继承这些基类：

- `TimeStampedModel`：这个模型的基类包含了 `created` 字段和 `modified` 字段，还有一个 `save()` 方法，在适当的场景下，该方法自动更新 `created` 和 `modified` 字段的值。
- `ActivatorModel`：如果你的模型需要像 `status`、`activate_date` 和 `deactivate_date` 这样的字段，可以使用这个基类。它还自带了一个启用 `.active()` 和 `.inactive()` 查询集的 manager。
- `TitleDescriptionModel` 和 `TitleSlugDescriptionModel`：这两个模型包括了 `title` 和 `description` 字段，其中 `description` 字段还包括 `slug`，它根据 `title`字段自动产生。

django-extensions 还有其他更多的功能，也许对你的项目有帮助，所以，去浏览一下它的[文档](https://django-extensions.readthedocs.io/)吧！

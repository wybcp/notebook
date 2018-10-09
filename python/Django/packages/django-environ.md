# django-environ

在 Django 项目的配置方面，[django-environ](https://django-environ.readthedocs.io/en/latest/) 提供了符合 [12 因子应用](https://www.12factor.net/) 方法论的管理方法。它是另外一些库的集合，包括 [envparse](https://github.com/rconradharris/envparse) 和 [honcho](https://github.com/nickstenning/honcho) 等。安装了 django-environ 之后，在项目的根目录创建一个 `.env` 文件，用这个文件去定义那些随环境不同而不同的变量，或者需要保密的变量。（比如 API 密钥，是否启用调试，数据库的 URL 等）

然后，在项目的 `settings.py` 中引入 `environ`，并参考[官方文档的例子](https://django-environ.readthedocs.io/)设置好 `environ.PATH()` 和 `environ.Env()`。就可以通过 `env('VARIABLE_NAME')` 来获取 `.env` 文件中定义的变量值了。

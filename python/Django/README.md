# [Django](https://www.djangoproject.com/)

新建项目

```bash
django-admin startproject mysite
```

迁移默认数据表

```bash
python manage.py migrate
```

改变模型

- 编辑 models.py 文件，改变模型。
- 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
- 运行 python manage.py migrate 来应用数据库迁移。

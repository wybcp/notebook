# 常见命令

## database

- `python manage.py check`：检查项目中的问题。
- `python manage.py migrate`：选中所有还没有执行过的迁移，在数据库中创建数据表，Django 通过在数据库中创建一个特殊的表 django_migrations 来跟踪执行过哪些迁移。
- `python manage.py makemigrations polls`： 为模型的改变生成迁移文件。
- `python manage.py sqlmigrate polls 0001`：sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL

## django api

通过以下命令打开 Python 命令行：

```sh
python manage.py shell
```

因为 manage.py 会设置 DJANGO_SETTINGS_MODULE 环境变量，这个变量会让 Django 根据 mysite/settings.py 文件来设置 Python 包的导入路径。

## admin

- `python manage.py createsuperuser`：创建管理员
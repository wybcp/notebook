# 本地化

<https://blog.csdn.net/aaazz47/article/details/78666099>

```django
MIDDLEWARE = [
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.locale.LocaleMiddleware',
   'django.middleware.common.CommonMiddleware',
]
```

<https://docs.djangoproject.com/zh-hans/2.0/topics/i18n/translation/>

```django
# “python/site-packages/django/conf/locale/”中的语言名称
LANGUAGE_CODE = 'zh-Hans'

# Windows环境中此项的时区必须和系统一致，设置为 Asia/Shanghai。
# 另外此项设置如果保持 UTC 有可能导致 Django 时间和本地时间不同的情况。
TIME_ZONE = 'Asia/Shanghai'

# 这里必须是 True，否则 LANGUAGE_CODE 会失效
USE_I18N = True
```

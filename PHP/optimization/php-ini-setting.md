# ini 设置

```config
[opcache]
opcache.enable=1
opcache.enable_cli=1
opcache.memory_consumption=128 #分配的内存128M
opcache.max_accelerated_files=10000 #保留最大数量的PHP脚本，一定要比应用中php文件数量大
opcache.interned_strings_buffer=16 #存储驻留字符串的内存量16M
opcache.validate_timestamps=1 #生产环境0（不检测PHP脚本更新），开发环境1
opcache.revalidate_freq=2 # 生产环境0，开发环境每隔多少秒更新脚本
```

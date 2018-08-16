# 上传大文件

上传大文件时，需要调整 php 和 nginx 的参数。

`php.ini`：

```config
upload_max_filesize = 2M
post_max_size = 8M
```

`nginx.conf`:

```config
client_max_body_size
```

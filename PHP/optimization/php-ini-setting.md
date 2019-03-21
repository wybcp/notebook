# ini 设置

```conf
[opcache]
opcache.enable=1
opcache.enable_cli=1
opcache.memory_consumption=128
;分配的内存128M
opcache.max_accelerated_files=10000
;保留最大数量的PHP脚本，一定要比应用中php文件数量大
opcache.interned_strings_buffer=16
;存储驻留字符串的内存量16M
opcache.validate_timestamps=1
;生产环境0（不检测PHP脚本更新），开发环境1
opcache.revalidate_freq=2
; 生产环境0，开发环境每隔多少秒更新脚本

; Enables or disables copying of PHP code (text segment) into HUGE PAGES.
; This should improve performance, but requires appropriate OS configuration.
;opcache.huge_code_pages=0


; Development Value: 4096
; Production Value: 4096
; 修改缓冲区的大小时，确保为4或者8的倍数，对应32位和64位。
; http://php.net/output-buffering
output_buffering = 4096
implicit_flush=false

; display_errors
;   Default Value: On
;   Development Value: On
;   Production Value: Off


; error_reporting
;   Default Value: E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED
;   Development Value: E_ALL
;   Production Value: E_ALL & ~E_DEPRECATED & ~E_STRICT


; 服务器中php版本的信息，建议关闭
; http://php.net/expose-php
expose_php = off

; 关闭危险函数
; http://php.net/disable-functions
disable_functions =system, passthru, exec, shell_exec, popen, phpinfo, escapeshellarg, escapeshellcmd, proc_close, proc_open, dl
;文件及目录操作相关的函数
;disable_functions = chdir, chroot, dir, getcwd, opendir, readdir, scandir, fopen, unlink, delete, copy, mkdir, rmdir, rename, file, file_get_contents, fputs, fwrite, chgrp,chmod, chown

; PHP's default character set is set to UTF-8.
; http://php.net/default-charset
default_charset = "UTF-8"

date.timezone ="Asia/Shanghai"

; Maximum allowed size for uploaded files.
; http://php.net/upload-max-filesize
upload_max_filesize = 2M

; Maximum size of POST data that PHP will accept.
; http://php.net/post-max-size
post_max_size = 8M
```

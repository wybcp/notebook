## curl

curl 用于传输一个 URL。可以使用这条命令用于测试应用程序的端点或与上游服务端点的连接。curl 还可用于检查你的应用程序是否能连接到其他服务，例如数据库，或检查您的服务是否处于健康的状态。

举个例子，假如你的应用程序抛出一个 HTTP 500 错误，表示无法访问 MongoDB 数据库：

```
$ curl -I -s myapplication:5000

HTTP/1.0 500 INTERNAL SERVER ERROR
```

-I 选项用于显示头信息，-s 选项表示使用静默模式，不显示错误和进度。检查数据库的端点是否正确：

```
$ curl -I -s database:27017

HTTP/1.0 200 OK
```

那么可能是什么问题呢？ 检查您的应用程序是否可以访问数据库以外的其他位置：

```
$ curl -I -s https://opensource.com

HTTP/1.1 200 OK
```

看起来这没问题，现在尝试访问数据库。您的应用程序正在使用数据库的主机名，因此请先尝试：

```
$ curl database:27017

curl: (6) Couldn't resolve host 'database'
```

这表示您的应用程序无法解析数据库，因为数据库的 URL 不可用或主机（容器或 VM）没有可用于解析主机名的域名服务器。

## ls

ls 用于列出目录中的文件，系统管理员和开发者会经常使用这个命令。在容器空间中，这条命令可以帮助确定容器镜像中的目录和文件。除了查找文件，ls 还可以用于检查权限。下面的示例中，由于权限问题，你不能运行 myapp。当你使用 ls -l 检查权限时，你会发现它的权限在 -rw-r–r– 中没有”x”，只有读写的权限。

```
$ ./myapp
bash: ./myapp: Permission denied
$ ls -l myapp
-rw-r--r--. 1 root root 33 Jul 21 18:36 myapp
```

## tail

tail 显示文件的最后一部分内容。通常情况下，你不需要浏览每行日志以进行故障排除。而是需要检查日志中对应用程序的最新请求的说明。例如，当你向 Apache HTTP 服务器发起请求时，可以使用 tail 来检查日志中发生的情况。

使用 `tail -f` 来跟踪日志文件并在发起请求时查看它们。

-f 选项表示跟随的意思，它可在日志被写入文件时输出它们。下面的示例具有每隔几秒访问端点的后台脚本，日志会记录请求。除了实时跟踪日志，还可以使用 tail 带上 -n 选项来查看文件的最后 100 行。

```
$ tail -n 100 /var/log/httpd/access_log
```
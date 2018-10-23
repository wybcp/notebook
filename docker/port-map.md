# 端口映射

当容器中运行一些网络应用，要让外部访问这些应用时，可以通过-P 或-p 参数来指定端口映射。当使用-P（大写的）标记时，Docker 会随机映射一个 的端口到内部容器开放的网络端口：

```bash
$ docker run -d -P training/webapp python app.py
ed7bf9a1c95efcc39098e1e59293f89e305c351dc3f7b261d09f7285ce7f98da
$ docker ps -l;
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
ed7bf9a1c95e        training/webapp     "python app.py"     13 seconds ago      Up 12 seconds       0.0.0.0:32769->5000/tcp   infallible_visvesvaraya
$ docker port infallible_visvesvaraya
5000/tcp -> 0.0.0.0:32769
```

## 指定端口

-p（小写的）则可以指定要映射的端口，并且，在一个指定端口上只可以绑定一个容器。支持的格式有 `IP：HostPort：ContainerPort`|`IP：：ContainerPort`|

### `HostPort：ContainerPort`。

多次使用-p 标记可以绑定多个端口。
`docker run -d -p 5000:5000 -p 3000:80 training/webapp python app.py`

### `IP：HostPort：ContainerPort`

映射使用一个特定地址
`$ docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py`

### `IP：：ContainerPort`

绑定 localhost 的任意端口到容器的 5000 端口，本地主机会自动分配一个端口
`$ docker run -d -p 127.0.0.1::5000 training/webapp python app.py`

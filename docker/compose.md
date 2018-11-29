# [compose](https://github.com/docker/compose)

Compose 作为 Docker 官方编排工具，可以让用户通过编写一个简单的模板文件，快速地创建和管理基于 Docker 容器的应用集群。

处理多个容器相互配合来完成某项任务的情况。

- 任务（task）：一个容器被称为一个任务。任务拥有独一无二的 ID，在同一个服务中的多个任务序号依次递增。
- 服务（service）：某个相同应用镜像的容器副本集合，一个服务可以横向扩展为多个容器实例。
- 服务栈（stack）：由多个服务组成，相互配合完成特定业务，如 Web 应用服务、数据库服务共同构成 Web 服务栈，一般由一个 docker-compose.yml 文件定义。

Compose 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 Compose 来进行编排管理。

`pip install -U docker-compose`

在基础模板中只定义一些可以共享的镜像和环境变量，在扩展模板中具体指定应用变量、链接、数据卷等信息。

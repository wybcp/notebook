# [Apiato](https://github.com/apiato/apiato)

Apiato 是一个基于 Laravel 5.6 的框架（5.5 也支持），通过提供一系列适用于 API 开发的工具和函数，可以帮助我们快速构建可扩展、易测试、以 API 为中心的现代 PHP 应用。

从头开始开发一套 API 的所有功能总是件很费时间的事，为此，Apiato 为我们提供了应用 API 开发所需的基础组件，我们只需专注业务逻辑开发即可，从而更快地将 API 接口交付给客户端。

#### 为什么需要 API 驱动的应用？

现在我们处在一个万物互联的时代，过去在 Web 时代我们只需直接从后端返回 HTML 页面给浏览器即可，而随着移动互联网、可穿戴设备的流行和发展，构建跨设备的应用逐渐成为了一种必然趋势，我们不仅要把数据返回给 Web 浏览器，还要提供给手机 App、智能手表等其他设备，这样单纯的 HTML 显然是不够的，我们需要提供一次数据，支持多种设备的渲染，从而满足业务扩展和快速增长，而要满足这种诉求，就需要提供 API 实现与不同终端应用的交互。

而且 API 应用以后也会越来越成为一种趋势，后端只会提供 API 接口，不再与视图层有任何瓜葛，App 与后端的分离很好理解，现在前后端分离也是大势所趋，未来后端将只提供服务和数据，而数据的渲染则完全交给前端来实现。

#### 功能特性

下面我们来看一下 Apiato 到底提供了哪些黑科技：

- 基于 Laravel Passport 实现 API 认证
- RBAC 权限系统
- 全文搜索支持查询参数
- 有效管理用户、权限、令牌等的界面
- 使用 ApiDocJS 生成 API 文档
- 支持 CORS 和 JSONP
- 自动对敏感 ID 进行编码/解码，避免直接对外暴露
- 支持 API 版本
- 通过自定义 JSON 错误响应处理异常
- 支持 ETag 请求头以降低客户端带宽
- 支持本地化
- 自动分页
- WEB 和 API 认证中间件
- 支持 HTTP 请求/响应监控和 DB 查询 Debug
- 使用 Laravel Debugbar 显示性能数据
- 第三方登录支持
- 通过 Fractal 对 JSON 响应和分页结果进行类型转化
- 提供测试辅助函数实现更好的自动化测试（PHPUnit）
- 支持多种响应格式（JSON、数组以及原生数据）
- 自动日期转化
- 支持 Stripe 和 WePay 支付网关
- 系统和用户级别的设置
- 通过请求对象轻松实现验证和授权
- 可维护、可扩展的软件架构模式（Porto SAP）
- 代码生成器命令（包括完整的 CRUD 操作等）
- UI 组件分离（Web、CLI 和 API）
- 管理后台
- 详细的文档
- 支持 100%自定义、开放源码，使用一流的框架、工具、扩展包和标准

### 系统要求

- Git
- PHP >= 7.1.3
- OpenSSL 扩展
- PDO 扩展
- Mbstring 扩展
- Tokenizer 扩展
- BCMath 扩展
- Intl 扩展
- Composer
- Node（生成文档时需要）
- Web 服务器（推荐 Nginx）
- 数据库（MySQL）
- 缓存系统（推荐 Redis）
- 队列系统（推荐 Beanstalkd）

### 安装配置

#### 通过 Composer 自动安装

安装最新版：

```
composer create-project apiato/apiato apiato
```

安装指定版本：

```
composer create-project apiato/apiato apiato ~7.2
```

安装开发版本：

```
composer create-project apiato/apiato apiato dev-master
```

选择上述其中一种方式安装完成后，接下来编辑 `.env` 文件将数据库、缓存、队列等配置按照自己开发环境进行调整。

#### 手动安装

如果你不想通过上述自动安装的方式进行安装的话，还可以选择手动安装：

```
git clone https://github.com/apiato/apiato.git
cd apiato
composer install
cp .env.example .env
php artisan key:generate
```

同样，最后编辑 `.env` 文件，将数据库、缓存、队列等配置按照自己开发环境进行调整。

#### 数据库设置

> 注：在此之前，确保已经将 `.env` 中的数据库按照本地开发环境进行了修改并测试访问通过。

首先通过如下命令完成数据库迁移：

```
php artisan migrate
```

然后为数据库填充测试数据：

```
php artisan db:seed
```

默认情况下 Apiato 会填充一个超级用户，我们可以为其设置 `admin` 权限：

```
php artisan apiato:permissions:toRole admin
```

> 注：如果你是用的是 LaraDock 作为开发环境的话，上述数据库相关 Artisan 命令需要在 `workspace` 容器中完成，可以通过 `docker-compose exec -it workspace bash` 命令进入该容器（有任何问题可以在下面的评论中留言，坑学院君已踩过）。

#### OAuth 2.0 设置

通过运行如下 Artisan 命令即可：

```
php artisan passport:install
```

#### 运行测试

![img](http://static.laravelacademy.org/wp-content/uploads/2018/03/15220826962706.jpg)

#### Web 服务器

如果你使用 Valet 进行本地开发的话，无需任何额外配置，如果使用的是 Homestead 或 LaraDock 的话，需要配置三个域名：`apiato.dev`、`admin.apiato.dev`、`api.apiato.dev`。当然，如果想要在新版 Google 浏览器中访问需要把后缀改为 `.test`，如果修改后缀的话，不要忘了 `.env` 文件的默认后缀也要相应修改：

```
APP_NAME="apiato"
APP_URL=http://apiato.test
API_URL=http://api.apiato.test
```

### 示例演示

打开浏览器，或者 REST 客户端（如 Postman、Paw 等）进行测试。

访问 `http://apiato.test`：

![img](http://static.laravelacademy.org/wp-content/uploads/2018/03/15220831570399.jpg)

访问 `http://api.apiato.test`：

![img](http://static.laravelacademy.org/wp-content/uploads/2018/03/15220832028219.jpg)

官方文档说访问 `http://admin.apiato.test` 会显示登录表单，我这边却是和 `http://apiato.test` 显示内容一样，感觉有毒，不过可以通过 `http://admin.apiato.test/dashboard` 登录：

![img](http://static.laravelacademy.org/wp-content/uploads/2018/03/15220833629554.jpg)

邮箱输入 `admin@admin.com`，密码输入 `admin` 即可成功登录。

接下来我们测试一个注册 API 接口：

![img](http://static.laravelacademy.org/wp-content/uploads/2018/03/15220836453729.jpg)

提示我们没有安装 BC Math 扩展，但其实数据已经插进去了，删除这条数据，安装 BC Math 扩展后重新测试该接口：

![img](http://static.laravelacademy.org/wp-content/uploads/2018/03/15220841488369.jpg)

接口返回成功，数据插入成功。

http://laravelacademy.org/post/9129.html

# [yarn](https://yarnpkg.com/zh-Hans/)

Yarn 配置安装加速：
`$ yarn config set registry https://registry.npm.taobao.org`
Yarn 安装依赖：
`$ SASS_BINARY_SITE=http://npm.taobao.org/mirrors/node-sass yarn`
在 yarn 命令前添加 `SASS_BINARY_SITE=http://npm.taobao.org/mirrors/node-sass` 的目的是告诉 yarn 到淘宝的镜像去下载 node-sass 二进制文件。

`npm run watch-poll`
watch-poll 会在你的终端里持续运行，监控 resources 文件夹下的资源文件是否有发生改变。在 watch-poll 命令运行的情况下，一旦资源文件发生变化，Webpack 会自动重新编译。

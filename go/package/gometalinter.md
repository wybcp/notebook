# [gometalinter](https://github.com/alecthomas/gometalinter)

gometalinter 本身不做代码检查，而是集成了各种 linter，提供统一的配置和输出。我们集成了 vet、golint 和 errcheck 三种检查。

## 使用

cd 到 go 项目下，执行 `gometalinter ./...`

即检查所有目录的 go 文件，此时 vendor 目录下的也会检测

如果是想指定指定目录，执行 gometalinter + 文件夹名。

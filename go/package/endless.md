# [endless](https://github.com/fvbock/endless)

fvbock/endless 来实现 Golang HTTP/HTTPS 服务重新启动的零停机

endless server 监听以下几种信号量：

- syscall.SIGHUP：触发 fork 子进程和重新启动
- syscall.SIGUSR1/syscall.SIGTSTP：被监听，但不会触发任何动作
- syscall.SIGUSR2：触发 hammerTime
- syscall.SIGINT/syscall.SIGTERM：触发服务器关闭（会完成正在运行的请求）
- endless 正正是依靠监听这些信号量，完成管控的一系列动作

## 考虑使用 http.Server 的 Shutdown 方法

endless 热更新是采取创建子进程后，将原进程退出的方式，不符合守护进程的要求

<https://github.com/EDDYCJY/blog/blob/master/golang/gin/2018-03-15-Gin%E5%AE%9E%E8%B7%B5-%E8%BF%9E%E8%BD%BD%E4%B8%83-Golang%E4%BC%98%E9%9B%85%E9%87%8D%E5%90%AFHTTP%E6%9C%8D%E5%8A%A1.md>

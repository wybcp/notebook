# [gitea](https://github.com/go-gitea/gitea)

```bash
#放行端口，如果是IPtables
/sbin/iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
service iptables save
service iptables restart
gitea web --port 80
```

`vim /etc/systemd/system/gitea.service`
[设置开机启动](http://wonse.info/gitea.html)
服务文件内插入如下代码：

```
[Unit]
Description=gitea
[Service]
User=root
ExecStart=home/gitea/gitea
Restart=on-abort
[Install]
WantedBy=multi-user.target
```

注意 ExecStart =后修改为自己 Gitea 的路径
重载 daemon，让新的服务文件生效：

```
systemctl daemon-reload
```

现在就可以用 systemctl 来启动 gitea 了：

```
systemctl start gitea
```

设置开机启动：`systemctl enable gitea`

停止、查看状态可以用：

```
systemctl stop gitea
systemctl status gitea
```

## 启动

### 启动 redis

#### 默认配置

```
$ redis-server
```

#### 配置文件（建议）

```
$ redis-server /path/to/redis.conf
```

重要配置：
config | config introduction
---|---
port | 端口
logfile | 日志文件
dir | redis工作目录（存放持久化和日志文件）
daemonize| 是否以进程守护的方式启动redis

#### 运行配置（不建议）

常见选项：

```shell
./redis-server --port 7777
./redis-server --port 7777 --slaveof 127.0.0.1 8888
./redis-server /etc/myredis.conf --loglevel verbose
```

### 启动redis-sentinel

```shell
./redis-server /etc/sentinel.conf –sentinel
./redis-sentinel /etc/sentinel.conf
```

部署后可以使用sstart对redis 和sentinel进行拉起，使用sctl进行supervisorctl的控制。（两个alias）

## 停止

```shell
redis-cli shutdown
```

sentinel方法一样，只是需要执行sentinel的连接端口

注意：正确关闭服务器方式是`redis-cli shutdown` 或者 kill，都会graceful shutdown，保证写RDB文件以及将AOF文件fsync到磁盘，不会丢失数据。 如果是粗暴的Ctrl+C，或者`kill -9` 就可能丢失。如果有配置save，还希望在shutdown时进行RDB写入，那么请使用`shutdown save`命令。

## 查看和修改配置

查看：

    config get ：获取服务器配置信息。
    redis 127.0.0.1:6379> config get dir
    config get *：查看所有配置

修改：

    临时设置：config set
    永久设置：config rewrite，将目前服务器的参数配置写入redis conf.

## 内存、CPU规划

一定要设置最大内存maxmemory参数，否则物理内存用爆了就会大量使用Swap，写RDB文件时的速度很慢。注意这个参数指的是info中的used_memory，在一些不利于jmalloc的时候，内存碎片会很大。

多留55%内存是最安全的。重写AOF文件和RDB文件的进程(即使不做持久化，复制到Slave的时候也要写RDB)会fork出一条新进程来，采用了操作系统的Copy-On-Write策略(子进程与父进程共享Page。如果父进程的Page-每页4K有修改，父进程自己创建那个Page的副本，不会影响到子进程)。

另外，需要考虑内存碎片，假设碎片为1.2，则如果机器为64G，那么64*45%/1.2 = 24G作为maxmemory是比较安全的规划。

留意Console打出来的报告，如"RDB: 1215 MB of memory used by copy-on-write"。在系统极度繁忙时，如果父进程的所有Page在子进程写RDB过程中都被修改过了，就需要两倍内存。

按照Redis启动时的提醒，设置

```shell
echo "vm.overcommit_memory = 1" >>  /etc/sysctl.conf
```

使得fork()一条10G的进程时，因为COW策略而不一定需要有10G的free memory。

另外，记得关闭THP，这个默认的Linux内存页面大小分配策略会导致RDB时出现巨大的latency和巨大的内存占用。关闭方法为：

```shell
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```

当最大内存到达时，按照配置的Policy进行处理， 默认策略为volatile-lru，对设置了expire time的key进行LRU清除(不是按实际expire time)。如果沒有数据设置了expire time或者policy为noeviction，则直接报错，但此时系统仍支持get之类的读操作。 另外还有几种policy，比如volatile-ttl按最接近expire time的，allkeys-lru对所有key都做LRU。注意在一般的缓存系统中，如果没有设置超时时间，则lru的策略需要设置为allkeys-lru，并且应用需要做好未命中的异常处理。特殊的，当redis当做DB时，请使用noneviction策略，但是需要对系统内存监控加强粒度。

CPU不求核数多，但求主频高，Cache大，因为redis主处理模式是单进程的,同时避免使用虚拟机。

redis参数设置技巧列表：

1. Daemonize 这个参数在使用supervisord这种进程管理工具时一定要设置为no，否则无法使用这些工具将redis启动。
2. Dir RDB的位置，一定要事先创建好，并且启动redis 的用户对此目录要有读写权限。
3. Include 如果是多实例的话可以将公共的设置放在一个conf文件中，然后引用即可： include /redis/conf/redis-common.conf


## 使用supervisord进行进程管理

Supervisord是一个优秀的进程管理工具，一般在部署redis时采用它来进行redis、sentinel等进程的管理，一个已经在生产环境采用的supervisord配置文件如下：
```
; Sample supervisor config file. 
; 
; For more information on the config file, please see: 
; http://supervisord.org/configuration.html 
; 
; Notes: 
; - Shell expansion ("~" or "$HOME") is not supported. Environment 
; variables can be expanded using this syntax: "%(ENV_HOME)s". 
; - Comments must have a leading space: "a=b ;comment" not "a=b;comment". 

[unix_http_server] 
file=/smsred/redis-3.0.4/run/supervisor.sock ; (the path to the socket file) 
;chmod=0700 ; socket file mode (default 0700) 
;chown=nobody:nogroup ; socket file uid:gid owner 
;username=user ; (default is no username (open server)) 
;password=123 ; (default is no password (open server)) 

;[inet_http_server] ; inet (TCP) server disabled by default 
;port=127.0.0.1:9001 ; (ip_address:port specifier, *:port for all iface) 
;username=user ; (default is no username (open server)) 
;password=123 ; (default is no password (open server)) 

[supervisord] 
logfile=/smsred/redis-3.0.4/log/supervisord.log ; (main log file;default $CWD/supervisord.log) 
logfile_maxbytes=50MB ; (max main logfile bytes b4 rotation;default 50MB) 
logfile_backups=10 ; (num of main logfile rotation backups;default 10) 
loglevel=info ; (log level;default info; others: debug,warn,trace) 
pidfile=/smsred/redis-3.0.4/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid) 
nodaemon=false ; (start in foreground if true;default false) 
minfds=1024 ; (min. avail startup file descriptors;default 1024) 
minprocs=200 ; (min. avail process descriptors;default 200) 
;umask=022 ; (process file creation umask;default 022) 
;user=chrism ; (default is current user, required if root) 
;identifier=supervisor ; (supervisord identifier, default is 'supervisor') 
;directory=/tmp ; (default is not to cd during start) 
;nocleanup=true ; (don't clean up tempfiles at start;default false) 
;childlogdir=/tmp ; ('AUTO' child log dir, default $TEMP) 
;environment=KEY="value" ; (key value pairs to add to environment) 
;strip_ansi=false ; (strip ansi escape codes in logs; def. false) 

; the below section must remain in the config file for RPC 
; (supervisorctl/web interface) to work, additional interfaces may be 
; added by defining them in separate rpcinterface: sections 
[rpcinterface:supervisor] 
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface 

[supervisorctl] 
serverurl=unix:///smsred/redis-3.0.4/run/supervisor.sock ; use a unix:// URL for a unix socket 
;serverurl=http://127.0.0.1:9001 ; use an http:// url to specify an inet socket 
;username=chris ; should be same as http_username if set 
;password=123 ; should be same as http_password if set 
;prompt=mysupervisor ; cmd line prompt (default "supervisor") 
;history_file=~/.sc_history ; use readline history if available 

; The below sample program section shows all possible program subsection values, 
; create one or more 'real' program: sections to be able to control them under 
; supervisor. 

;[program:theprogramname] 
;command=/bin/cat ; the program (relative uses PATH, can take args) 
;process_name=%(program_name)s ; process_name expr (default %(program_name)s) 
;numprocs=1 ; number of processes copies to start (def 1) 
;directory=/tmp ; directory to cwd to before exec (def no cwd) 
;umask=022 ; umask for process (default None) 
;priority=999 ; the relative start priority (default 999) 
;autostart=true ; start at supervisord start (default: true) 
;autorestart=unexpected ; whether/when to restart (default: unexpected) 
;startsecs=1 ; number of secs prog must stay running (def. 1) 
;startretries=3 ; max # of serial start failures (default 3) 
;exitcodes=0,2 ; 'expected' exit codes for process (default 0,2) 
;stopsignal=QUIT ; signal used to kill process (default TERM) 
;stopwaitsecs=10 ; max num secs to wait b4 SIGKILL (default 10) 
;stopasgroup=false ; send stop signal to the UNIX process group (default false) 
;killasgroup=false ; SIGKILL the UNIX process group (def false) 
;user=chrism ; setuid to this UNIX account to run the program 
;redirect_stderr=true ; redirect proc stderr to stdout (default false) 
;stdout_logfile=/a/path ; stdout log path, NONE for none; default AUTO 
;stdout_logfile_maxbytes=1MB ; max # logfile bytes b4 rotation (default 50MB) 
;stdout_logfile_backups=10 ; # of stdout logfile backups (default 10) 
;stdout_capture_maxbytes=1MB ; number of bytes in 'capturemode' (default 0) 
;stdout_events_enabled=false ; emit events on stdout writes (default false) 
;stderr_logfile=/a/path ; stderr log path, NONE for none; default AUTO 
;stderr_logfile_maxbytes=1MB ; max # logfile bytes b4 rotation (default 50MB) 
;stderr_logfile_backups=10 ; # of stderr logfile backups (default 10) 
;stderr_capture_maxbytes=1MB ; number of bytes in 'capturemode' (default 0) 
;stderr_events_enabled=false ; emit events on stderr writes (default false) 
;environment=A="1",B="2" ; process environment additions (def no adds) 
;serverurl=AUTO ; override serverurl computation (childutils) 

; The below sample eventlistener section shows all possible 
; eventlistener subsection values, create one or more 'real' 
; eventlistener: sections to be able to handle event notifications 
; sent by supervisor.

;[eventlistener:theeventlistenername]
;command=/bin/eventlistener ; the program (relative uses PATH, can take args) 
;process_name=%(program_name)s ; process_name expr (default %(program_name)s) 
;numprocs=1 ; number of processes copies to start (def 1) 
;events=EVENT ; event notif. types to subscribe to (req'd) 
;buffer_size=10 ; event buffer queue size (default 10) 
;directory=/tmp ; directory to cwd to before exec (def no cwd) 
;umask=022 ; umask for process (default None) 
;priority=-1 ; the relative start priority (default -1) 
;autostart=true ; start at supervisord start (default: true) 
;autorestart=unexpected ; whether/when to restart (default: unexpected) 
;startsecs=1 ; number of secs prog must stay running (def. 1) 
;startretries=3 ; max # of serial start failures (default 3) 
;exitcodes=0,2 ; 'expected' exit codes for process (default 0,2) 
;stopsignal=QUIT ; signal used to kill process (default TERM) 
;stopwaitsecs=10 ; max num secs to wait b4 SIGKILL (default 10) 
;stopasgroup=false ; send stop signal to the UNIX process group (default false) 
;killasgroup=false ; SIGKILL the UNIX process group (def false) 
;user=chrism ; setuid to this UNIX account to run the program 
;redirect_stderr=true ; redirect proc stderr to stdout (default false) 
;stdout_logfile=/a/path ; stdout log path, NONE for none; default AUTO 
;stdout_logfile_maxbytes=1MB ; max # logfile bytes b4 rotation (default 50MB) 
;stdout_logfile_backups=10 ; # of stdout logfile backups (default 10) 
;stdout_events_enabled=false ; emit events on stdout writes (default false) 
;stderr_logfile=/a/path ; stderr log path, NONE for none; default AUTO 
;stderr_logfile_maxbytes=1MB ; max # logfile bytes b4 rotation (default 50MB) 
;stderr_logfile_backups ; # of stderr logfile backups (default 10) 
;stderr_events_enabled=false ; emit events on stderr writes (default false) 
;environment=A="1",B="2" ; process environment additions 
;serverurl=AUTO ; override serverurl computation (childutils) 

; The below sample group section shows all possible group values, 
; create one or more 'real' group: sections to create "heterogeneous" 
; process groups.

;[group:thegroupname]
;programs=progname1,progname2 ; each refers to 'x' in [program:x] definitions 
;priority=999 ; the relative start priority (default 999) 

; The [include] section can just contain the "files" setting. This 
; setting can list multiple files (separated by whitespace or 
; newlines). It can also contain wildcards. The filenames are 
; interpreted as relative to this file. Included files *cannot* 
; include files themselves.

;[include]
;files = relative/directory/*.ini

[program:redis-1xxx]
command=/smsred/redis-3.0.4/bin/redis-server /smsred/redis-3.0.4/conf/redis-1xxx.conf 
autostart=true
autorestart=false
user=smsred
stdout_logfile=/smsred/redis-3.0.4/log/redis-1xxx.out.log 
stderr_logfile=/smsred/redis-3.0.4/log/redis-1xxx.err.log 
priority=1000

[program:redis-1xxx]
command=/smsred/redis-3.0.4/bin/redis-server /smsred/redis-3.0.4/conf/redis-1xxx.conf 
autostart=true
autorestart=false
user=smsred
stdout_logfile=/smsred/redis-3.0.4/log/redis-1xxx.out.log 
stderr_logfile=/smsred/redis-3.0.4/log/redis-1xxx.err.log 
priority=1000

[program:redis-1xxx]
command=/smsred/redis-3.0.4/bin/redis-server /smsred/redis-3.0.4/conf/redis-1xxx.conf 
autostart=true
autorestart=false
user=smsred
stdout_logfile=/smsred/redis-3.0.4/log/redis-1xxx.out.log 
stderr_logfile=/smsred/redis-3.0.4/log/redis-1xxx.err.log 
priority=1000

[program:redis-sentinel]
command =/smsred/redis-3.0.4/bin/redis-sentinel /smsred/redis-3.0.4/conf/sentinel.conf 
autostart=true
autorestart=true
startsecs=3
```

## 使用alias方便操作

如果开多实例，那么shell下进行操作的次数会很多，因此你需要一些alias进行命令的缩短，这个技巧并不高深，但是很实用。一个实例如下：

```shell
alias cli1='$HOME/redis-3.0.4/bin/redis-cli -a xxx -p 1xx'
alias cli2='$HOME/redis-3.0.4/bin/redis-cli -a xxx -p 1xx'
alias cli3='$HOME/redis-3.0.4/bin/redis-cli -a xxx -p 1xx'
alias clis='$HOME/redis-3.0.4/bin/redis-cli -p 26379'

alias sctl='supervisorctl -c $HOME/redis-3.0.4/conf/redis-supervisord.conf '
alias sstart='supervisord -c $HOME/redis-3.0.4/conf/redis-supervisord.conf'
alias see='pdsh -R ssh -w MSMSRED[1-3],PSMSRED1,PSMSAPP1 "/usr/local/bin/supervisorctl -c /smsred/redis-3.0.4/conf/redis-supervisord.conf status "'
```

## 使用pdsh/pdcp进行多机器操作

Pdsh/pdcp是一个python ssh多机操作的工具，在部署中可以采用它进行多机的同一操作批量执行，注意编译的时候把ssh编译进去，在执行时指定ssh模式，一个查看多机supervisord管理进程的命令实例如下：

```shell
pdsh -R ssh -w MSMSRED[1-3],PSMSRED1,PSMSAPP1 "/usr/local/bin/supervisorctl -c /smsred/redis-3.0.4/conf/redis-supervisord.conf status "
```

前提是你这些机器已经建立了ssh互信。建立互信可以用下边这个脚本
```
#!/bin/bash 
#2015-12-08 
#author gnuhpc 

expect -c "spawn ssh-keygen -t rsa 
expect { 
\":\" {send \"\r\"; exp_continue} 
\"*(y/n)*\" {send \"y\r\"; exp_continue} 
} 
" 
for p in $(cat ip.cfg) 
do 
ip=$(echo "$p"|cut -f1 -d":") 
username=$(echo "$p"|cut -f2 -d":") 
password=$(echo "$p"|cut -f3 -d":") 
echo $password 

expect -c " 
spawn ssh-copy-id ${username}@$ip 
expect { 
\"*yes/no*\" {send \"yes\r\"; exp_continue} 
\"*(y/n)*\" {send \"y\r\"; exp_continue} 
\"*password*\" {send \"$password\r\"; exp_continue} 
\"*Password*\" {send \"$password\r\"; exp_continue} 
} 
" 
expect -c "
spawn ssh ${username}@$ip "hostname"
expect {
\"*yes/no*\" {send \"yes\r\"; exp_continue}
\"*password*\" {send \"$password\r\"; exp_continue}
\"*(y/n)*\" {send \"y\r\"; exp_continue}
\"*Password*\" {send \"$password\r\";}
}
"
done
```

指定一个ip.cfg，里面的格式为：IP（主机名也行，只要能解析）:用户名:密码
例如：
```
xxxx.139:username:password
xxxx.140:username:password
xxxx.141:username:password
xxxx.142:username:password
xxxx.137:username:password
```

## 使用脚本进行sentinel配置文件的备份

Sentinel在启动、切换时会对config文件进行rewrite，在上线前或者某些手动维护后你可能希望把conf文件都变为最初，当系统中有很多redis实例时，这个手工操作会让人疯掉，那不妨写个脚本在配置好sentinel和redis后不启动先备份一下，测试完毕后再恢复。

一个简单的备份脚本`backupconf.sh`如下：

```config
#!/bin/bash
for i in `find ~/redis-3.0.4/conf -name *.conf`
do
cp -v $i ${i}.bak
done
```

恢复脚本`recoveryconf.sh`：

```config
#!/bin/bash
for i in `find ~/redis-3.0.4/conf -name *.conf.bak`
do
cp -v $i ${i%.*}
done
```
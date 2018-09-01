# 网站性能测试

怎么去评定一个网站的性能，网站在高并发下的测试，服务器端的测试，下面是几种方案
mysql 基准测试工具等简介 google page speed test ,ab test，mysqlslap,sysbench

## 一. google page test

登陆 google，搜索 [google page speed test](https://developers.google.com/speed/pagespeed/insights/)
进入后，在输入框中输入自己要输入的内容然后确认

## 二. ab test

简介
ab 是一个 Apache HTTP 服务器基准测试工具，它可以测试 HTTP 服务器每秒可以处理多少个请求，如果测试的是 WEB 服务，这个结果可以转换为整个应用每秒可以处理多少个应用

1. 安裝 ab 命令
   sudo apt-get install apache2-utils
2. ab 命令参数说明
   可以暂时不看直接看下面如何使用，有其他需求再看这里

    ```config
    Options are:
    -n requests Number of requests to perform
    -c concurrency Number of multiple requests to make at a time
    -t timelimit Seconds to max. to spend on benchmarking
    This implies -n 50000
    -s timeout Seconds to max. wait for each response
    Default is 30 seconds
    -b windowsize Size of TCP send/receive buffer, in bytes
    -B address Address to bind to when making outgoing connections
    -p postfile File containing data to POST. Remember also to set -T
    -u putfile File containing data to PUT. Remember also to set -T
    -T content-type Content-type header to use for POST/PUT data, eg.
    'application/x-www-form-urlencoded'
    Default is 'text/plain'
    -v verbosity How much troubleshooting info to print
    -w Print out results in HTML tables
    -i Use HEAD instead of GET
    -x attributes String to insert as table attributes
    -y attributes String to insert as tr attributes
    -z attributes String to insert as td or th attributes
    -C attribute Add cookie, eg. 'Apache=1234'. (repeatable)
    -H attribute Add Arbitrary header line, eg. 'Accept-Encoding: gzip'
    Inserted after all normal header lines. (repeatable)
    -A attribute Add Basic WWW Authentication, the attributes
    are a colon separated username and password.
    -P attribute Add Basic Proxy Authentication, the attributes
    are a colon separated username and password.
    -X proxy:port Proxyserver and port number to use
    -V Print version number and exit
    -k Use HTTP KeepAlive feature
    -d Do not show percentiles served table.
    -S Do not show confidence estimators and warnings.
    -q Do not show progress when doing more than 150 requests
    -l Accept variable document length (use this for dynamic pages)
    -g filename Output collected data to gnuplot format file.
    -e filename Output CSV file with percentages served
    -r Don't exit on socket receive errors.
    -m method Method name
    -h Display usage information (this message)
    -Z ciphersuite Specify SSL/TLS cipher suite (See openssl ciphers)
    -f protocol Specify SSL/TLS protocol
    (SSL3, TLS1, TLS1.1, TLS1.2 or ALL)
    ```

3. 运行 ab

   `ab -n 100 -c 10 https://www.baidu.com/`
   对 `https://www.baidu.com/` 进行 100 次请求，10 个并发请求压力测试结果。

    ```
    This is ApacheBench, Version 2.3 <$Revision: 1638069 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking www.baidu.com (be patient).....done

    Server Software: bfe/1.0.8.18
    Server Hostname: www.baidu.com
    Server Port: 443
    SSL/TLS Protocol: TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128

    Document Path: /
    Document Length: 227 bytes

    Concurrency Level: 10
    Time taken for tests: 0.321 seconds
    Complete requests: 100
    Failed requests: 0
    Total transferred: 103266 bytes
    HTML transferred: 22700 bytes
    Requests per second: 311.94 [#/sec] (mean)
    Time per request: 32.057 [ms] (mean)
    Time per request: 3.206 [ms] (mean, across all concurrent requests)
    Transfer rate: 314.58 [Kbytes/sec] received

    Connection Times (ms)
    min mean[+/-sd] median max
    Connect: 19 24 3.1 24 33
    Processing: 5 7 1.2 7 13
    Waiting: 5 7 1.2 7 13
    Total: 25 31 3.5 31 41

    Percentage of the requests served within a certain time (ms)
    50% 31
    66% 32
    75% 34
    80% 34
    90% 36
    95% 37
    98% 41
    99% 41
    100% 41 (longest request)
    ```

4. ab 结果分析 : 1. 19 行 Failed request 数目 2. 23 行 Time per request: 32.057 [ms](mean) 平均每个请求使用的数目 3. 35-43 行大概的响应时间
   例如第一个 50% 31 表示百分之 50 的时间在 31 毫秒之内完成

其中有个注意的点 如果你 failed request 太多，看看是不是并发太多导致项目崩溃，也有可能你这个页面是动态的，每次返回的值不一样，这个 ab 工具也会默认为失败

## 三：mysqlslap

简介：
这是 mysql 自带的测试工具，可以模拟服务器的负载，并且输出计时信息，我觉得最重要的是他能指定特点的 sql 语句，你可以查看该语句在高并发下的执行情况
，这里主要介绍指定的 sql，假如你的数据库有个数据库名字为 database1，数据库中表的名字为 city 表，我们需要随机取出 10 条，然后查看该语句的性能，数据库用户名为 root，密码为 123
指定 sql 测试
直接执行

```bash
mysqlslap -uroot -p123 --iterations=1 --concurrency=1,10 --number-of-queries=100
 --create-schema="databases1" --query="select * from city order by rand() limit 10;"
```

介绍 --concurency = 1,10 表示分别以 1 个并发，10 个并发 --number-of-queries=100 总共发出 100 个请求所用时间 --iterations=1 只运行一次就出结果，建议多写几次，会更准确
其实还有很多功能，例如可以测试不同的引擎等

输出结果分析：

我感觉我和网上其他人的结果分析不太一样，不知道是自己想错了还是别人错了，以后再分析

```
Benchmark
Average number of seconds to run all queries: 2.442 seconds //执行这100个请求用时平均数，这里并发数为1，所以平均每个查询用时为2.442/100=0.0242秒
Minimum number of seconds to run all queries: 2.442 seconds //上面是平均，这里是最小时间，只有当 --iterations大于1，让其多迭代几次后，这个数才有变化
Maximum number of seconds to run all queries: 2.442 seconds //上面是平均，这里是最大时间,只有当 --iterations大于1，让其多迭代几次后，这个数才有变化
Number of clients running queries: 1 并发数(客户端)的数目为1
Average number of queries per client: 100 //平均每个链接查询的数目

Benchmark
Average number of seconds to run all queries: 1.603 seconds //执行这100个请求用时平均数，这里并发数为10,平均每个线程(客户端查询数目为10)查询10次，所以平均每个线程(客户端)查询用时为1.603/10=0.163秒，相对于1个并发的0.024秒，明显并发10个后每个查询就慢了。
Minimum number of seconds to run all queries: 1.603 seconds
Maximum number of seconds to run all queries: 1.603 seconds
Number of clients running queries: 10
Average number of queries per client: 10 平均每个线程(客户端)查询的数目
更多常用功能：
1) --concurrency代表并发数量，多个可以用逗号隔开,例如：concurrency=10,50,100, 并发连接线程数分别是10、50、100个并发。
2) --engines代表要测试的引擎，可以有多个，用分隔符隔开。
3) --iterations代表要运行这些测试多少次。
4) --auto-generate-sql 代表用系统自己生成的SQL脚本来测试。
5）--auto-generate-sql-load-type 代表要测试的是读还是写还是两者混合的（read,write,update,mixed）
6) --number-of-queries 代表总共要运行多少次查询。每个客户端运行的查询数量可以用查询总数/并发数来计算。
7) --debug-info 代表要额外输出CPU以及内存的相关信息。
8) --number-int-cols ：创建测试表的 int 型字段数量
9) --auto-generate-sql-add-autoincrement : 代表对生成的表自动添加auto_increment列，从5.1.18版本开始
10) --number-char-cols 创建测试表的 char 型字段数量。
11) --create-schema 测试的schema，MySQL中schema也就是database，如果存在就不创建。
12) --query  使用自定义脚本执行测试，例如可以调用自定义的一个存储过程或者sql语句来执行测试。
13) --only-print 如果只想打印看看SQL语句是什么，可以用这个选项。
14) --create　指定创建表的语句或含有创建表sql的文件
15) --no-drop 在测试过程中不删除任何schema
```

个人看法：
mysqkslap 只不过是测试服务器的性能，想要测试某一条语句在高并发下的执行速度，感觉不是很可靠，其实用 ab test，或者 screaming frog for seo 工具进行直接测试可能更好。

## 四：sysbench

sysbench 的提供的基准测试功能的 Linux 版本。它支持测试 CPU，内存，文件 I
/ O，互斥性能 甚至支持 mysql 的性能。

安装
On Debian/Ubuntu 等系统可以直接执行下面的命令进行安装
apt-get install sysbench
查看是否按照成功以及使用方法
man sysbench
如果出现以下那么就成功
SYSBENCH(1) sysbench User Manual SYSBENCH(1)
SYSBENCH(1) sysbench User Manual SYSBENCH(1)

使用方法
这里只介绍查看 mysql 的性能的方法:
假如有个数据库名字角 databases1，数据库名字为 root，密码为 123
准备一张表,这一句话必须执行

```bash
sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=databases1
 --mysql-user=root --mysql-password=123
 prepare
```

这里会在你填写的数据库中生成一张 sbtest 表,里面的内容有 100000 条数据
之后，运行下面的语句：

```bash
sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=databases1 --mysql-user=root --mysql-password=123
 --max-time=60 --oltp-read-only=on --max-requests=0 --num-threads=8 run
```

这句话的解释：
--num-threads=8 表示使用的线程为 8 个
--oltp-table-size=1000000 表示测试表的记录总数为 500000 条

最后结果显示分析

```
OLTP test statistics:
    queries performed:
        read:                            2253860 //总读数
        write:                           0 //总写数
        other:                           321980 //其他的操作
        total:                           2575840 //其他操作总数
    transactions:                        160990 (2683.06 per sec.) // 总事务数(每秒事务数)
    deadlocks:                           0      (0.00 per sec.) //-- 发生死锁总数
    read/write requests:                 2253860 (37562.81 per sec.) // -- 读写总数(每秒读写次数)
    other operations:                    321980 (5366.12 per sec.) //-- 其他操作总数(每秒其他操作次数)
```

```
Test execution summary:
    total time:                          60.0024s //总耗时
    total number of events:              160990 一共发生多少事物
    total time taken by event execution: 479.3419
    per-request statistics: --响应时间统计
         min:                                  0.81ms
         avg:                                  2.98ms
         max:                               3283.40ms
         approx.  95 percentile:               4.62ms

Threads fairness:
    events (avg/stddev):           20123.7500/63.52
    execution time (avg/stddev):   59.9177/0.00
```

其他通用选项：

```
--num-threads=N：需要使用的线程总数（默认值为1）。
--max-requests=N：请求总数的上限值（默认值为10000）。
--max-time=N：总执行时间的上限值，以秒为单位（默认值为0，表示执行时间无限）。
--forced-shutdown=STRING：在–max-time之后，强制停止之前，需要等待的时间总量（默认值为off）。
--thread-stack-size=SIZE：每个线程的栈空间的大小（默认值为32KB）。
--init-rng=[on|off]：是否初始化随机数生成器（默认值为off）。
--seed-rng=N：随机数生成器的种子，当为0时忽略（默认值为0）。
--tx-rate=N：目标事务速率（TPS）（默认值为0）。
--tx-jitter=N：目标事务变化率，以毫秒为单位（默认值为0）。
--report-interval=N：指定一个间隔时间，sysbench便会定期地报告测试期间的中间统计结果，以秒为单位。若取值为0，则表示禁用中间报告功能（默认值为0）。
--report-checkpoints=[LIST,...]：在指定的时间点，转储完整的统计数据，并且复位所有的计数器。这个选项的参数是一个由逗号分隔的值，表示从测试开始到必须执行报告检查点时需要花费的时间，以秒为单位。默认禁用报告检查点。
--test=STRING：需要运行的测试项。
--debug=[on|off]：输出更多的调试信息（默认值为off）。
--validate=[on|off]：在可能的情况下执行有效性检查。
--help=[on|off]：输出帮助信息，然后退出。
--version=[on|off]：输出版本信息，然后退出。
```

使用心得：
这个不能测试单条语句的性能，只能测试服务器中该数据库的性能，如果有一些服务器或者机器的对比，才能看得出效果

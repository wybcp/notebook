# [logstash](https://www.elastic.co/cn/downloads/logstash)

数据采集

## [安装](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

## mysql-connector-java-8.0.20.jar

Directory: `C:\Program Files (x86)\MySQL\Connector J 8.0\mysql-connector-java-8.0.20.jar`

增量读取MySQL数据

```config
input {
    stdin {
    }
    jdbc {
      # mysql jdbc connection string to our backup databse
      jdbc_connection_string => "jdbc:mysql://localhost:3306/test"
      # the user we wish to excute our statement as
      jdbc_user => "root"
      jdbc_password => "1x@zs20$"
      # the path to our downloaded jdbc driver
      jdbc_driver_library => "./lib/mysql-connector-java-5.1.17.jar"
      # the name of the driver class for mysql
      jdbc_driver_class => "com.mysql.jdbc.Driver"
      #开启分页查询（默认false不开启）
      #jdbc_paging_enabled => "true"
      #单次分页查询条数
      #jdbc_page_size => "50000"
      #type => "jdbc"
      #last_run_metadata_path => "/home/config/test.log"

      #执行myqsl的语句
      statement => "select * from web_crawler_tbl where id > :sql_last_value"
      #是否使用列值作为依据，进行上次运行位置的记录
      #如果设置为true，则使用tracking_column定义的列，作为:sql_last_value.
      #如果设置为false，则:sql_last_value反映的是上次SQL的运行时间。
      use_column_value => true
      tracking_column => "id"
      #是否记录本次采集数据的位置
      record_last_run => true

      #sql脚本执行的频率，同步频率(分 时 天 月 年)，默认每分钟同步一次，如下*/2是两分钟一次
      schedule => "*/2 * * * *"

    }
}
output {
    file {
            path => "/root/test-%{+YYYY-MM-dd}.txt"
            }
    stdout{
            codec => json_lines
        }
}
```

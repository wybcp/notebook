# 日志类

使用 PHP 开发的日志处理类，本类可自定义多种日志配置，根据标签对应配置。代码中方便调用此类进行日志记录操作。

## 功能：

1. 自定义日志根目录及日志文件名称。
2. 使用日期时间格式自定义日志目录。
3. 自动创建不存在的日志目录。
4. 记录不同分类的日志，例如信息日志，警告日志，错误日志。
5. 可自定义日志配置，日志根据标签调用不同的日志配置。

## Log 类

```php
<?php
/**
 * php日志类
 * Date:    2017-08-27
 * Author:  fdipzone
 * Version: 1.0
 *
 * Description:
 * 1.自定义日志根目录及日志文件名称。
 * 2.使用日期时间格式自定义日志目录。
 * 3.自动创建不存在的日志目录。
 * 4.记录不同分类的日志，例如信息日志，警告日志，错误日志。
 * 5.可自定义日志配置，日志根据标签调用不同的日志配置。
 *
 * Func
 * public  static setConfig 设置配置
 * public  static getLogger 获取日志类对象
 * public  info              写入信息日志
 * public  warn              写入警告日志
 * public  error             写入错误日志
 * private add               写入日志
 * private createLogPath   创建日志目录
 * private getLogFile      获取日志文件名称
 */
class Log {

    // 日志根目录
    private $_log_path = '.';

    // 日志文件
    private $_log_file = 'default.log';

    // 日志自定义目录
    private $_format = 'Y/m/d';

    // 日志标签
    private $_tag = 'default';

    // 总配置设定
    private static $_CONFIG;

    /**
     * 设置配置
     * @param  array $config 总配置设定
     */
    public static function setConfig($config=array()){
        self::$_CONFIG = $config;
    }

    /**
     * 获取日志类对象
     * @param  array $config 总配置设定
     * @return object
     */
    public static function getLogger($tag='default'){

        // 根据tag从总配置中获取对应设定，如不存在使用default设定
        $config = isset(self::$_CONFIG[$tag])? self::$_CONFIG[$tag] : (isset(self::$_CONFIG['default'])? self::$_CONFIG['default'] : array());

        // 设置标签
        $config['tag'] = $tag!='' && $tag!='default'? $tag : '-';

        // 返回日志类对象
        return new Log($config);
    }

    /**
     * 初始化
     * @param array $config 配置设定
     */
    public function __construct($config=array()){

        // 日志根目录
        if(isset($config['log_path'])){
            $this->_log_path = $config['log_path'];
        }

        // 日志文件
        if(isset($config['log_file'])){
            $this->_log_file = $config['log_file'];
        }

        // 日志自定义目录
        if(isset($config['format'])){
            $this->_format = $config['format'];
        }

        // 日志标签
        if(isset($config['tag'])){
            $this->_tag = $config['tag'];
        }

    }

    /**
     * 写入信息日志
     * @param  String $data 信息数据
     * @return Boolean
     */
    public function info($data){
        return $this->add('INFO', $data);
    }

    /**
     * 写入警告日志
     * @param  String  $data 警告数据
     * @return Boolean
     */
    public function warn($data){
        return $this->add('WARN', $data);
    }

    /**
     * 写入错误日志
     * @param  String  $data 错误数据
     * @return Boolean
     */
    public function error($data){
        return $this->add('ERROR', $data);
    }

    /**
     * 写入日志
     * @param  String  $type 日志类型
     * @param  String  $data 日志数据
     * @return Boolean
     */
    private function add($type, $data){

        // 获取日志文件
        $log_file = $this->getLogFile();

        // 创建日志目录
        $is_create = $this->createLogPath(dirname($log_file));

        // 创建日期时间对象
        $dt = new DateTime;

        // 日志内容
        $log_data = sprintf('[%s] %-5s %s %s'.PHP_EOL, $dt->format('Y-m-d H:i:s'), $type, $this->_tag, $data);

        // 写入日志文件
        if($is_create){
            return file_put_contents($log_file, $log_data, FILE_APPEND);
        }

        return false;

    }

    /**
     * 创建日志目录
     * @param  String  $log_path 日志目录
     * @return Boolean
     */
    private function createLogPath($log_path){
        if(!is_dir($log_path)){
            return mkdir($log_path, 0777, true);
        }
        return true;
    }

    /**
     * 获取日志文件名称
     * @return String
     */
    private function getLogFile(){

        // 创建日期时间对象
        $dt = new DateTime;

        // 计算日志目录格式
        return sprintf("%s/%s/%s", $this->_log_path, $dt->format($this->_format), $this->_log_file);

    }

}
```

## Log demo

```php
<?php
/**
 * Created by PhpStorm.
 * User: riverside
 * Date: 2017/8/28
 */

require 'Log.class.php';

define('Log_PATH', dirname(__FILE__).'/logs');

// 总配置设定
$config = array(
    'default' => array(
        'log_path' => Log_PATH,       // 日志根目录
        'log_file' => 'default.log',  // 日志文件
        'format' => 'Y/m/d',          // 日志自定义目录，使用日期时间定义
    ),
    'user' => array(
        'log_path' => Log_PATH,
        'log_file' => 'user.log',
        'format' => 'Y/m/d',
    ),
    'order' => array(
        'log_path' => Log_PATH,
        'log_file' => 'order.log',
        'format' => 'Y/m/d',
    ),
);

// 设置总配置
Log::setConfig($config);

// 调用日志类，使用默认设定
$logger = Log::getLogger();
$logger->info('Test Add Info Log');
$logger->warn('Test Add Warn Log');
$logger->error('Test Add Error Log');

// 调用日志类，使用user设定
$logger1 = Log::getLogger('user');
$logger1->info('Test Add User Info Log');
$logger1->warn('Test Add User Warn Log');
$logger1->error('Test Add User Error Log');

// 调用日志类，使用order设定
$logger2 = Log::getLogger('order');
$logger2->info('Test Add Order Info Log');
$logger2->warn('Test Add Order Warn Log');
$logger2->error('Test Add Order Error Log');

// 调用日志类，设定类型不存在，使用默认设定
$logger3 = Log::getLogger('notexists');
$logger3->info('Test Add Not Exists Info Log');
$logger3->warn('Test Add Not Exists Warn Log');
$logger3->error('Test Add Not Exists Error Log');
```

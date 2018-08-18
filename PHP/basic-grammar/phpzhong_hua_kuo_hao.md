# php中花括号

http://www.cnblogs.com/xccjmpc/archive/2013/08/30/3292253.html

##1.简单句法规则（用花括号界定变量名）
```
    $a = 'flower';
    echo "She received some $as";
    // 无效；字母s会被当成有效的变量名组成元素，但是这里的变量是$a
    echo "She received some ${a}s"; // 有效
    echo "She received some {$a}s"; // 有效；推荐的使用方法
```
  

```
    echo "She received some $a"."s";
    echo "She received some ".$a."s";
    // 这两种习惯性的写法应该没有加花括号的写法简洁明了吧？
    
    echo "She received some { $a}s";
    // 输出的结果为：She received some { flower}s
 ```
注意：不管{是出现在$前面还是后面，只有两者紧挨着时花括号才会被当成是界定符号。不要在之间加空格，要不然就会被当作普通的花括号处理
##2.复杂句法规则（用花括号界定表达式等，PHP4+）
   ```
   echo "有效的写法： {$arr[4][3]}";
    // 有效；界定多维数组
    echo "有效的写法： {$arr['foo'][3]}";
    // 有效；当在字符串中使用多维数组时，一定要用括号将它括起来
    echo "有效的写法： {$this->width}00";
    // 有效；如果不界定的话，就会变成 $this->width00
    echo "有效的写法： {$this->value[3]->name}";
    // 有效；该例演示了界定链式调用
    echo "有效的写法： $name: {${$name}}";
    // 有效；该例演示的效果实际上是一个可变变量
    echo "有效的写法: {${getName()}}";
    // 有效；该例演示了将函数的返回值作为变量名
    echo "有效的下发： {${$this->getName()}}";
    // 有效；该例演示了将函数的返回值作为变量名
    ```
    
注意1：echo "这样写有效吗： {getName()}";输出结果为：'这样写有效吗：
{getName()}'。因为里面不含$，所以花括号不会被当作界定符

注意2：echo "这样写有效吗：{$arr[foo][3]}"; 在回答这个问题前我们先来进行一个实验：
 ```   
    error_reporting(E_ALL);
    $arr = array('a', 'b', 'c', 'd'=>'e');
    echo "This is $arr[d]";
    // 我们发现这样写是没有问题的，那么我们像下面这样写呢？
    echo $arr[d];
    产生了这样的错误：
    Notice: Use of undefined constant d - assumed 'd'
    注意：采用了未定义的常量d，可能应该为'd'
    那么如果我们像下面这样修改一下代码的话
    error_reporting(E_ALL);
    $arr = array('a', 'b', 'c', 'd'=>'e');
    define('f', 'd');
    echo $arr[f];
```

我 们发现这次没有问题了。可以看出在字符串中数组的索引不加单引号是没有问题的，但是如果这种写法不是出现在字符串当中就会报错，而对于字符串中 {$arr[foo][3]}的解析就是按照非字符串的方式解析的。所以说在字符串当中对数组只加花括号界定而不对索引加单引号的写法是错误的。因为程序 会把不加单引号的索引当作是常量来进行解析，这就产生了错误。正确的写法应该是：

  ` echo "有效的写法： {$arr['foo'][3]}";`
  
  特别提醒一点：echo "This is $arr[d]";这种写法虽然能够被程序解析，但这也仅限于数组是一维数组的情况。严谨的写法应该是：echo "This is {$arr['d']}";我的学生曾经在这一点上和我争论过，他说：既然前面一种写法能出结果，为什么一定要用后面一种写法呢？那么，我们再继续修改一 下前面的代码
  
    error_reporting(E_ALL);
    $arr = array('a', 'b', 'c',
    'd'=>array('e'=>'f')
    );
    echo "This is $arr[d][e]";
    这样还能够被正确解析吗？我只想告诉你，加花括号是严谨的必要的。
    
    注意3：
    error_reporting(E_ALL);
    $arr = array('a', 'b', 'c', 'd');
    echo "This is {$arr[2]} 
    ";
    echo "This is {$arr['2']} 
    ";
    执行上面的代码。结果是一样的，为什么会这样呢？我只能告诉你PHP是弱类型语言，至于什么叫弱类型语言我就不在这里多说了。自己去Google一下吧。说了这么多，那么最能体现这些句法规则优势的具体应用在什么地方呢？----SQL语句
    // 示例一：
    $SQL1 = "select * from table where id={$_GET['id']}";
    // 示例二：
    $SQL2 = "select * from table where id={$this->id}";
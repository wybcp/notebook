这篇文章不会详细叙述某个ini配置项的用途，这些在手册上已经讲解的面面俱到。我只是想从某个特定的角度去挖掘php的实现机制，会涉及到一些php内核方面的知识:-)

使用php的同学都知道php.ini配置的生效会贯穿整个SAPI的生命周期。在一段php脚本的执行过程中，如果手动修改ini配置，是不会启作用的。此时如果无法重启apache或者nginx等，那么就只能显式的在php代码中调用ini_set接口。ini_set是php向我们提供的一个动态修改配置的函数，需要注意的是，利用ini_set所设置的配置与ini文件中设置的配置，其生效的时间范围并不相同。在php脚本执行结束之后，ini_set的设置便会随即失效。

因此本文打算分两篇，第一篇阐述php.ini配置原理，第二篇讲动态修改php配置。

php.ini的配置大致会涉及到三块数据，configuration_hash，EG(ini_directives)以及PG、BG、PCRE_G、JSON_G、XXX_G等。如果不清楚这三种数据的含义也没有关系，下文会详细解释。

# 解析INI配置文件

由于php.ini需要在SAPI过程中一直生效，那么解析ini文件并据此来构建php配置的工作，必定是发生SAPI的一开始。换句话说，也就是必定发生在php的启动过程中。php需要任意一个实际的请求到达之前，其内部已经生成好这些配置。

反映到php的内核，即为php_module_startup函数。

php_module_startup主要负责对php进行启动，通常它会在SAPI开始的时候被调用。btw，还有一个常见的函数是php_request_startup，它负责将在每个请求到来的时刻进行初始化，php_module_startup与php_request_startup是两个标识性的动作，不过对他们进行分析并不在本文的探讨范围内。

举个例子，当php挂接在apache下面做一个module，那么apache启动的时候，便会激活所有这些module，其中包括php module。在激活php module时，便会调用到php_module_startup。php_module_startup函数完成了茫茫多的工作，一旦php_module_startup调用结束就意味着，OK，php已经启动，现在可以接受请求并作出响应了。

在php_module_startup函数中，与解析ini文件相关的实现是：

```
/* this will read in php.ini, set up the configuration parameters,
   load zend extensions and register php function extensions
   to be loaded later */
if (php_init_config(TSRMLS_C) == FAILURE) {
    return FAILURE;
}
```

可以看到，其实就是调用了php_init_config函数，去完成对ini文件的parse。parse工作主要进行lex&grammar分析，并将ini文件中的key、value键值对提取出来并保存。php.ini的格式很简单，等号左侧为key，右侧为value。每当一对kv被提取出来之后，php将它们存储到哪儿呢？答案就是之前提到的configuration_hash。

```
static HashTable configuration_hash;
```

configuration_hash声明在php_ini.c中，它是一个HashTable类型的数据结构。顾名思义，其实就是张hash表。题外话，在php5.3之前的版本是没法获取configuration_hash的，因为它是php_ini.c文件的一个static的变量。后来php5.3添加了php_ini_get_configuration_hash接口，该接口直接返回&configuration_hash，使 得php各个扩展可以方便的一窥configuration_hash全貌...真是普大喜奔...

注意四点：

第一，php_init_config不会做除了词法语法以外的任何校验。也就是说，假如我们在ini文件中添加一行 hello=world，只要这是一个格式正确的配置项，那么最终configuration_hash中就会包含一个键为hello、值为world的元素，configuration_hash最大限度的反映出ini文件。

第二，ini文件允许我们以数组的形式进行配置。例如ini文件中写入以下三行：

```
drift.arr[]=1
drift.arr[]=2
drift.arr[]=3
```

那么最终生成的configuration_hash表中，就会存在一个key为drift.arr的元素，其value为一个包含的1,2,3三个数字的数组。这是一种极为罕见的配置方法。

第三，php还允许我们除了默认的php.ini文件（准确说是php-%s.ini）之外，另外构建一些ini文件。这些ini文件会被放入一个额外的目录。该目录由环境变量PHP_INI_SCAN_DIR来指定，当php_init_config解析完了php.ini之后，会再次扫描此目录，然后找出目录中所有.ini文件来分析。这些额外的ini文件中产生的kv键值对，也会被加入到configuration_hash中去。

这是一个偶尔有用的特性，假设我们自己开发php的扩展，却又不想将配置混入php.ini，便可以另外写一份ini，并通过PHP_INI_SCAN_DIR告诉php该去哪儿找到它。当然，其缺点也显而易见，其需要设置额外的环境变量来支持。更好的解决办法是，开发者在扩展中自己调用php_parse_user_ini_file或zend_parse_ini_file去解析对应的ini文件。

第四，在configuration_hash中，key是字符串，那么值的类型是什么？答案也是字符串（除了上述很特殊的数组）。具体来说，比如下面的配置：

```
display_errors = On
log_errors = Off
log_errors_max_len = 1024
```

 那么最后configuration_hash中实际存放的键值对为：

```
key: "display_errors"
val : "1"

key: "log_errors"
val : ""

key: "log_errors_max_len"
val : "1024"
```

注意log_errors，其存放的值连"0"都不是，就是一个实实在在地空字符串。另外，log_errors_max_len也并非数字，而是字符串1024。

分析至此，基本上解析ini文件相关的内容都说清楚了。简单总结一下：

1，解析ini发生在php_module_startup阶段

2，解析结果存放在configuration_hash里。

# 配置作用到模块

php的大致结构可以看成是最下层有一个zend引擎，它负责与OS进行交互、编译php代码、提供内存托管等等，在zend引擎的上层，排列着很多很多的模块。其中最核心的就一个Core模块，其他还有比如Standard，PCRE，Date，Session等等...这些模块还有另一个名字叫php扩展。我们可以简单理解为，每个模块都会提供一组功能接口给开发者来调用，举例来说，常用的诸如explode，trim，array等内置函数，便是由Standard模块提供的。

为什么需要谈到这些，是因为在php.ini里除了针对php自身，也就是针对Core模块的一些配置（例如safe_mode，display_errors，max_execution_time等），还有相当多的配置是针对其他不同模块的。

例如，date模块，它提供了常见的date， time，strtotime等函数。在php.ini中，它的相关配置形如：

```
[Date]
;date.timezone = 'Asia/Shanghai'
;date.default_latitude = 31.7667
;date.default_longitude = 35.2333
;date.sunrise_zenith = 90.583333
;date.sunset_zenith = 90.583333
```

除了这些模块拥有独立的配置，zend引擎也是可配的，只不过zend引擎的可配项非常少，只有error_reporting，zend.enable_gc和detect_unicode三项。

在上一小节中我们已经谈到，php_module_startup会调用php_init_config，其目的是解析ini文件并生成configuration_hash。那么接下来在php_module_startup中还会做什么事情呢？很显然，就是会将configuration_hash中的配置作用于Zend，Core，Standard，SPL等不同模块。当然这并非一个一蹴而就的过程，因为php通常会包含有很多模块，php启动的过程中这些模块也会依次进行启动。那么，对模块A进行配置的过程，便是发生在模块A的启动过程中。

有扩展开发经验的同学会直接指出，模块A的启动不就是在PHP_MINIT_FUNCTION(A)中么？

是的，如果模块A需要配置，那么在PHP_MINIT_FUNCTION中，可以调用REGISTER_INI_ENTRIES()来完成。REGISTER_INI_ENTRIES会根据当前模块所需要的配置项名称，去configuration_hash查找用户设置的配置值，并更新到模块自己的全局空间中。

## 模块的全局空间

要理解如何将ini配置从configuration_hash作用到各个模块之前，有必要先了解一下php模块的全局空间。对于不同的php模块，均可以开辟一块属于自己的存储空间，并且这块空间对于该模块来说，是全局可见的。一般而言，它会被用来存放该模块所需的ini配置。也就是说，configuration_hash中的配置项，最终会被存放到该全局空间中。在模块的执行过程中，只需要直接访问这块全局空间，就可以拿到用户针对该模块进行的设置。当然，它也经常被用来记录模块在执行过程中的中间数据。

我们以bcmath模块来举例说明，bcmath是一个提供数学计算方面接口的php模块，首先我们来看看它有哪些ini配置：

```
PHP_INI_BEGIN()
    STD_PHP_INI_ENTRY("bcmath.scale", "0", PHP_INI_ALL, OnUpdateLongGEZero, bc_precision, zend_bcmath_globals, bcmath_globals)
PHP_INI_END()
```

bcmath只有一个配置项，我们可以在php.ini中用bcmath.scale来配置bcmath模块。

接下来继续看看bcmatch模块的全局空间定义。在php_bcmath.h中有如下声明：

```
ZEND_BEGIN_MODULE_GLOBALS(bcmath)
    bc_num _zero_;
    bc_num _one_;
    bc_num _two_;
    long bc_precision;
ZEND_END_MODULE_GLOBALS(bcmath)
```

 宏展开之后，即为：

typedef struct _zend_bcmath_globals {
    bc_num _zero_;
    bc_num _one_;
    bc_num _two_;
    long bc_precision;
} zend_bcmath_globals;

其实，zend_bcmath_globals类型就是bcmath模块中的全局空间类型。这里仅仅声明了zend_bcmath_globals结构体，在bcmath.c中还有具体的实例化定义：

```
// 展开后即为zend_bcmath_globals bcmath_globals;
ZEND_DECLARE_MODULE_GLOBALS(bcmath) 
```

可以看出，用ZEND_DECLARE_MODULE_GLOBALS完成了对变量bcmath_globals的定义。

bcmath_globals是一块真正的全局空间，它包含有四个字段。其最后一个字段bc_precision，对应于ini配置中的bcmath.scale。我们在php.ini中设置了bcmath.scale的值，随后在启动bcmath模块的时候，bcmath.scale的值被更新到bcmath_globals.bc_precision中去。

把configuration_hash中的值，更新到各个模块自己定义的xxx_globals变量中，就是所谓的将ini配置作用到模块。一旦模块启动完成，那么这些配置也都作用到位。所以**在随后的执行阶段，php模块无需再次访问configuration_hash，模块仅需要访问自己的XXX_globals，就可以拿到用户设定的配置。**

bcmath_globals，除了有一个字段为ini配置项，其他还有三个字段为何意？这就是模块全局空间的第二个作用，它除了用于ini配置，还可以存储模块执行过程中的一些数据。

![img](https://images.cnblogs.com/cnblogs_com/driftcloudy/491509/o_20141012.PNG)

再例如json模块，也是php中一个很常用的模块：

```
ZEND_BEGIN_MODULE_GLOBALS(json)
    int error_code;
ZEND_END_MODULE_GLOBALS(json)
```

可以看到json模块并不需要ini配置，它的全局空间只有一个字段error_code。error_code记录了上一次执行json_decode或者json_encode中发生的错误。json_last_error函数便是返回这个error_code，来帮助用户定位错误原因。

为了能够很便捷的访问模块全局空间变量，php约定俗成的提出了一些宏。比如我们想访问json_globals中的error_code，当然可以直接写做json_globals.error_code（多线程环境下不行），不过更通用的写法是定义JSON_G宏：

```
#define JSON_G(v) (json_globals.v)
```

我们使用JSON_G(error_code)来访问json_globals.error_code。本文刚开始的时候，曾提到PG、BG、JSON_G、PCRE_G，XXX_G等等，这些宏在php源代码中也是很常见的。现在我们可以很轻松的理解它们，PG宏可以访问Core模块的全局变量，BG访问Standard模块的全局变量，PCRE_G则访问PCRE模块的全局变量。

```
#define PG(v) (core_globals.v)
#define BG(v) (basic_globals.v)
```

## 如何确定一个模块需要哪些配置呢？

模块需要什么样的INI配置，都是在各个模块中自己定义的。举例来说，对于Core模块，有如下的配置项定义：

```
PHP_INI_BEGIN()
    ......
    STD_PHP_INI_ENTRY_EX("display_errors", "1", PHP_INI_ALL,    OnUpdateDisplayErrors, display_errors, php_core_globals, core_globals, display_errors_mode)
    STD_PHP_INI_BOOLEAN("enable_dl",       "1", PHP_INI_SYSTEM, OnUpdateBool,          enable_dl,      php_core_globals, core_globals)
    STD_PHP_INI_BOOLEAN("expose_php",      "1", PHP_INI_SYSTEM, OnUpdateBool,          expose_php,     php_core_globals, core_globals)
    STD_PHP_INI_BOOLEAN("safe_mode",       "0", PHP_INI_SYSTEM, OnUpdateBool,          safe_mode,      php_core_globals, core_globals)
    ......
PHP_INI_END()
```

可以在php-src\main\main.c文件大概450+行找到上述代码。其中涉及的宏比较多，有ZEND_INI_BEGIN 、ZEND_INI_END、PHP_INI_ENTRY_EX、STD_PHP_INI_BOOLEAN等等，本文不一一赘述，感兴趣的读者可自行分析。

上述代码进行宏展开后得到：

```
static const zend_ini_entry ini_entries[] = {
    ..
    { 0, PHP_INI_ALL,    "display_errors",sizeof("display_errors"),OnUpdateDisplayErrors,(void *)XtOffsetOf(php_core_globals, display_errors), (void *)&core_globals, NULL, "1", sizeof("1")-1, NULL, 0, 0, 0, display_errors_mode },
    { 0, PHP_INI_SYSTEM, "enable_dl",     sizeof("enable_dl"),     OnUpdateBool,         (void *)XtOffsetOf(php_core_globals, enable_dl),      (void *)&core_globals, NULL, "1", sizeof("1")-1, NULL, 0, 0, 0, zend_ini_boolean_displayer_cb },
    { 0, PHP_INI_SYSTEM, "expose_php",    sizeof("expose_php"),    OnUpdateBool,         (void *)XtOffsetOf(php_core_globals, expose_php),     (void *)&core_globals, NULL, "1", sizeof("1")-1, NULL, 0, 0, 0, zend_ini_boolean_displayer_cb },
    { 0, PHP_INI_SYSTEM, "safe_mode",     sizeof("safe_mode"),     OnUpdateBool,         (void *)XtOffsetOf(php_core_globals, safe_mode),      (void *)&core_globals, NULL, "0", sizeof("0")-1, NULL, 0, 0, 0, zend_ini_boolean_displayer_cb },
    ...
    { 0, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, 0, 0, 0, NULL }
};
```

我们看到，配置项的定义，其本质上就是定义了一个zend_ini_entry类型的数组。zend_ini_entry结构体的字段具体含义为：

```
struct _zend_ini_entry {
    int module_number;                // 模块的id
    int modifiable;                   // 可被修改的范围，例如php.ini，ini_set
    char *name;                       // 配置项的名称
    uint name_length;
    ZEND_INI_MH((*on_modify));        // 回调函数，配置项注册或修改的时候会调用
    void *mh_arg1;                    // 通常为配置项字段在XXX_G中的偏移量
    void *mh_arg2;                    // 通常为XXX_G
    void *mh_arg3;                    // 通常为保留字段，极少用到

    char *value;                      // 配置项的值
    uint value_length;

    char *orig_value;                 // 配置项的原始值
    uint orig_value_length;
    int orig_modifiable;              // 配置项的原始modifiable
    int modified;                     // 是否发生过修改，如果有修改，则orig_value会保存修改前的值

    void (*displayer)(zend_ini_entry *ini_entry, int type);
};
```

## 将配置作用到模块——REGISTER_INI_ENTRIES

经常能够在不同扩展的PHP_MINIT_FUNCTION里看到REGISTER_INI_ENTRIES。REGISTER_INI_ENTRIES主要负责完成两件事情，第一，对模块的全局空间XXX_G进行填充，同步configuration_hash中的值到XXX_G中去。其次，它还生成了EG(ini_directives)。

REGISTER_INI_ENTRIES也是一个宏，展开之后实则为zend_register_ini_entries方法。具体来看下zend_register_ini_entries的实现：

```
ZEND_API int zend_register_ini_entries(const zend_ini_entry *ini_entry, int module_number TSRMLS_DC) /* {{{ */
{
    // ini_entry为zend_ini_entry类型数组，p为数组中每一项的指针
    const zend_ini_entry *p = ini_entry;
    zend_ini_entry *hashed_ini_entry;
    zval default_value;
    
    // EG(ini_directives)就是registered_zend_ini_directives
    HashTable *directives = registered_zend_ini_directives;
    zend_bool config_directive_success = 0;
    
    // 还记得ini_entry最后一项固定为{ 0, 0, NULL, ... }么
    while (p->name) {
        config_directive_success = 0;
        
        // 将p指向的zend_ini_entry加入EG(ini_directives)
        if (zend_hash_add(directives, p->name, p->name_length, (void*)p, sizeof(zend_ini_entry), (void **) &hashed_ini_entry) == FAILURE) {
            zend_unregister_ini_entries(module_number TSRMLS_CC);
            return FAILURE;
        }
        hashed_ini_entry->module_number = module_number;
        
        // 根据name去configuration_hash中查询，取出来的结果放在default_value中
        // 注意default_value的值比较原始，一般是数字、字符串、数组等，具体取决于php.ini中的写法
        if ((zend_get_configuration_directive(p->name, p->name_length, &default_value)) == SUCCESS) {
            // 调用on_modify更新到模块的全局空间XXX_G中
            if (!hashed_ini_entry->on_modify || hashed_ini_entry->on_modify(hashed_ini_entry, Z_STRVAL(default_value), Z_STRLEN(default_value), hashed_ini_entry->mh_arg1, hashed_ini_entry->mh_arg2, hashed_ini_entry->mh_arg3, ZEND_INI_STAGE_STARTUP TSRMLS_CC) == SUCCESS) {
                hashed_ini_entry->value = Z_STRVAL(default_value);
                hashed_ini_entry->value_length = Z_STRLEN(default_value);
                config_directive_success = 1;
            }
        }

        // 如果configuration_hash中没有找到，则采用默认值
        if (!config_directive_success && hashed_ini_entry->on_modify) {
            hashed_ini_entry->on_modify(hashed_ini_entry, hashed_ini_entry->value, hashed_ini_entry->value_length, hashed_ini_entry->mh_arg1, hashed_ini_entry->mh_arg2, hashed_ini_entry->mh_arg3, ZEND_INI_STAGE_STARTUP TSRMLS_CC);
        }
        p++;
    }
    return SUCCESS;
}
```

简单来说，可以把上述代码的逻辑表述为：

1，将模块声明的ini配置项添加到EG(ini_directives)中。注意，ini配置项的值可能在随后被修改。

2，尝试去configuration_hash中寻找各个模块需要的ini。

- 如果能够找到，说明用户叜ini文件中配置了该值，那么采用用户的配置。
- 如果没有找到，OK，没有关系，因为模块在声明ini的时候，会带上默认值。

3，将ini的值同步到XX_G里面。毕竟在php的执行过程中，起作用的还是这些XXX_globals。具体的过程是调用每条ini配置对应的on_modify方法完成，on_modify由模块在声明ini的时候进行指定。

我们来具体看下on_modify，它其实是一个函数指针，来看两个具体的Core模块的配置声明：

```
STD_PHP_INI_BOOLEAN("log_errors",      "0",    PHP_INI_ALL, OnUpdateBool, log_errors,         php_core_globals, core_globals)
STD_PHP_INI_ENTRY("log_errors_max_len","1024", PHP_INI_ALL, OnUpdateLong, log_errors_max_len, php_core_globals, core_globals)
```

对于log_errors，它的on_modify被设置为OnUpdateBool，对于log_errors_max_len，则on_modify被设置为OnUpdateLong。

进一步假设我们在php.ini中的配置为：

```
log_errors = On
log_errors_max_len = 1024
```

具体来看下OnUpdateBool函数：

```
ZEND_API ZEND_INI_MH(OnUpdateBool) 
{
    zend_bool *p;
    
    // base表示core_globals的地址
    char *base = (char *) mh_arg2;

    // p表示core_globals的地址加上log_errors字段的偏移量
    // 得到的即为log_errors字段的地址
    p = (zend_bool *) (base+(size_t) mh_arg1);  

    if (new_value_length == 2 && strcasecmp("on", new_value) == 0) {
        *p = (zend_bool) 1;
    }
    else if (new_value_length == 3 && strcasecmp("yes", new_value) == 0) {
        *p = (zend_bool) 1;
    }
    else if (new_value_length == 4 && strcasecmp("true", new_value) == 0) {
        *p = (zend_bool) 1;
    }
    else {
        // configuration_hash中存放的value是字符串"1"，而非"On"
        // 因此这里用atoi转化成数字1
        *p = (zend_bool) atoi(new_value);
    }
    return SUCCESS;
}
```

最令人费解的估计就是mh_arg1和mh_arg2了，其实对照前面所述的zend_ini_entry定义，mh_arg1，mh_arg2还是很容易参透的。mh_arg1表示字节偏移量，mh_arg2表示XXX_globals的地址。因此，(char *)mh_arg2 + mh_arg1的结果即为XXX_globals中某个字段的地址。具体到本case中，就是计算core_globals中log_errors的地址。因此，当OnUpdateBool最后执行到

*p = (zend_bool) atoi(new_value);

其作用就相当于

core_globals.log_errors = (zend_bool) atoi("1");

分析完了OnUpdateBool，我们再来看OnUpdateLong便觉得一目了然：

```
ZEND_API ZEND_INI_MH(OnUpdateLong)
{
    long *p;
    char *base = (char *) mh_arg2;

    // 获得log_errors_max_len的地址
    p = (long *) (base+(size_t) mh_arg1);

    // 将"1024"转化成long型，并赋值给core_globals.log_errors_max_len
    *p = zend_atol(new_value, new_value_length);
    return SUCCESS;
}
```

最后需要注意的是，zend_register_ini_entries函数中，如果configuration_hash中存在配置，则当调用on_modify结束后，hashed_ini_entry中的value和value_length会被更新。也就是说，如果用户在php.ini中配置过，则EG(ini_directives)存放的就是实际配置的值。如果用户没配，EG(ini_directives)中存放的是声明zend_ini_entry时给出的默认值。

zend_register_ini_entries中的default_value变量命名比较糟糕，相当容易造成误解。其实default_value并非表示默认值，而是表示用户实际配置的值。

# 总结

至此，三块数据configuration_hash，EG(ini_directives)以及PG、BG、PCRE_G、JSON_G、XXX_G...已经都交代清楚了。

总结一下：

1，configuration_hash，存放php.ini文件里的配置，不做校验，其值为字符串。
2，EG(ini_directives)，存放的是各个模块中定义的zend_ini_entry，如果用户在php.ini配置过（configuration_hash中存在），则值被替换为configuration_hash中的值，类型依然是字符串。
3，XXX_G，该宏用于访问模块的全局空间，这块内存空间可用来存放ini配置，并通过on_modify指定的函数进行更新，其数据类型由XXX_G中的字段声明来决定。



# 运行时改变配置

在前一篇中曾经谈到，ini_set函数可以在php执行的过程中，动态修改php的部分配置。注意，仅仅是部分，并非所有的配置都可以动态修改。关于ini配置的可修改性，参见：<http://php.net/manual/zh/configuration.changes.modes.php>

我们直接进入ini_set的实现，函数虽然有点长，但是逻辑很清晰：

```
PHP_FUNCTION(ini_set)
{
    char *varname, *new_value;
    int varname_len, new_value_len;
    char *old_value;

    if (zend_parse_parameters(ZEND_NUM_ARGS() TSRMLS_CC, "ss", &varname, &varname_len, &new_value, &new_value_len) == FAILURE) {
        return;
    }

    // 去EG(ini_directives)中获取配置的值
    old_value = zend_ini_string(varname, varname_len + 1, 0);

    /* copy to return here, because alter might free it! */
    if (old_value) {
        RETVAL_STRING(old_value, 1);
    } else {
        RETVAL_FALSE;
    }

    // 如果开启了安全模式，那么如下这些ini配置可能涉及文件操作，需要要辅助检查uid
#define _CHECK_PATH(var, var_len, ini) php_ini_check_path(var, var_len, ini, sizeof(ini))
    /* safe_mode & basedir check */
    if (PG(safe_mode) || PG(open_basedir)) {
        if (_CHECK_PATH(varname, varname_len, "error_log") ||
            _CHECK_PATH(varname, varname_len, "java.class.path") ||
            _CHECK_PATH(varname, varname_len, "java.home") ||
            _CHECK_PATH(varname, varname_len, "mail.log") ||
            _CHECK_PATH(varname, varname_len, "java.library.path") ||
            _CHECK_PATH(varname, varname_len, "vpopmail.directory")) {
            if (PG(safe_mode) && (!php_checkuid(new_value, NULL, CHECKUID_CHECK_FILE_AND_DIR))) {
                zval_dtor(return_value);
                RETURN_FALSE;
            }
            if (php_check_open_basedir(new_value TSRMLS_CC)) {
                zval_dtor(return_value);
                RETURN_FALSE;
            }
        }
    }

    // 在安全模式下，如下这些ini受到保护，不会被动态修改
    if (PG(safe_mode)) {
        if (!strncmp("max_execution_time", varname, sizeof("max_execution_time")) ||
            !strncmp("memory_limit", varname, sizeof("memory_limit")) ||
            !strncmp("child_terminate", varname, sizeof("child_terminate"))
        ) {
            zval_dtor(return_value);
            RETURN_FALSE;
        }
    }

    // 调用zend_alter_ini_entry_ex去动态修改ini配置
    if (zend_alter_ini_entry_ex(varname, varname_len + 1, new_value, new_value_len, PHP_INI_USER, PHP_INI_STAGE_RUNTIME, 0 TSRMLS_CC) == FAILURE) {
        zval_dtor(return_value);
        RETURN_FALSE;
    }
}
```

可以看到，除了一些必要的验证工作，主要就是调用zend_alter_ini_entry_ex。

我们继续跟进到zend_alter_ini_entry_ex函数中：

```
ZEND_API int zend_alter_ini_entry_ex(char *name, uint name_length, char *new_value, uint new_value_length, int modify_type, int stage, int force_change TSRMLS_DC) /* {{{ */
{
    zend_ini_entry *ini_entry;
    char *duplicate;
    zend_bool modifiable;
    zend_bool modified;

    // 找出EG(ini_directives)中对应的ini_entry
    if (zend_hash_find(EG(ini_directives), name, name_length, (void **) &ini_entry) == FAILURE) {
        return FAILURE;
    }

    // 是否被修改以及可修改性
    modifiable = ini_entry->modifiable;
    modified = ini_entry->modified;

    if (stage == ZEND_INI_STAGE_ACTIVATE && modify_type == ZEND_INI_SYSTEM) {
        ini_entry->modifiable = ZEND_INI_SYSTEM;
    }

    // 是否强制修改
    if (!force_change) {
        if (!(ini_entry->modifiable & modify_type)) {
            return FAILURE;
        }
    }

    // EG(modified_ini_directives)用于存放被修改过的ini_entry
    // 主要用做恢复
    if (!EG(modified_ini_directives)) {
        ALLOC_HASHTABLE(EG(modified_ini_directives));
        zend_hash_init(EG(modified_ini_directives), 8, NULL, NULL, 0);
    }
    
    // 将ini_entry中的值，值的长度，可修改范围，保留到orig_xxx中去
    // 以便在请求结束的时候，可以对ini_entry做恢复
    if (!modified) {
        ini_entry->orig_value = ini_entry->value;
        ini_entry->orig_value_length = ini_entry->value_length;
        ini_entry->orig_modifiable = modifiable;
        ini_entry->modified = 1;
        zend_hash_add(EG(modified_ini_directives), name, name_length, &ini_entry, sizeof(zend_ini_entry*), NULL);
    }

    duplicate = estrndup(new_value, new_value_length);

    // 调用modify来更新XXX_G中对应的ini配置
    if (!ini_entry->on_modify || ini_entry->on_modify(ini_entry, duplicate, new_value_length, ini_entry->mh_arg1, ini_entry->mh_arg2, ini_entry->mh_arg3, stage TSRMLS_CC) == SUCCESS) {
        // 同上面，如果多次修改，则需要释放前一次修改的值
        if (modified && ini_entry->orig_value != ini_entry->value) {
            efree(ini_entry->value);
        }
        ini_entry->value = duplicate;
        ini_entry->value_length = new_value_length;
    } else {
        efree(duplicate);
        return FAILURE;
    }

    return SUCCESS;
}
```

有3处逻辑需要我们仔细体会：

1）ini_entry中的modified字段用来表示该配置是否被动态修改过。一旦该ini配置发生修改，modified就会被置为1。上述代码中有一段很关键：

```
// 如果多次调用ini_set，则orig_value等始终保持最原始的值
if (!modified) {
    ini_entry->orig_value = ini_entry->value;
    ini_entry->orig_value_length = ini_entry->value_length;
    ini_entry->orig_modifiable = modifiable;
    ini_entry->modified = 1;
    zend_hash_add(EG(modified_ini_directives), name, name_length, &ini_entry, sizeof(zend_ini_entry*), NULL);
}
```

这段代码表示，不管我们先后在php代码中调用几次ini_set，只有第一次ini_set时才会进入这段逻辑，设置好orig_value。从第二次调用ini_set开始，便不会再次执行这段分支，因为此时的modified已经被置为1了。因此，ini_entry->orig_value始终保存的是第一次修改之前的配置值（即最原始的配置）。

2）为了能使ini_set修改的配置立即生效，需要on_modify回调函数。

如前一篇文中所述，调用on_modify是为了能够更新模块的全局变量。再次回忆下，首先，模块全局变量中的配置已经不是字符串类型了，该用bool用bool、该用int用int。其次，每一个ini_entry中都存储了该模块全局变量的地址以及对应的偏移量，使得on_modify可以很迅速的进行内存修改。此外不要忘记，on_modify调用完了之后，仍需进一步更新ini_entry->value，这样EG(ini_directives)中的配置值就是最新的了。

3）这里出现了一张新的hash表，EG(modified_ini_directives)。

EG(modified_ini_directives)只用于存放被动态修改过的ini配置，如果一个ini配置被动态修改过，那么它既存在于EG(ini_directives)中，又存在于EG(modified_ini_directives)中。既然每一个ini_entry都有modified字段做标记，那岂不是可以遍历EG(ini_directives)来获得所有被修改过的配置呢？

答案是肯定的。个人觉得，这里的EG(modified_ini_directives)主要还是为了提升性能，酱直接遍历EG(modified_ini_directives)就足够了。此外，把EG(modified_ini_directives)的初始化推迟到zend_alter_ini_entry_ex中，也可以看出php在细节上的性能优化点。

# 恢复配置

**ini_set的作用时间和php.ini文件的作用时间是不一样的，一旦请求执行结束，则ini_set会失效**。此外，当我们代码中调用了ini_restore函数，则之前通过ini_set设置的配置也会失效。

每一个php请求执行完毕之后，会触发php_request_shutdown，它和php_request_startup是两个相对应过程。如果php是挂接在apache/nginx下，则每处理完一个http请求，就会调用php_request_shutdown；如果php以CLI模式来运行，则脚本执行完毕之后，也会调用php_request_shutdown。

在php_request_shutdown中，我们可以看到针对ini的恢复处理：

```
/* 7. Shutdown scanner/executor/compiler and restore ini entries */
zend_deactivate(TSRMLS_C);
```

进入zend_deactivate，可以进一步看到调用了zend_ini_deactivate函数，由zend_ini_deactivate来负责将php的配置进行恢复。

```
zend_try {
    zend_ini_deactivate(TSRMLS_C);
} zend_end_try();
```

具体来看看zend_ini_deactivate的实现：

```
ZEND_API int zend_ini_deactivate(TSRMLS_D) /* {{{ */
{
    if (EG(modified_ini_directives)) {
        // 遍历EG(modified_ini_directives)中这张表
        // 对每一个ini_entry调用zend_restore_ini_entry_wrapper
        zend_hash_apply(EG(modified_ini_directives), (apply_func_t) zend_restore_ini_entry_wrapper TSRMLS_CC);
        
        // 回收操作
        zend_hash_destroy(EG(modified_ini_directives));
        FREE_HASHTABLE(EG(modified_ini_directives));
        EG(modified_ini_directives) = NULL;
    }
    return SUCCESS;
}
```

从zend_hash_apply来看，真正恢复ini的任务最终落地到了zend_restore_ini_entry_wrapper回调函数。

```
static int zend_restore_ini_entry_wrapper(zend_ini_entry **ini_entry TSRMLS_DC)
{
    // zend_restore_ini_entry_wrapper就是zend_restore_ini_entry_cb的封装
    zend_restore_ini_entry_cb(*ini_entry, ZEND_INI_STAGE_DEACTIVATE TSRMLS_CC);
    return 1;
}

static int zend_restore_ini_entry_cb(zend_ini_entry *ini_entry, int stage TSRMLS_DC)
{
    int result = FAILURE;

    // 只看修改过的ini项
    if (ini_entry->modified) {
        if (ini_entry->on_modify) {
            // 使用orig_value，对XXX_G内的相关字段进行重新设置
            zend_try {
                result = ini_entry->on_modify(ini_entry, ini_entry->orig_value, ini_entry->orig_value_length, ini_entry->mh_arg1, ini_entry->mh_arg2, ini_entry->mh_arg3, stage TSRMLS_CC);
            } zend_end_try();
        }
        if (stage == ZEND_INI_STAGE_RUNTIME && result == FAILURE) {
            /* runtime failure is OK */
            return 1;
        }
        if (ini_entry->value != ini_entry->orig_value) {
            efree(ini_entry->value);
        }
        
        // ini_entry本身恢复到最原始的值
        ini_entry->value = ini_entry->orig_value;
        ini_entry->value_length = ini_entry->orig_value_length;
        ini_entry->modifiable = ini_entry->orig_modifiable;
        ini_entry->modified = 0;
        ini_entry->orig_value = NULL;
        ini_entry->orig_value_length = 0;
        ini_entry->orig_modifiable = 0;
    }
    return 0;
}
```

逻辑都蛮清晰的，相信读者可以看明白。总结一下关于ini配置的恢复流程：

php_request_shutdown--->zend_deactivate--->zend_ini_deactivate--->zend_restore_ini_entry_wrapper--->zend_restore_ini_entry_cb

# 配置的销毁

在sapi生命周期结束的时候，比如apache关闭，cli程序执行完毕等等。一旦进入到这个阶段，之前所说的configuration_hash，EG(ini_directives)等都需要被销毁，其用到的内存空间需要被释放。

1，php会依次结束所有的模块，在每个模块的PHP_MSHUTDOWN_FUNCTION中调用UNREGISTER_INI_ENTRIES。UNREGISTER_INI_ENTRIES和REGISTER_INI_ENTRIES对应，但是UNREGISTER_INI_ENTRIES并不负责模块全局空间的释放，XXX_globals这块内存放在静态数据区上，无需人为回收。

UNREGISTER_INI_ENTRIES主要做的事情，是将某个模块的ini_entry配置从EG(ini_directives)表中删除。删除之后，ini_entry本身的空间会被回收，但是ini_entry->value不一定会被回收。

当所有模块的PHP_MSHUTDOWN_FUNCTION都调用UNREGISTER_INI_ENTRIES一遍之后，EG(ini_directives)中只剩下了Core模块的ini配置。此时，就需要手动调用UNREGISTER_INI_ENTRIES，来完成对Core模块配置的删除工作。

```
void php_module_shutdown(TSRMLS_D)
{
    ...
    
    // zend_shutdown会依次关闭除了Core之外的所有php模块
    // 关闭时会调用各个模块的PHP_MSHUTDOWN_FUNCTION
    zend_shutdown(TSRMLS_C);
    
    ...

    // 至此，EG(ini_directives)中只剩下了Core模块的配置
    // 这里手动清理一下
    UNREGISTER_INI_ENTRIES();
    
    // 回收configuration_hash
    php_shutdown_config();
```

```
    // 回收EG(ini_directives)
    zend_ini_shutdown(TSRMLS_C);

    ...
}
```

当手动调用UNREGISTER_INI_ENTRIES完成之后，EG(ini_directives)已经不包含任何的元素，理论上讲，此时的EG(ini_directives)是一张空的hash表。

2，configuration_hash的回收发生在EG(ini_directives)之后，上面贴出的代码中有关于php_shutdown_config的函数调用。php_shutdown_config主要负责回收configuration_hash。

```
int php_shutdown_config(void)
{
    // 回收configuration_hash
    zend_hash_destroy(&configuration_hash);
    
    ...
    
    return SUCCESS;
}
```

注意zend_hash_destroy并不会释放configuration_hash本身的空间，同XXX_G访问的模块全局空间一样，configuration_hash也是一个全局变量，无需手动回收。

3，当php_shutdown_config完成时，只剩下EG(ini_directives)的自身空间还没被释放。因此最后一步调用zend_ini_shutdown。zend_ini_shutdown用于释放EG(ini_directives)。在前文已经提到，此时的EG(ini_directives)理论上是一张空的hash表，因此该HashTable本身所占用的空间需要被释放。

```
ZEND_API int zend_ini_shutdown(TSRMLS_D)
{
    // EG(ini_directives)是动态分配出的空间，需要回收
    zend_hash_destroy(EG(ini_directives));
    free(EG(ini_directives));
    return SUCCESS;
}
```

# 总结

用一张图大致描述一下和ini配置相关的流程：

 

![img](https://images.cnblogs.com/cnblogs_com/driftcloudy/491509/o_2014101301.png)



http://www.cnblogs.com/driftcloudy/p/4011954.html

http://www.cnblogs.com/driftcloudy/p/4021079.html
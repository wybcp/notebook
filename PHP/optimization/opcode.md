# 深入理解 PHP opcode 优化

## 1.概述

PHP(本文所述案例 PHP 版本均为 7.1.3)作为一门动态脚本语言，其在 zend 虚拟机执行过程为：读入脚本程序字符串，经由词法分析器将其转换为单词符号，接着语法分析器从中发现语法结构后生成抽象语法树，再经静态编译器生成 opcode，最后经解释器模拟机器指令来执行每一条 opcode。

在上述整个环节中，生成的 opcode 可以应用编译优化技术如死代码删除、条件常量传播、函数内联等各种优化来精简 opcode，达到提高代码的执行性能的目的。

PHP 扩展 opcache，针对生成的 opcode 基于共享内存支持了缓存优化。在此基础上又加入了 opcode 的静态编译优化。

这里所述优化通常采用优化器（Optimizer）来管理，编译原理中，一般用优化遍(Opt pass)来描述每一个优化。

整体上说，优化遍分两种：

- 一种是分析 pass，是提供数据流、控制流分析信息为转换 pass 提供辅助信息；
- 一种是转换 pass，它会改变生成代码，包括增删指令、改变替换指令、调整指令顺序等，通常每一个 pass 前后可 dump 出生成代码的变化。

本文基于编译原理，结合 opcache 扩展提供的优化器，以 PHP 编译基本单位 op_array、PHP 执行最小单位 opcode 为出发点。介绍编译优化技术在 Zend 虚拟机中的应用，梳理各个优化遍是如何一步步优化 opcode 来提高代码执行性能的。最后结合 PHP 语言虚拟机执行给出几点展望。

## 2.几个概念说明

### 1）静态编译／解释执行／即时编译

静态编译（static compilation），也称事前编译（ahead-of-time compilation），简称 AOT。即把源代码编译成目标代码，执行时在支持目标代码的平台上运行。

动态编译（dynamic compilation），相对于静态编译而言，指”在运行时进行编译”。通常情况下采用解释器(interpreter)编译执行，它是指一条一条的解释执行源语言。

JIT 编译（just-in-time compilation），即即时编译，狭义指某段代码即将第一次被执行时进行编译，而后则不用编译直接执行，它为动态编译的一种特例。

上述三类不同编译执行流程，可大体如下图来描述：![alt](https://tech.youzan.com/content/images/2017/05/blog-comiler-2.jpg)

### 2）数据流／控制流

编译优化需要从程序中获取足够多的信息，这是所有编译优化的根基。

编译器前端产生的结果可以是语法树亦可以是某种低级中间代码。但无论结果什么形式，它对程序做什么、如何做仍然没有提供多少信息。编译器将发现每一个过程内控制流层次结构的任务留给控制流分析，将确定与数据处理有关的全局信息任务留给数据流分析。

- 控制流 是获取程序控制结构信息的形式化分析方法，它为数据流分析、依赖分析的基础。控制的一个基本模型是控制流图（Control Flow Graph,CFG）。单一过程的控制流分析有使用必经结点找循环、区间分析两种途径。
- 数据流 从程序代码中收集程序的语义信息，并通过代数的方法在编译时确定变量的定义和使用。数据的一个基本模型是数据流图（Data Flow Graph,DFG）。通常的数据流分析是基于控制树的分析（Control-tree-based data-flow analysis），算法分为区间分析与结构分析两种。

### 3）op_array

类似于 C 语言的栈帧（stack frame）概念，即一个运行程序的基本单位（一帧），一般为一次函数调用的基本单位。此处，一个函数或方法、整个 PHP 脚本文件、传给 eval 表示 PHP 代码的字符串都会被编译成一个 op_array。

实现上 op_array 为一个包含程序运行基本单位的所有信息的结构体，当然 opcode 数组为该结构最为重要的字段，不过除此之外还包含变量类型、注释信息、异常捕获信息、跳转信息等。

### 4）opcode

解释器执行(ZendVM)过程即是执行一个基本单位 op_array 内的最小优化 opcode，按顺序遍历执行，执行当前 opcode，会预取下一条 opcode，直到最后一个 RETRUN 这个特殊的 opcode 返回退出。

这里的 opcode 某种程度也类似于静态编译器里的中间表示(类似于 LLVM IR)，通常也采用三地址码的形式，即包含一个操作符，两个操作数及一个运算结果。其中两个操作数均包含类型信息。此处类型信息有五种，分别为：

- 编译变量（Compiled Variable，简称 CV），编译时变量即为 php 脚本中定义的变量。
- 内部可重用变量（VAR），供 ZendVM 使用的临时变量，可与其它 opcode 共用。
- 内部不可重用变量（TMP_VAR），供 ZendVM 使用的临时变量，不可与其它 opcode 共用。
- 常量（CONST），只读常量，值不可被更改。
- 无用变量(UNUSED)。由于 opcode 采用三地址码，不是每一个 opcode 均有操作数字段，缺省时用该变量补齐字段。

类型信息与操作符一起，供执行器匹配选择特定已编译好的 C 函数库模板，模拟生成机器指令来执行。

opcode 在 ZendVM 中以 zend_op 结构体来表征，其主体结构如下:
![alt](https://tech.youzan.com/content/images/2017/05/opcode-compiler2-1.jpeg)

## 3.opcache optimizer 优化器

PHP 脚本经过词法分析、语法分析生成抽象语法树结构后，再经静态编译生成 opcode。它作为向不同的虚拟机执行指令的公共平台，依赖不同的虚拟机具体实现(然对于 PHP 来说，大部分是指 ZendVM)。

在虚拟机执行 opcode 之前，如果对 opcode 进行优化可得到执行效率更高的代码，pass 的作用就是优化 opcode，它作用于 opcde、处理 opcode、分析 opcode、寻找优化的机会并修改 opcode 产生更高执行效率的代码。

### 1）ZendVM 优化器简介

在 Zend 虚拟机（ZendVM）中，opcache 的静态代码优化器即为 zend opcode optimization。

为观察优化效果及便于调试，它也提供了优化与调试选项：

- optimization*level （opcache.optimization*level=0xFFFFFFFF） 优化级别，缺省打开大部分优化遍，用户亦通过传入命令行参数控制关闭
- opt*debug*level （opcache.opt*debug*level=-1） 调试级别，缺省不打开，但提供了各优化前后 opcode 的变换过程

执行静态优化所需的脚本上下文信息则封装在结构 zend_script 中，如下：

```c
typedef struct _zend_script {
    zend_string   *filename;        //文件名
    zend_op_array  main_op_array;   //栈帧
    HashTable      function_table;  //函数单位符号表信息
    HashTable      class_table;     //类单位符号表信息
} zend_script;

```

上述三个内容信息即作为输入参数传递给优化器供其分析优化。当然与通常的 PHP 扩展类似，它与 opcode 缓存模块一起（zend_accel）构成了 opcache 扩展。其在缓存加速器内嵌入了三个内部 API：

- zend*optimizer*startup 启动优化器
- zend*optimize*script 优化器实现优化的主逻辑
- zend*optimizer*shutdown 优化器产生的资源清理

关于 opcode 缓存，也是 opcode 非常重要的优化。其基本应用原理是大体如下：

虽然 PHP 作为动态脚本语言，它并不会直接调用 GCC/LLVM 这样的整套编译器工具链，也不会调用 Javac 这样的纯前端编译器。但每次请求执行 PHP 脚本时，都经历过词法、语法、编译为 opcode、VM 执行的完整生命周期。

除去执行外的前三个步骤基本就是一个前端编译器的完整过程，然而这个编译过程并不会快。假如反复执行相同的脚本，前三个步骤编译耗时将严重制约运行效率，而每次编译生成的 opcode 则没有变化。因此可在第一次编译时把 opcode 缓存到某一个地方，opcache 扩展即是将其缓存到共享内存（Java 则是保存到文件中），下次执行相同脚本时直接从共享内存中获取 opcode，从而省去编译时间。

opcache 扩展的 opcode 缓存流程大致如下：
![alt](https://tech.youzan.com/content/images/2017/05/opcache.jpg)由于本文主要集中讨论静态优化遍，关于缓存优化的具体实现此处不展开。

### 2）ZendVM 优化器原理

依“鲸书”(《高级编译器设计与实现》)所述，一个优化编译器较为合理的优化遍顺序如下：![alt](https://tech.youzan.com/content/images/2017/05/pass-compiler-1.jpeg)
上图中涉及的优化从简单的常量、死代码到循环、分支跳转，从函数调用到过程间优化，从预取、缓存到软流水、寄存器分配，当然也包含数据流、控制流分析。

当然，当前 opcode 优化器并没有实现上述所有优化遍，而且也没有必要实现机器相关的低层中间表示优化如寄存器分配。

opcache 优化器接收到上述脚本参数信息后，找到最小编译单位。以此为基础，根据优化 pass 宏及其对应的优化级别宏，即可实现对某一个 pass 的注册控制。

注册的优化中，按一定顺序组织串联各优化，包含常量优化、冗余 nop 删除、函数调用优化的转换 pass，及数据流分析、控制流分析、调用关系分析等分析 pass。

zend*optimize*script 及实际的优化注册 zend_optimize 流程如下：

```c
zend_optimize_script(zend_script *script,
      zend_long optimization_level, zend_long debug_level)
    ｜zend_optimize_op_array(&script->main_op_array, &ctx);
        遍历二元操作符的常量操作数，由运行时转化为编译时(反向pass2)
        实际优化pass，zend_optimize
        遍历二元操作符的常量操作数，由编译时转化为运行时(pass2)
    ｜遍历op_array内函数zend_optimize_op_array(op_array, &ctx);
    ｜遍历类内非用户函数zend_optimize_op_array(op_array, &ctx);
       (用户函数设static_variables)
    ｜若使用DFA pass & 调用图pass & 构建调用图成功
         遍历二元操作符的常量操作数，由运行时转化为编译时(反向pass2)
         设置函数返回值信息，供SSA数据流分析使用
         遍历调用图的op_array，做DFA分析zend_dfa_analyze_op_array
         遍历调用图的op_array，做DFA优化zend_dfa_optimize_op_array
         若开调试，遍历dump调用图的每一个op_array(优化变换后)
         若开栈矫正优化，矫正栈大小adjust_fcall_stack_size_graph
         再次遍历调用图内的的所有op_array，
           针对DFA pass变换后新产生的常量场景，常量优化pass2再跑一遍
         调用图op_array资源清理
    ｜若开栈矫正优化
          矫正栈大小main_op_array
          遍历矫正栈大小op_array
    ｜清理资源

```

该部分主要调用了 SSA/DFA/CFG 这几类用于 opcode 分析 pass，涉及的 pass 有 BB 块、CFG、DFA(CFG、DOMINATORS、LIVENESS、PHI-NODE、SSA)。

用于 opcode 转换的 pass 则集中在函数 zend_optimize 内，如下：

```c
zend_optimize
｜op_array类型为ZEND_EVAL_CODE，不做优化
｜开debug，    可dump优化前内容
｜优化pass1，  常量替换、编译时常量操作变换、简单操作转换
｜优化pass2    常量操作转换、条件跳转指令优化
｜优化pass3    跳转指令优化、自增转换
｜优化pass4    函数调用优化(主要为函数调用优化)
｜优化pass5    控制流图（CFG）优化
 ｜构建流图
 ｜计算数据依赖
 ｜划分BB块(basic block，简称BB，数据流分析基本单位)
 ｜BB块内基于数据流分析优化
 ｜BB块间跳转优化
 ｜不可到达BB块删除
 ｜BB块合并
 ｜BB块外变量检查
 ｜重新构建优化后的op_array（基于CFG）
 ｜析构CFG
｜优化pass6/7  数据流分析优化
 ｜数据流分析（基于静态单赋值SSA）
  ｜构建SSA
  ｜构建CFG  需要找到对应BB块序号、管理BB块数组、计算BB块后继BB、标记可到达BB块、计算BB块前驱BB
  ｜计算Dominator树
  ｜标识循环是否可简化（主要依赖于循环回边）
  ｜基于phi节点构建完SSA  def集、phi节点位置、SSA构造重命名
  ｜计算use-def链
  ｜寻找不当依赖、后继、类型及值范围值推断
 ｜数据流优化  基于SSA信息，一系列BB块内opcode优化
 ｜析构SSA
｜优化pass9    临时变量优化
｜优化pass10   冗余nop指令删除
｜优化pass11   压缩常量表优化

```

还有其他一些优化遍如下：

    优化 pass12 矫正栈大小
    优化 pass15 收集常量信息
    优化 pass16 函数调用优化，主要是函数内联优化

除此之外，pass 8/13/14 可能为预留 pass id。由此可看出当前提供给用户选项控制的 opcode 转换 pass 有 13 个。但是这并不计入其依赖的数据流／控制流的分析 pass。

### 3）函数内联 pass 的实现

通常在函数调用过程中，由于需要进行不同栈帧间切换，因此会有开辟栈空间、保存返回地址、跳转、返回到调用函数、返回值、回收栈空间等一系列函数调用开销。因此对于函数体适当大小情况下，把整个函数体嵌入到调用者（Caller）内部，从而不实际调用被调用者（Callee）是一个提升性能的利器。

由于函数调用与目标机的应用二进制接口（ABI）强相关，静态编译器如 GCC/LLVM 的函数内联优化基本是在指令生成之前完成。

ZendVM 的内联则发生在 opcode 生成后的 FCALL 指令的替换优化，pass id 为 16，其原理大致如下：

```c
｜ 遍历op_array中的opcode,找到DO_XCALL四个opcode之一
｜ opcode ZEND_INIT_FCALL
｜ opcode ZEND_INIT_FCALL_BY_NAMEZ
     ｜ 新建opcode，操作码置为ZEND_INIT_FCALL，计算栈大小，
        更新缓存槽位，析构常量池字面量，替换当前opline的opcode
｜ opcode ZEND_INIT_NS_FCALL_BY_NAME
     ｜ 新建opcode，操作码置为ZEND_INIT_FCALL，计算栈大小，
        更新缓存槽位，析构常量池字面量，替换当前opline的opcode
｜ 尝试函数内联
     ｜ 优化条件过滤 （每个优化pass通常有较多限制条件，某些场景下
         由于缺乏足够信息不能优化或出于代价考虑而排除）
        ｜ 方法调用ZEND_INIT_METHOD_CALL，直接返回不内联
        ｜ 引用传参，直接返回不内联
        ｜ 缺省参数为命名常量，直接返回不内联
     ｜ 被调用函数有返回值，添加一条ZEND_QM_ASSIGN赋值opcode
     ｜ 被调用函数无返回值，插入一条ZEND_NOP空opcode
     ｜ 删除调用被内联函数的call opcode（即当前online的前一条opcode）
```

如下示例代码，当调用 fname()时，使用字符串变量名 fname 来动态调用函数 foo，而没有使用直接调用的方式。此时可通过 VLD 扩展查看其生成的 opcode，或打开 opcache 调试选项(opcache.opt*debug*level=0xFFFFFFFF)亦可查看。

```php
function foo() { }
$fname = 'foo';
```

开启 debug 后 dump 可看出，发生函数调用优化前 opcode 序列（仅截取片段）为：

```c
ASSIGN CV0($fname) string("foo")
INIT_FCALL_BY_NAME 0 CV0($fname)
DO_FCALL_BY_NAME
```

INIT_FCALL_BY_NAME 这条 opcode 执行逻辑较为复杂，当开启激进内联优化后，可将上述指令序列直接合并成一条 DO_FCALL string("foo")指令，省去间接调用的开销。这样也恰好与直接调用生成的 opcode 一致。

### 4）如何为 opcache opt 添加一个优化 pass

根据以上描述，可见向当前优化器加入一个 pass 并不会太难，大体步骤如下：

- 先向 zend_optimize 优化器注册一个 pass 宏(例如添加 pass17)，并决定其优化级别。
- 在优化管理器某个优化 pass 前后调用加入的 pass（例如添加一个尾递归优化 pass），建议在 DFA/SSA 分析 pass 之后添加，因为此时获得的优化信息更多。
- 实现新加入的 pass，进行定制代码转换（例如 zend*optimize*func_calls 实现一个尾递归优化）。针对当前已有 pass，主要添加转换 pass，这里一般也可利用 SSA/DFA 的信息。不同于静态编译优化一般是在贴近于机器相关的低层中间表示优化，这里主要是在 opcode 层的 opcode／operand 相应的一些转换。
- 实现 pass 前，与函数内联类似，通常首先收集优化所需信息，然后排除掉不适用该优化的一些场景（如非真正的尾不递归调用、参数问题无法做优化等）。实现优化后，可 dump 优化前后生成 opcode 结构的变化是否优化正确、是否符合预期（如尾递归优化最终的效果是变换函数调用为 forloop 的形式）。

## 4.一点思考

以下是对基于动态的 PHP 脚本程序执行的一些看法，仅供参考。

由于 LLVM 从前端到后端，从静态编译到 jit 整个工具链框架的支持，使得许多语言虚拟机都尝试整合。当前 PHP7 时代的 ZendVM 官方还没采用，原因之一虚拟机 opcode 承载着相当复杂的分析工作。相比于静态编译器的机器码每一条指令通常只干一件事情（通常是 CPU 指令时钟周期），opcode 的操作数（operand）由于类型不固定，需要在运行期间做大量的类型检查、转换才能进行运算，这极度影响了执行效率。即使运行时采用 jit，以 byte code 为单位编译，编译出的字节码也会与现有解释器一条一条 opcode 处理类似，类型需要处理、也不能把 zval 值直接存在寄存器。

以函数调用为例，比较现有的 opcode 执行与静态编译成机器码执行的区别，如下图：![alt](https://tech.youzan.com/content/images/2017/06/func-compiler.jpeg)

### 类型推断

在不改变现有 opcode 设计的前提下，加强类型推断能力，进而为 opcode 的执行提供更多的类型信息，是提高执行性能的可选方法之一。

### 多层 opcode

既然 opcode 承担如此复杂的分析工作，能否将其分解成多层的 opcode 归一化中间表示( intermediate representation, IR)。各优化可选择应用哪一层中间表示，传统编译器的中间表示依据所携带信息量、从抽象的高级语言到贴近机器码，分成高级中间表示（HIR） 、中级中间表示（MIR）、低级中间表示（LIR）。

### pass 管理

关于 opcode 的优化 pass 管理，如前文鲸书图所述，应该尚有改进空间。虽然当前分析依赖的有数据流／控制流分析，但仍缺少诸如过程间的分析优化，pass 管理如运行顺序、运行次数、注册管理、复杂 pass 分析的信息 dump 等相对于 llvm 等成熟框架仍有较大差距。

### JIT

ZendVM 实现大量的 zval 值、类型转换等操作，这些可借助 LLVM 编译成机器码用于运行时，但代价是编译时间极速膨胀。当然也可采用 libjit。

## 参考

- [深入理解 PHP opcode 优化](https://tech.youzan.com/understanding-opcode-optimization-in-php/)

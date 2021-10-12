# [pandas](https://pandas.pydata.org/)

## [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

## [pandas教程](https://datawhalechina.github.io/joyful-pandas/build/html/%E7%9B%AE%E5%BD%95/index.html)

- set_index()设置索引

## 基本数据结构

pandas 中具有两种基本的数据存储结构，存储一维 values 的 Series 和存储二维 values 的 DataFrame ，在这两种结构上定义了很多的属性和方法。

### Series

Series 一般由四个部分组成，分别是序列的值 data 、索引 index 、存储类型 dtype 、序列的名字 name 。其中，索引也可以指定它的名字，默认为空。

```python
In [22]: s = pd.Series(data = [100, 'a', {'dic1':5}],
   ....:               index = pd.Index(['id1', 20, 'third'], name='my_idx'),
   ....:               dtype = 'object',
   ....:               name = 'my_name')
   ....: 

In [23]: s
Out[23]: 
my_idx
id1              100
20                 a
third    {'dic1': 5}
Name: my_name, dtype: object
```

#### object 类型

object 代表了一种混合类型，目前 pandas 把纯字符串序列也默认为是一种 object 类型的序列，但它也可以用 string 类型存储。

对于这些属性，可以通过`.`的方式来获取：

```python
In [24]: s.values
Out[24]: array([100, 'a', {'dic1': 5}], dtype=object)

In [25]: s.index
Out[25]: Index(['id1', 20, 'third'], dtype='object', name='my_idx')

In [26]: s.dtype
Out[26]: dtype('O')

In [27]: s.name
Out[27]: 'my_name'
```

利用 .shape 可以获取序列的长度：

```python
In [28]: s.shape
Out[28]: (3,)
```

索引是 pandas 中最重要的概念之一，如果想要取出单个索引对应的值，可以通过 [index_item] 可以取出。

```python
In [29]: s['third']
Out[29]: {'dic1': 5}
```

### DataFrame

DataFrame 在 Series 的基础上增加了列索引，一个数据框可以由二维的 data 与行列索引来构造：

```python
In [30]: data = [[1, 'a', 1.2], [2, 'b', 2.2], [3, 'c', 3.2]]

In [31]: df = pd.DataFrame(data = data,
   ....:                   index = ['row_%d'%i for i in range(3)],
   ....:                   columns=['col_0', 'col_1', 'col_2'])
   ....:

In [32]: df
Out[32]:
       col_0 col_1  col_2
row_0      1     a    1.2
row_1      2     b    2.2
row_2      3     c    3.2
```

但一般而言，更多的时候会采用从列索引名到数据的映射来构造数据框，同时再加上行索引：

```python
In [33]: df = pd.DataFrame(data = {'col_0': [1,2,3], 'col_1':list('abc'),
   ....:                           'col_2': [1.2, 2.2, 3.2]},
   ....:                   index = ['row_%d'%i for i in range(3)])
   ....:

In [34]: df
Out[34]:
       col_0 col_1  col_2
row_0      1     a    1.2
row_1      2     b    2.2
row_2      3     c    3.2
```

由于这种映射关系，在 DataFrame 中可以用 [col_name] 与 [col_list] 来取出相应的列与由多个列组成的表，结果分别为 Series 和 DataFrame ：

```python
In [35]: df['col_0']
Out[35]:
row_0    1
row_1    2
row_2    3
Name: col_0, dtype: int64

In [36]: df[['col_0', 'col_1']]
Out[36]:
       col_0 col_1
row_0      1     a
row_1      2     b
row_2      3     c
```

与 Series 类似，在数据框中同样可以取出相应的属性：

```python
In [37]: df.values
Out[37]:
array([[1, 'a', 1.2],
       [2, 'b', 2.2],
       [3, 'c', 3.2]], dtype=object)

In [38]: df.index
Out[38]: Index(['row_0', 'row_1', 'row_2'], dtype='object')

In [39]: df.columns
Out[39]: Index(['col_0', 'col_1', 'col_2'], dtype='object')

In [40]: df.dtypes # 返回的是值为相应列数据类型的Series
Out[40]:
col_0      int64
col_1     object
col_2    float64
dtype: object

In [41]: df.shape
Out[41]: (3, 3)
```

通过 .T 可以把 DataFrame 进行转置：

```python
In [42]: df.T
Out[42]:
      row_0 row_1 row_2
col_0     1     2     3
col_1     a     b     c
col_2   1.2   2.2   3.2
```

## 函数

head, tail 函数分别表示返回表或者序列的前 n 行和后 n 行，其中 n 默认为5

```python
df.head(2)
df.tail(2)
```

`df.info()`返回表的信息概况
`df.describe()` 返回表中数值列对应的主要统计量

mad() 函数返回的是一个序列中偏离该序列均值的绝对值大小的均值，例如序列1,3,7,10中，均值为5.25，每一个元素偏离的绝对值为4.25,2.25,1.75,4.75

### 统计函数

在 Series 和 DataFrame 上定义了许多统计函数，最常见的是 sum, mean, median, var, std, max, min 。

- df.quantile()分位数
- df.count()非缺失值个数
- df.idxmax()最大值对应的索引
- df.idxmin()最小值对应的索引

### 唯一值函数

对序列使用：

- unique()得到其唯一值组成的列表
- nunique() 得到其唯一值的个数。
- value_counts() 得到唯一值和其对应出现的频数

- duplicated（）返回了是否为唯一值的布尔列表。keep 参数，其返回的序列，把重复元素设为 True ，否则为 False 。
- drop_duplicates()如果想要观察多个列组合的唯一值,去除重复项，保留唯一值。关键参数是 keep ，默认值 first 表示每个组合保留第一次出现的所在行， last 表示保留最后一次出现的所在行， False 表示把所有重复组合所在的行剔除。drop_duplicates 等价于把 duplicated 为 True 的对应行剔除。

### 替换函数

#### replace

可以通过字典构造，或者传入两个列表来进行替换：

    df['Gender'].replace({'Female':0, 'Male':1})
    df['Gender'].replace(['Female', 'Male'], [0, 1])

#### 逻辑替换

包括了 where 和 mask ，这两个函数是完全对称的：

- where 函数在传入条件为 False 的对应行进行替换
- mask 在传入条件为 True 的对应行进行替换，当不指定替换值时，替换为缺失值。

```python
In [72]: s = pd.Series([-1, 1.2345, 100, -50])

In [73]: s.where(s<0)
Out[73]:
0    -1.0
1     NaN
2     NaN
3   -50.0
dtype: float64

In [74]: s.where(s<0, 100)
Out[74]:
0     -1.0
1    100.0
2    100.0
3    -50.0
dtype: float64

In [75]: s.mask(s<0)
Out[75]:
0         NaN
1      1.2345
2    100.0000
3         NaN
dtype: float64

In [76]: s.mask(s<0, -50)
Out[76]:
0    -50.0000
1      1.2345
2    100.0000
3    -50.0000
dtype: float64
```

需要注意的是，传入的条件只需是与被调用的 Series 索引一致的布尔序列即可：

```python
In [77]: s_condition= pd.Series([True,False,False,True],index=s.index)

In [78]: s.mask(s_condition, -50)
Out[78]:
0    -50.0000
1      1.2345
2    100.0000
3    -50.0000
dtype: float64
```

#### 数值替换

数值替换包含了 round, abs, clip 方法，它们分别表示取整、取绝对值和截断：

```ipython
In [79]: s = pd.Series([-1, 1.2345, 100, -50])

In [80]: s.round(2)
Out[80]:
0     -1.00
1      1.23
2    100.00
3    -50.00
dtype: float64

In [81]: s.abs()
Out[81]:
0      1.0000
1      1.2345
2    100.0000
3     50.0000
dtype: float64

In [82]: s.clip(0, 2) # 前两个数分别表示上下截断边界
Out[82]:
0    0.0000
1    1.2345
2    2.0000
3    0.0000
dtype: float64
```

### 排序函数

排序共有两种方式，

- 值排序sort_values()
- 索引排序sort_index()

对身高进行排序，默认参数 ascending=True 为升序：

```python
In [84]: df_demo.sort_values('Height').head()
Out[84]:
                         Height  Weight
Grade     Name
Junior    Xiaoli Chu      145.4    34.0
Senior    Gaomei Lv       147.3    34.0
Sophomore Peng Han        147.8    34.0
Senior    Changli Lv      148.7    41.0
Sophomore Changjuan You   150.5    40.0

In [85]: df_demo.sort_values('Height', ascending=False).head()
Out[85]:
                        Height  Weight
Grade    Name
Senior   Xiaoqiang Qin   193.9    79.0
         Mei Sun         188.9    89.0
         Gaoli Zhao      186.5    83.0
Freshman Qiang Han       185.3    87.0
Senior   Qiang Zheng     183.9    87.0
```

多列排序：

```python
In [86]: df_demo.sort_values(['Weight','Height'],ascending=[True,False]).head()
Out[86]:
                       Height  Weight
Grade     Name
Sophomore Peng Han      147.8    34.0
Senior    Gaomei Lv     147.3    34.0
Junior    Xiaoli Chu    145.4    34.0
Sophomore Qiang Zhou    150.5    36.0
Freshman  Yanqiang Xu   152.4    38.0
```

索引排序的用法和值排序完全一致，只不过元素的值在索引中，此时需要指定索引层的名字或者层号，用参数 level 表示。另外，需要注意的是字符串的排列顺序由字母顺序决定。

### apply方法

apply 方法常用于 DataFrame 的行迭代或者列迭代， apply 的参数默认是一个以序列x为输入的函数。

```python
In [88]: df_demo = df[['Height', 'Weight']]

In [89]: def my_mean(x):
   ....:     res = x.mean()
   ....:     return res
   ....:

In [90]: df_demo.apply(my_mean)
Out[90]:
Height    163.218033
Weight     55.015873
dtype: float64
```

指定 axis=1 ，那么每次传入函数的就是行元素组成的 Series ，其结果与之前的逐行均值结果一致。

```python
In [92]: df_demo.apply(lambda x:x.mean(), axis=1).head()
Out[92]: 
0    102.45
1    118.25
2    138.95
3     41.00
4    124.00
dtype: float64
```

### [swifter](https://github.com/jmcarpenter2/swifter)多核执行

优化，提速

```python
df_demo.swifter.apply(lambda x:x.mean(), axis=1).head()
```

## 窗口对象

滑动窗口 rolling 、扩张窗口 expanding 以及指数加权窗口 ewm

## excel

### 读取

```python
import pandas as pd
df_excel = pd.read_excel('data/my_excel.xlsx')
#接受工作表名称，将工作表转换成Dataframe
```

常用的公共参数：

- header=None 表示第一行不作为列名，
- index_col 表示把某一列或几列作为索引
- usecols 表示读取列的集合，默认读取所有的列`usecols=['col1', 'col2']`
- parse_dates 表示需要转化为时间的列`parse_dates=['col5']`
- nrows 表示读取的数据行数。

df是一个dataframe，可以用`df.columns`看看表头有哪些列，可以用`df.loc['行标签','列标签']`获取/设置特定位置的内容

### 写入

```python
df_excel.to_excel('data/my_excel_saved.xlsx', index=False)
```

把 index 设置为 False ，特别当索引没有特殊意义的时候，把索引在保存的时候去除。

## 数据处理

### 丢失的数据类型主要有None 和 np.nan

np.nan是一个float类型的数据 None是一个NoneType类型

1、在ndarray中显示时 np.nan会显示nan，如果进行计算 结果会显示为NANNone显示为None，并且对象为object类型,如果进行计算，结果会报错所以ndarray中无法对有缺失值的数据进行计算

2、 在Serise中显示的时候都会显示为NAN，均可以视作np.nan

    进行计算时可以通过`np.sum()`得到结果，此时NAN默认为0.0
    
    s1 + 10 对于空值得到的结果为NAN,
    如果使用加法 可以通过s1.add(参数，fill_value = 0)指定空值的默认值为0

## 索引

对于表而言，有两种索引器，一种是基于元素的loc索引器，另一种是基于位置的 iloc 索引器。

### loc 索引器

loc 索引器的一般形式是`loc[*, *]`，其中第一个`*`代表行的选择，第二个`*`代表列的选择，如果省略第二个位置写作`loc[*]`，这个`*`是指行的筛选。其中，`*` 的位置一共有五类合法对象，分别是：单个元素、元素列表、元素切片、布尔列表以及函数。

### iloc 索引器

iloc 的使用与 loc 完全类似，只不过是针对位置进行筛选，在相应的 * 位置处一共也有五类合法对象，分别是：整数、整数列表、整数切片、布尔列表以及函数，函数的返回值必须是前面的四类合法对象中的一个，其输入同样也为 DataFrame 本身。

## tips

[python DataFrame转dict字典过程详解](http://www.cppcns.com/jiaoben/python/295412.html)

```python
# 将item_id,item_category两列数值转为dict字典
# 注意：同种商品类别肯定会对应不同商品，即一对多，进行字典映射，一定要是item_id作为键，item_category作为值
# 由于原始数据为int类型，结果将是字符串之间的映射，因此需要对列值进行数据类型转换
item.item_id = (item['item_id']).astype(str)
item.item_category = (item['item_category']).astype(str)
item_dict = item.set_index('item_id')['item_category'].to_dict()
```

或者另一种复杂一点方法
[将dataframe中的两列数据转换成字典dic](https://lover.blog.csdn.net/article/details/100692266?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.control)

## SettingWithCopyWarning

<https://zhuanlan.zhihu.com/p/41202576>

`SettingWithCopyWarning` 是一个警告 Warning，而不是错误 Error。

错误表明某些内容是“坏掉”的，例如无效语法（invalid syntax）或尝试引用未定义的变量；警告的作用是提醒编程人员，他们的代码可能存在潜在的错误或问题，但是这些操作在该编程语言中依然合法。在这种情况下，警告很可能表明一个严重但不容易意识到的错误。

## Memory Error问题的解决方法汇总

<https://blog.csdn.net/qq_41780295/article/details/89677453>

## read csv

报错提示：“sys:1: DtypeWarning: Columns (15) have mixed types. Specify dtype option on import or set low_memory=False.”

low_memory : boolean, default True

- 分块加载到内存，再低内存消耗中解析，但是可能出现类型混淆。
- 确保类型不被混淆需要设置为False，或者使用dtype 参数指定类型。
- 注意使用chunksize 或者iterator 参数分块读入会将整个文件读入到一个Dataframe，而忽略类型（只能在C解析器中有效）

```python
import pandas as pd
pd = pd.read_csv(Your_path, low_memory=False)
```

http://www.cnblogs.com/duanxz/p/3862356.html
mysql插入数据后返回自增ID的方法
 
mysql和oracle插入的时候有一个很大的区别是，oracle支持序列做id，mysql本身有一个列可以做自增长字段，mysql在插入一条数据后，如何能获得到这个自增id的值呢？
 
方法一：是使用last_insert_id

mysql> SELECT LAST_INSERT_ID();
    产生的ID 每次连接后保存在服务器中。这意味着函数向一个给定客户端返回的值是该客户端产生对影响AUTO_INCREMENT列的最新语句第一个 AUTO_INCREMENT值的。这个值不能被其它客户端影响，即使它们产生它们自己的 AUTO_INCREMENT值。这个行为保证了你能够找回自己的 ID 而不用担心其它客户端的活动，而且不需要加锁或处理。 
 
    每次mysql_query操作在mysql服务器上可以理解为一次“原子”操作, 写操作常常需要锁表的， 是mysql应用服务器锁表不是我们的应用程序锁表。
 
    值得注意的是，如果你一次插入了多条记录，这个函数返回的是第一个记录的ID值。
    因为LAST_INSERT_ID是基于Connection的，只要每个线程都使用独立的Connection对象，LAST_INSERT_ID函数 将返回该Connection对AUTO_INCREMENT列最新的insert or update*作生成的第一个record的ID。这个值不能被其它客户端（Connection）影响，保证了你能够找回自己的 ID 而不用担心其它客户端的活动，而且不需要加锁。使用单INSERT语句插入多条记录,  LAST_INSERT_ID返回一个列表。
    LAST_INSERT_ID 是与table无关的，如果向表a插入数据后，再向表b插入数据，LAST_INSERT_ID会改变。
 
方法二：是使用max(id)
 
使用last_insert_id是基础连接的，如果换一个窗口的时候调用则会一直返回10
如果不是频繁的插入我们也可以使用这种方法来获取返回的id值

select max(id) from user;
这个方法的缺点是不适合高并发。如果同时插入的时候返回的值可能不准确。
 
方法三：是创建一个存储过程，在存储过程中调用先插入再获取最大值的操作

复制代码
DELIMITER $$
DROP PROCEDURE IF EXISTS `test` $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `test`(in name varchar(100),out oid int)
BEGIN
  insert into user(loginname) values(name);
  select max(id) from user into oid;
  select oid;
END $$
DELIMITER ;
call test('gg',@id);
复制代码
方法四:使用@@identity

select @@IDENTITY
    @@identity是表示的是最近一次向具有identity属性(即自增列)的表插入数据时对应的自增列的值，是系统定 义的全局变量。一般系统定义的全局变量都是以@@开头，用户自定义变量以@开头。比如有个表A，它的自增列是id，当向A表插入一行数据后，如果插入数据 后自增列的值自动增加至101，则通过select @@identity得到的值就是101。使用@@identity的前提是在进行insert操作后，执行select @@identity的时候连接没有关闭，否则得到的将是NULL值。

方法五:是使用getGeneratedKeys()

复制代码
Connection conn = ;
Serializable ret = null;
PreparedStatement state = .;
ResultSet rs=null;
try {
    state.executeUpdate();
    rs = state.getGeneratedKeys();
    if (rs.next()) {
        ret = (Serializable) rs.getObject(1);
    }     
} catch (SQLException e) {
}
return ret;
复制代码
总结一下，在mysql中做完插入之后获取id在高并发的时候是很容易出错的。另外last_insert_id虽然是基于session的但是不知道为什么没有测试成功。
     
方法6：selectkey:

其实在ibtias框架里使用selectkey这个节点，并设置insert返回值的类型为integer，就可以返回这个id值。

SelectKey在Mybatis中是为了解决Insert数据时不支持主键自动生成的问题，他可以很随意的设置生成主键的方式。

不管SelectKey有多好，尽量不要遇到这种情况吧，毕竟很麻烦。

 

selectKey Attributes
属性	描述
keyProperty	selectKey 语句结果应该被设置的目标属性。
resultType	结果的类型。MyBatis 通常可以算出来,但是写上也没有问题。MyBatis 允许任何简单类型用作主键的类型,包括字符串。
order	这可以被设置为 BEFORE 或 AFTER。如果设置为 BEFORE,那么它会首先选择主键,设置 keyProperty 然后执行插入语句。如果设置为 AFTER,那么先执行插入语句,然后是 selectKey 元素-这和如 Oracle 数据库相似,可以在插入语句中嵌入序列调用。
statementType	和前面的相 同,MyBatis 支持 STATEMENT ,PREPARED 和CALLABLE 语句的映射类型,分别代表 PreparedStatement 和CallableStatement 类型。
 

SelectKey需要注意order属性，像Mysql一类支持自动增长类型的数据库中，order需要设置为after才会取到正确的值。

像Oracle这样取序列的情况，需要设置为before，否则会报错。

 

另外在用Spring管理事务时，SelectKey和插入在同一事务当中，因而Mysql这样的情况由于数据未插入到数据库中，所以是得不到自动增长的Key。取消事务管理就不会有问题。

 

下面是一个xml和注解的例子，SelectKey很简单，两个例子就够了：

<insert id="insert" parameterType="map">  
    insert into table1 (name) values (#{name})  
    <selectKey resultType="java.lang.Integer" keyProperty="id">  
      CALL IDENTITY()  
    </selectKey>  
</insert>
上面xml的传入参数是map，selectKey会将结果放到入参数map中。用POJO的情况一样，但是有一点需要注意的是，keyProperty对应的字段在POJO中必须有相应的setter方法，setter的参数类型还要一致，否则会报错。

@Insert("insert into table2 (name) values(#{name})")  
@SelectKey(statement="call identity()", keyProperty="nameId", before=false, resultType=int.class)  
int insertTable2(Name name); 
上面是注解的形式。

方法:7：使用<insert中的useGeneratedKeys 和keyProperty 两个属性

1.在Mybatis Mapper文件中添加属性“useGeneratedKeys”和“keyProperty”，其中keyProperty是Java对象的属性名，而不是表格的字段名。

2.Mybatis执行完插入语句后，自动将自增长值赋值给对象systemBean的属性id。因此，可通过systemBean对应的getter方法获取！

【注意事项】

1.Mybatis Mapper 文件中，“useGeneratedKeys”和“keyProperty”必须添加，而且keyProperty一定得和java对象的属性名称一直，而不是表格的字段名

2.java Dao中的Insert方法，传递的参数必须为java对象，也就是Bean，而不能是某个参数。
以角色为基础的访问控制（Role-based access control,RBAC），是资讯安全领域中，一种较新且广为使用的访问控制机制，其不同于强制访问控制以及自由选定访问控制直接赋予使用者权限，而是将权限赋予角色。是一套较强制访问控制以及自由选定访问控制更为中性且更具灵活性的访问控制技术。


一些理论性的东西：


RBAC模型的基本思想是将访问许可权分配给一定的角色，用户通过饰演不同的角色获得角色所拥有的访问许可权。


访问控制可以简单表述为：判断谁（Who）对什么（What/Which）进行怎样（How）的操作是否为真。


在RBAC中，用户的权限不是在用户本身上进行管理的，用户的权限是由用户所处的角色所决定的。在权限管理中，通过角色这一桥梁将用户与权限联系起来。用户和角色、角色与权限是一个多对多的关系。


与RBAC访问控制相关的概念有：
1. 用户（User）：一个具有唯一标识符的用户，与权限相分离，只能通过所属的Role去关联权限，一个用户可以拥有多项角色；
2. 角色（Role）:一定数量的权限的集合，角色可以继承，一个角色对应多项权限；
3. 权限（Resource）：也可以看作是资源，它对应了应用系统中的一个功能；


        



设计对应的数据表结构：


这里使用的是ThinkPHP的表结构，字段设置符合功能的设计要求。


第一个表是 用户表，都是一些很常用的字段，比较好理解



    CREATE TABLE `think_user` (
      `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT,
      `account` varchar(64) NOT NULL,
      `nickname` varchar(50) NOT NULL,
      `password` char(32) NOT NULL,
      `email` varchar(50) NOT NULL,
      `remark` varchar(255) NOT NULL,
      `create_time` int(11) UNSIGNED NOT NULL,
       `status` tinyint(1) DEFAULT '0',
       PRIMARY KEY  (`id`),
      UNIQUE KEY `account` (`account`)
    ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8



第二个是角色表，也可以理解为分组表



    CREATE TABLE IF NOT EXISTS `think_role` (
     `id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
     `name` varchar(20) NOT NULL,
     `pid` smallint(6) DEFAULT NULL,
     `status` tinyint(1) UNSIGNED DEFAULT NULL,
     `remark` varchar(255) DEFAULT NULL,
     PRIMARY KEY (`id`),
     KEY `pid` (`pid`),
     KEY `status` (`status`)
     ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 ;



第三个是 角色—用户—关系映射表，注意，这个表的数据，可以是多对多的关系，也就是多个角色对应一个用户，多个用户对应一个角色。在我的实际使用中，没有涉及到一个用户对应多个角色的情况，也是为了简化操作。



        CREATE TABLE IF NOT EXISTS `think_role_user` (
         `role_id` mediumint(9) UNSIGNED DEFAULT NULL,
         `user_id` char(32) DEFAULT NULL,
         KEY `group_id` (`role_id`),
         KEY `user_id` (`user_id`)
         ) ENGINE=MyISAM DEFAULT CHARSET=utf8;



第四个是节点表，也就是资源表，要注意的两个字段：pid 用来关联节点的层级，level用来说明该节点是 应用 ，还是模块和操作。



    CREATE TABLE IF NOT EXISTS `think_node` (
     `id` smallint(6) UNSIGNED NOT NULL AUTO_INCREMENT,
     `name` varchar(20) NOT NULL,
     `title` varchar(50) DEFAULT NULL,
     `status` tinyint(1) DEFAULT '0',
     `remark` varchar(255) DEFAULT NULL,
     `sort` smallint(6) UNSIGNED DEFAULT NULL,
     `pid` smallint(6) UNSIGNED NOT NULL,
     `level` tinyint(1) UNSIGNED NOT NULL,
     PRIMARY KEY (`id`),
     KEY `level` (`level`),
     KEY `pid` (`pid`),
     KEY `status` (`status`),
     KEY `name` (`name`)
     ) ENGINE=MyISAM  DEFAULT CHARSET=utf8;



最后，也是最关键的表 权限访问表，这个表中的数据，是每个角色对应的权限。理解这个表的结构，也就明白了整个RBAC的关键。



    CREATE TABLE IF NOT EXISTS `think_access` (
     `role_id` smallint(6) UNSIGNED NOT NULL,
     `node_id` smallint(6) UNSIGNED NOT NULL,
     `level` tinyint(1) NOT NULL,
     `module` varchar(50) DEFAULT NULL,
     KEY `groupId` (`role_id`),
     KEY `nodeId` (`node_id`)
     ) ENGINE=MyISAM DEFAULT CHARSET=utf8;



通过以上五张表即可完成基于RBAC的权限控制。当然，上面提到的都是整个权限管理的基础数据，也就是需要配置的数据。下一步，就是要在用户登录的时候，获取对应的权限。


获取用户的权限列表的方法是：
1. 查询用户所属的角色ID；
2.  根据角色ID从access表中获取该角色所能访问的节点列表；
3.  从node中查询节点列表的相关信息；
4.  对产生的节点列表信息进行处理，生成访问决策列表保存到SESSION中；


到此，已经能够知道当前用户对应的权限列表了，在实际项目中，就可以根据使用的框架，设置权限验证的环节。比如在ThinkPHP 中，是通过设置 自己的公共控制器来实现统一入口验证，在CodiIgniter中，一般是通过设置Hooks，来实现在程序入口鉴权。
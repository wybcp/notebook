# configparser

模块能被用来读取配置文件。

在每个配置文件中，配置数据会被分组（比如例子中的“installation”、 “debug” 和 “server”）。每个分组在其中指定对应的各个变量值。

创建 ConfigPaser 时有多个参数，比较重要的是 allow_no_value。

allow_no_value 默认取值为 False，表示在配置文件中是否允许选项没有值的情况。在一些特殊的应用中，选项存在就表示取值为真，选项不存在就表示取值为假。

- sections:返回一个包含所有章节的列表;
- has_section:判断章节是否存在;
- items:以元组的形式返回所有选项;
- options:返回一个包含章节下所有选项的列表;
- has_option:判断某个选项是否存在;
- get、 getboolean、 getinit、 getfloat:获取选项的值 。
- remove_section:删除一个章节;
- add_section:添加一个章节;
- remote_option:删除一个选项;
- set:添加一个选项;
- write 将 ConfigParser 对象中的数据保存到文件中 。

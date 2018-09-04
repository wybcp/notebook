# 字段类型

设计原则：保小不保大，能用占用直接小的字段就不用大字段。

常见字段类型设置建议：
|字段|类型|缘由
|--|--|--|
|手机号|bigint|bigint 只有 8 个字节，string 则需要 3\*11=33 个字节|
|ipv4|unsigned int(11)|使用 inet_aton()将 ip 转换为数字（反函数 inet_ntoa()）,char(15)不建议(有待商榷),IPV4 a minimum length of 7 characters (0.0.0.0) and a maximum length of 15 (255.255.255.255).IPv6 becomes more prevalent, the savings will only become larger: a 128-bit (16 byte) IPv6 address can be up to 39 characters long when represented in a “human readable” format.|
|年龄|tinyint(3)|0~150，一个字节|
|状态|tinyint|0 表示优，1 表示良...也可使用 enum，都是 1 字节，当 enum 不利于扩展（）也可以限定状态），可以直观展示
|时间|timestamp|timestamp（4字节，）和datetime（8字节）都精确到秒，具有自动更新时间功能，设置默认为null可禁止更新
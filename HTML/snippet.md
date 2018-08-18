# snippet

种语言创建代码段,这里以设置js代码段为例,其他语言方法是一样的.
选择js后会自动打开一个JSON格式的配置文件.Visual Studio Code默认已经给出Demo了.照葫芦画瓢即可.

```
{
/*
	 // Place your snippets for JavaScript here. Each snippet is defined under a snippet name and has a prefix, body and 
	 // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	 // $1, $2 for tab stops, ${id} and ${id:label} and ${1:label} for variables. Variables with the same id are connected.
	 // Example:
	 "Print to console": {
		"prefix": "log",
		"body": [
			"console.log('$1');",
			"$2"
		],
		"description": "Log output to console"
	}
*/
}
```



参数解释:

+ prefix      :这个参数是使用代码段的快捷入口,比如这里的log在使用时输入log会有智能感知.
+ body        :这个是代码段的主体.需要设置的代码放在这里,字符串间换行的话使用\r\n换行符隔开.注意如果值里包含特殊字符需要进行转义.多行语句的以,隔开

+ $1          :这个为光标的所在位置.
+ $2          :使用这个参数后会光标的下一位置将会另起一行,按tab键可进行快速切换,还可以有$3,$4,$5.....
+ description :代码段描述,在使用智能感知时的描述
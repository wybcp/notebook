# Email

PHP 允许您从脚本直接发送电子邮件。

防止 e-mail 注入的最好方法是对输入进行验证。
```
 function spamcheck($field)
{
	// filter_var() 过滤 e-mail
	// 使用 FILTER_SANITIZE_EMAIL
	$field=filter_var($field, FILTER_SANITIZE_EMAIL);

	//filter_var() 过滤 e-mail
	// 使用 FILTER_VALIDATE_EMAIL
	if(filter_var($field, FILTER_VALIDATE_EMAIL))
	{
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}```


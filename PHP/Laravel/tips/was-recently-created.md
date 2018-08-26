# wasRecentlyCreated

使用 model 模型的`wasRecentlyCreated`属性检测这个模型是否已经被创建或者找到

```php
$user=User::firstOrCreated([
    'name'=>'riverside'
]);
if($user->wasRencentlyCreated){
//            new user
}else{
//            this user was found in the database.
}
```

[firstOrCreate](https://laravel.0x123.com/zh/docs/5.5/eloquent#other-creation-methods)
  
 `firstOrCreate` 方法会使用给定的字段及其值在数据库中查找记录。如果在数据库中找不到模型，则将使用第一个参数中的属性以及可选的第二个参数中的属性插入记录。

https://twitter.com/marcelpociot/status/949689761979039744/photo/1?ref_src=twsrc%5Etfw&ref_url=https%3A%2F%2Fmurze.be%2Fuse-the-wasrecentlycreated-model-attribute-to-check-if-your-model-was-created-or-found

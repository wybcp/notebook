# 代码注释

代码注释，可以说是比代码本身更重要。

## 一、不要重复阅读者已经知道的内容（×）

一些光看方法名，光看代码就能看出来功能的就没必要写注释，

```php
// If the color is red, turn it green
if (color.is_red()) {
  color.turn_green();
}
```

## 二、要注释说明推理和历史（√）

如果代码中的业务逻辑以后可能需要更新或更改，那就应该留下注释:

```php
/* The API currently returns an array of items
even though that will change in an upcoming ticket.
Therefore, be sure to change the loop style here so that
we properly iterate over an object */

var api_result = {items: ["one", "two"]},
    items = api_result.items,
    num_items = items.length;

for(var x = 0; x < num_items; x++) {
  ...
}
```

## 三、同一行的注释不要写得很长（×）

```php
function Person(name) {
  this.name = name;
  this.first_name = name.split(" ")[0]; // This is just a shot in the dark here. If we can extract the first name, let's do it
}
```

## 四、要把长注释放在逻辑上面，短注释放在后面（√）

注释如果不超过 120 个字符那可以放在代码旁边。否则，就应该直接把注释放到语句上面。

```php
if (person.age < 21) {
  person.can_drink = false; // 21 drinking age

  /* Fees are given to those under 25, but only in
     some states. */
  person.has_car_rental_fee = function(state) {
    if (state === "MI") {
      return true;
    }
  };
}
```

## 五、不要为了注释而添加不必要的注释（×）

```php
if (person.age >= 21) {
  person.can_drink = true; // A person can drink at 21
  person.can_smoke = true; // A person can smoke at 18
  person.can_wed = true; // A person can get married at 18
  person.can_see_all_movies = true; // A person can see all movies at 17
  //I hate babies and children and all things pure because I comment too much
}
```

## 六、注释要拼写正确（√）

不要为代码注释中的拼写错误找借口。IDE 可以为你检查拼写。如果没有这个功能，那就去下载插件，自己动手！

## 七、要多多练习（√）

熟能生巧。试着写一些有用的注释，可以问问其他开发人员你的注释是否有用。随着时间的推移，你会慢慢懂得怎样才算是友好的注释。

## 八、要审查别人的注释（√）

在代码审查时，我们往往会忽略查看注释。不要怕要求更多的注释，你应该提出质疑。如果每个人都养成写好注释的好习惯，那么世界将会更美好。

## 九、对注释一定要知道的的精华总结

注释是开发进程中非常重要的一部分，但我们不应该为了注释而注释。注释应该是有用的，简洁的，应该是对代码的一种补充。注释不应该用于逐行地解释代码，相反，它应该用于解释业务逻辑，推理以及对将来的启示。

[PHP 代码注释小细节](http://m.php.cn/article/350210.html)

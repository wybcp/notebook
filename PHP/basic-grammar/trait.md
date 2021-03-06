# [Trait](https://secure.php.net/manual/zh/language.oop5.traits.php)

自 PHP 5.4.0 起，PHP 实现了一种代码复用的方法，称为 trait。

Trait 是为类似 PHP 的单继承语言而准备的一种代码复用机制。Trait 为了减少单继承语言的限制，无法通过 trait 自身来实例化。它为传统继承增加了水平特性的组合。

## trait 定义

```php
trait t{
  public function test(){}
}
# 使用
class Test{
  use t;
  public function test2{
    $this->test();
  }
}
```

## 优先级

从基类继承的成员会被 trait 插入的成员所覆盖。优先顺序是来自当前类的成员覆盖了 trait 的方法，而 trait 则覆盖了被继承的方法。

## 多个 trait 组合

通过逗号分隔，在 use 声明列出多个 trait，可以都插入到一个类中

## 冲突的解决

如果多个 trait 中，都有同名的方法，则会产生冲突，冲突会产生一个致命的错误。

为了解决多个 trait 在同一个类中的命名冲突，

- 需要使用`insteadof`操作符来明确指定使用冲突方法中的哪一个
- `as`操作符可以为某个方法引入别名

```php
trait A {
    public function smallTalk() {
        echo 'a';
    }
    public function bigTalk() {
        echo 'A';
    }
}

trait B {
    public function smallTalk() {
        echo 'b';
    }
    public function bigTalk() {
        echo 'B';
    }
}

class Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
    }
}

class Aliased_Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
        B::bigTalk as talk;
    }
}
```

## 使用 as 修改访问控制

```php
class Base {
    public function say(){
        echo "base";
    }
}
trait Test{
    public function say(){
        echo "trait";
    }
}

class Son extends Base {
    use Test {say as private say2;}
    public function say(){
        echo "son";
    }
}

$s = new Son();
$s->say2();//error
```

## 使用多个 trait 组合

```php
trait A{}
trait B{}
trait C{
    use A,B;
}
```

## trait 抽象成员方法

为了对使用的类施加强制要求，trait 支持抽象方法的使用

```php
trait T{
  abstract public function test();
}

class Test{
  use T;
  public function test(){}
}
```

## trait 静态方法

```php
trait T{
   public static function test() {};
}

class Test{
  use T;
}
Test::test();
```

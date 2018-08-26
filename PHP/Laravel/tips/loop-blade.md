# [循环体中使用 $loop 变量](http://laravelacademy.org/post/6780.html)

在循环的时候，可以在循环体中使用 $loop 变量，该变量提供了一些有用的信息，比如当前循环索引，以及当前循环是不是第一个或最后一个迭代：

```html
@foreach ($users as $user)
    @if ($loop->first)
        This is the first iteration.
    @endif

    @if ($loop->last)
        This is the last iteration.
    @endif

    <p>This is user {{ $user->id }}</p>
@endforeach
```

如果你身处嵌套循环，可以通过 $loop 变量的 parent 属性访问父级循环：

```html
@foreach ($users as $user)
    @foreach ($user->posts as $post)
        @if ($loop->parent->first)
            This is first iteration of the parent loop.
        @endif
    @endforeach
@endforeach
```

$loop 变量还提供了其他一些有用的属性：

| 属性             | 描述                         |
| ---------------- | ---------------------------- |
| $loop->index     | 当前循环迭代索引 (从 0 开始) |
| $loop->iteration | 当前循环迭代 (从 1 开始)     |
| $loop->remaining | 当前循环剩余的迭代           |
| $loop->count     | 迭代数组元素的总数量         |
| $loop->first     | 是否是当前循环的第一个迭代   |
| $loop->last      | 是否是当前循环的最后一个迭代 |
| $loop->depth     | 当前循环的嵌套层级           |
| $loop->parent    | 嵌套循环中的父级循环变量     |

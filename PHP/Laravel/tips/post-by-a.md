# 使用 a 标签 post 提交表单

```html
<a href="{{route('logout')}}" onclick="event.preventDefault();
document.getElementById('logout-form').submit()">退出登录</a>
<form action="{{route('logout')}}" id="logout-form" style="display: none" method="post">
</form>
```

# 错误码设计

[新浪错误码参考](https://open.weibo.com/wiki/Error_code)

错误代码说明：20502

| 2                            | 05           | 02           |
| ---------------------------- | ------------ | ------------ |
| 服务级错误（1 为系统级错误） | 服务模块代码 | 具体错误代码 |

- 服务级别错误：1 为系统级错误；2 为普通错误，通常是由用户非法操作引起的
- 服务模块为两位数：一个大型系统的服务模块通常不超过两位数
- 错误码为两位数：防止一个模块定制过多的错误码，后期不好维护
- code = 0 说明是正确返回，

```json
{
  "code": 20502,
  "message": "Error occurred while binding the request body to the struct."
}
```

# Composer 授权

由于 GitHub api 限制调用频率，使用 composer 时可能会频繁要求你输入你的 github 账号及密码。你可以使用提前配置避免这个问题。

配置过程如下：

1. 在[GitHub](https://github.com/settings/tokens) 创建一个 OAuth token，成功后 token 仅显示一次，请自行保存，否则需要重新生成。

2. 使用这个命令全局配置 `composer config -g github-oauth.github.com <oauthtoken>`或者只在某个项目使用，请在`composer.json`添加：

   ```json
   {
     "github-oauth": {
       "github.com": "oauthtoken"
     }
   }
   ```

## 参考

https://getcomposer.org/doc/articles/troubleshooting.md#api-rate-limit-and-oauth-tokens

# install

```
gem install bundler
ERROR:  While executing gem ... (Gem::RemoteFetcher::FetchError)
    Errno::ECONNRESET: An existing connection was forcibly closed by the remote host. - SSL_connect (https://api.rubygems.org/quick/Marshal.4.8/bundler-1.10.6.gemspec.rz)
 ```
 
临时的解决方法：

1）改用http版本(ok)
```
>gem sources -r https://rubygems.org/
https://rubygems.org/ removed from sources
>gem sources -a http://rubygems.org/
https://rubygems.org is recommended for security over http://rubygems.org/
Do you want to add this insecure source? [yn]  y
http://rubygems.org/ added to sources
>gem sources
*** CURRENT SOURCES ***
http://rubygems.org/
```
注意https末尾是有斜杠的，改用http时也保持一致。
 
2）bundle项目临时改用taobao镜像
```
>bundle config mirror.https://rubygems.org https://ruby.taobao.org
>```
3）改用taobao镜像
```
gem sources --r https://rubygems.org/
gem sources --r http://rubygems.org/
gem sources -a https://ruby.taobao.org/
```
 
原因请参看https://ruby.taobao.org/ 的说明，亚马逊云平台被限制访问了。

http://blog.csdn.net/zhangbin1314/article/details/51122397
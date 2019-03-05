# 蓝灯

查看蓝灯的设置网页里面的信息

代理地址是： http://127.0.0.1:50815

## git

在终端设置：

```sh
git config --global http.proxy http://127.0.0.1:50815
git config --global https.proxy https://127.0.0.1:50815
```

默认不设置代理：

```sh
git config --global --unset http.proxy
git config --global --unset https.proxy
```

查看已经设置的值：

```sh
git config http.proxy
```

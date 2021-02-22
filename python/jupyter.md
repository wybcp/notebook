# [Jupyter](https://jupyter.org/index.html)

## 简介

jupyter notebook是一种 Web 应用，能让用户将说明文本、数学方程、代码和可视化内容全部组合到一个易于共享的文档中。它可以直接在代码旁写出叙述性文档，而不是另外编写单独的文档。也就是它可以能将代码、文档等这一切集中到一处，让用户一目了然。

Jupyter这个名字是它要服务的三种语言的缩写：Julia，PYThon和R，这个名字与“木星（jupiter）”谐音。Jupyter Notebook 已迅速成为数据分析，机器学习的必备工具。因为它可以让数据分析师集中精力向用户解释整个分析过程。我们可以通过Jupyter notebook写出了我们的学习笔记。但是jupyter远远不止支持上面的三种语言，目前能够使用的语言他基本上都能支持，包括C、C++、C#，java、Go等等。

## 使用

### 安装启用

在文件夹输入`jupyter notebook`

jupyter notebook会在浏览器中中打开，是一种Web应用,当一次打开多个jupyter notebook的时候，端口号会依次递增8889，8890依次递增。

### 查看配置文件

在cmd中使用如下命令：`jupyter-notebook --generate-config`

找到`jupyter_notebook_config.py`配置文件

- 有两个井号开头 ##，是注释文本
- 以一个井号#开头的实际上就是默认的配置信息

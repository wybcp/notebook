# Python

Python 3.7

## [语言规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/)

google python 风格指南



**black**

可以说是最流行最多人使用的python格式化工具了，统一的格式化标准。傻瓜化的使用方式，极少的定制化选项（没错，开发者包括使用 black 的人都认为这是个优势）。

默认的 black 是将字符串格式化成用双引号包含且不支持自定义，在连续的用户抗议和开发组成员“吵”了近百楼，各种丢数据各种引经据典后，开发组成员才勉为其难给出了个不格式化字符串引号的选项。github 原楼请戳。

**总结**

autopep8 是刚开始学习 python 的人都被推荐的一个格式化工具，不幸的是它已经不适合当下了。较低的维护频率，较低的社区活跃度，一大堆 issuse 未解决。都是我们放弃它的理由。

yapf 包含着 google 文化中的工程师极客精神，支持多样化的自定义配置是他的优点。如果你对自己的代码风格有硬性的要求，yapf 将是你不二的选择。

black 秉承的是 "less is more" 的设计标准，开发组人员负责调研哪种格式化风格更适合pythonista的开发。允许我们自定义的余地较小，但对于我们来说，有人替我们考虑了哪种方式更好，躺平享受成果不失为一种最好的选择。

## 目录

## 参考

- [关于 Python 的面试题](https://github.com/taizilongxu/interview_python)
- [learn-python](https://github.com/trekhleb/learn-python)
- [Python 时间处理方法总结](https://mp.weixin.qq.com/s/ng8KnEWBewPs11acmcfiOw)

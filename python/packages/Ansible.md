# [Ansible](https://github.com/ansible/ansible)

Ansible是一个极其简单的IT自动化系统。它处理配置管理，应用程序部署，云配置，临时任务执行和多节点编排 – 包括通过负载平衡器轻松实现零停机滚动更新等操作。

[Ansible中文权威指南](https://ansible-tran.readthedocs.io/en/latest/)

## 安装

```bash
brew install ansible

#Mac OS X by default is configured for a small number of file handles, so if you want to use 15 or more forks you’ll need to raise the ulimit bellow command. This command can also fix any “Too many open files” error.
sudo launchctl limit maxfiles unlimited
```

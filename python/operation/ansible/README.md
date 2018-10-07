# [Ansible](https://github.com/ansible/ansible)

ansible 2.6

Ansible 是一个极其简单的 IT 自动化系统。它处理配置管理，应用程序部署，云配置，临时任务执行和多节点编排 – 包括通过负载平衡器轻松实现零停机滚动更新等操作。

[Ansible 中文权威指南](https://ansible-tran.readthedocs.io/en/latest/)

## 安装

```bash
brew install ansible

#Mac OS X by default is configured for a small number of file handles， so if you want to use 15 or more forks you’ll need to raise the ulimit bellow command. This command can also fix any “Too many open files” error.
sudo launchctl limit maxfiles unlimited
```

## 编排

Ansible 的编排引擎由 Inventory、 API、 Modules (模块)和 Plugins 组成。Ansible 的典型用法是，工程师将需要在远程服务器执行的操作写在 Ansible Playbook 中，然后使用 Ansible 执行 Playbook 中的操作。

使用 Ansible 操作远程服务器时，首先需要确定的是操作哪些服务器，然后再确定对这些服务器执行哪些操作。Ansible 会默认读取`/etc/ansible/hosts`文件中配置的远程服务器列表。

```hosts
[test]
127.0.0.1 ansible_user=test ansible_port=22
```

## 配置文件

Ansible 默认使用 `/etc/ansible/ansible.cfg` 文件，可以在 `ansible.cfg` 中[设定一些默认值](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)，这样就不需要对同样的内容输入多次。

```cfg
[defaults]
remote_port = 22
remote_user = test
inventory = /home/test/hosts
```

[ansible.cfg](https://raw.github.com/ansible/ansible/devel/examples/ansible.cfg)例子。

[ansible-config](https://docs.ansible.com/ansible/latest/cli/ansible-config.html#ansible-config)命令：

```bash
$ ansible-config --version
ansible-config 2.6.4
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/Users/riverside/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/ansible
  executable location = /Users/riverside/bin/ansible-config
  python version = 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
```

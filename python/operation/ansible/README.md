# [Ansible](https://github.com/ansible/ansible)

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

Ansible 默认使用 `/etc/ansible/ansible.cfg` 文件，可以在 `ansible.cfg` 中设定一些默认值，这样就不需要对同样的内容输入多次。

```cfg
[defaults]
remote_port = 22
remote_user = test
inventory = /home/test/hosts
```

## hosts 文件

默认情况下， Ansible 读取`/etc/ansible/hosts`文件中的服务器配置，获取需要操作的服务器列表。

在 Ansible 中，有三种方式指定 hosts 文件，分别是:

- 默认读取 `/etc/ansible/hosts` 文件;
- 通过命令行参数的`-i` 指定 hosts 文件;
- 通过 `ansible.cfg` 文件中的 inventory 选项指定 hosts 文件。

ansible 命令的`--list-hosts`选项用来显示匹配的服务器列表。 `$ ansible test --list-hosts`

在 hosts 文件中定义变量时，使用的是`var= value`格式定义。将变量保存在一个独立的文件时，使用的是`var: value`格式定义。

## Inventory 管理

在 Ansible 中，将可管理的服务器集合称为 Inventory，即服务器管理。

| 名称                         | 默认值          | 描述                               |
| ---------------------------- | --------------- | ---------------------------------- |
| ansible_ssh_host             | 主机的名字      | SSH 目的主机名或 IP                |
| ansible_ssh_port             | 22              | SSH 目的端口                       |
| ansible_ssh_user             | root            | SSH 登录使用的用户名               |
| ansible_ssh_pass             | none            | SSH 认证所使用的密码               |
| ansible_connection           | smart           | ansible 使用何种连接模式连接到主机 |
| ansible_ssh_private_key_file | none            | SSH 认证所使用的私钥               |
| ansible_shell_type           | sh              | 命令所使用的 shell                 |
| ansible_python_interpreter   | /usr/bin/python | 主机上的 python 解释器             |

# 可执行程序

## ansible

command 模块在服务器执行 shell 命令。

```bash
$ ansible test -m command -a "hostname"
```

-a 参数指定模块的参数，Ansible 的模块包含多个参数， 参数使用`key=value`的形式表示，各个参数之间使用空格分隔。

- 将本地文件拷贝到服务器中:`ansible test -m copy a ”src=/tmp/data.txt dest=/tmp/data.txt”`
- 修改文件的所有者和权限:`ansible all -m file -a ”dest=/tmp/data.txt mode=500 owner=root group=root” -become`
- 在远程服务器中安装软件:`ansible test -m apt a ”name=git state=present" become`

command 是 Ansible 中的默认模块，当我们省略-m 参数时，默认使用 command 模块。

## ansible-doc

ansible-doc 命令用于在命令行查看模块列表，也可以使用该工具在命令行获取模块帮助信息。

```bash
ansible -l
```

## ansible-playbook

YAML 文件称为 Ansible Playbook。Playbook 中首先包含了一些声明信息，如 hosts 关键字声明该 Playbook 应用的服务器列表，become 和 become_method 表示在远程服务器通过 sudo 执行操作。Playbook 最后包含了若干个 task， 每一个 task 对应于前面的一条 ad-hoc 命令。具体执行时，多个 task 按序执行。

通过 ansible-playbook 命令执行。`ansible-playbook test_playbook.yml`

## ansible-vault

## ansible-console

## ansible-galaxy

## ansible-pull

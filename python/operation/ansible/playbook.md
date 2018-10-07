# ansible-playbook

YAML 文件称为 Ansible Playbook。Playbook 中首先包含了一些声明信息，如 hosts 关键字声明该 Playbook 应用的服务器列表，become 和 become_method 表示在远程服务器通过 sudo 执行操作。Playbook 最后包含了若干个 task，每一个 task 对应于前面的一条 ad-hoc 命令。具体执行时，多个 task 按序执行。

通过 ansible-playbook 命令执行。`ansible-playbook test_playbook.yml`

在 Ansible 中，一个 Play 必须包含以下两项：

- hosts：需要对哪些远程服务器执行操作；
- tasks：需要在这些服务器上执行的任务列表。

一般只会在 Playbook 中编写一个 Play。

使用 include 组合单一的 paly。

```yaml
- include: db.yml
- include: web.yml
```

## 权限

在 Playbook 的 Play 定义中指定连接远程服务器的用户。

```yaml
- hosts: webservers
  remote_user: root
```

 每个 task 配置用户:

```yaml
tasks:
  - name: test connection
    remote_user: yourname
```

## 控制 hosts 执行顺序

```yaml
- hosts: all
  order: sorted
  gather_facts: False
  tasks:
    - debug:
        var: inventory_hostname
```

- inventory：默认值，按照 inventory 里的顺序执行
- reverse_inventory：与 inventory 相反的顺序
- sorted：字母顺序
- reverse_sorted：反字母顺序
- shuffle：每次随机执行

## 通知

在 Ansible 中，模块是幕等的。

notify 与 handler 机制：通过 notify 选项通知 handler 进行处理。

```yaml
- hosts: webservers
  tasks:
    - name: ensure apache is at the latest version
      yum: name=httpd state=latest

    - name: write the apache config file
      template: src=/srv/httpd.j2 dest=/etc/httpd.conf
      notify:
        - restart apache

    - name: ensure apache is running
      service: name=httpd state=started

  handlers:
    - name: restart apache
      service: name=httpd state=restarted
```

Ansible 官方文档提到 handler 的唯一用途，就是重启服务与服务器。

## 变量

最直接的方式是将变量定义在 Playbook 的 vars 选项中。

```yaml
- hosts: dbservers
  vars:
    mysql_port: 80
```

引用变量:`port={{ mysql_port }}`

当变量较多时，变量保存在一个独立的文件中，并通过 `vars_files`选项引用该文件。

```yaml
- hosts: dbservers
  vars:
    mysql_port: 80
  vars_files:
    - /vars/external_vars.yml
```

保存变量的文件是一个简单的 YAML 格式的字典。

获取任务的执行结果，将任务的执行结果保存在一个变量中，之后引用这个变量。这样的变量在 Ansible 中使用 register 选项获取，也称为注册变量。

## Facts 变量

Facts 变量是 Ansible 执行远程部署之前从远程服务器中获取的系统信息，包括服务器的名称、IP 地址、操作系统、分区信息、硬件信息等。Facts 变量可以配合 Playbook 实现更加个性化的功能需求。

通过 setup 模块查看 Facts 变量的列表（本机 ip)：

```bash
ansible 127.0.0.1 -m setup
```

通过 gather_facts 选项控制是否收取远程服务器的信息。默认为 yes

```yaml
---
- hosts: dbservers
  gather_facts: no
  tasks:
```

## 循环

```yaml
- name: 工nstall Mysql package
  yum: name={{item}} state=installed
  with items:
    - mysql-server
    - MySQL-python
    - libselinux-python
    - libsemanage-python
```

## 条件

在 Playbook 中可以通过 when 选项执行条件语句。

## 任务执行策略

Ansible 支持名为 free 的任务执行策略，允许执行较快的远程服务器提前完成 Play 的部署， 不用等待其他远程服务器一起执行 task。

## 线性更新服务器

Ansible 为了提高部署的效率，默认使用并发的方式对远程服务器进行更新。我们可以使用`--forks`参数控制并发的进程数，默认并发进程数为 5。在更新线上服务器时应该循序渐进地进行更新，以此达到降低对线上服务影响的目的。如果服务器数量较少，可以逐台更新；如果服务器数量较多，则渐进式更新。

为了实现线性更新，我们可以使用 Ansible Playbook 的 serial 选项。该选项可以取值为一个数字，表示一次更新多少台服务器；也可以取值为一个百分 比，表示一次更新多少比例的服务器；还可以取值为一个数字或百分比的列表，实现渐进式更新。

## 任务委派功能

对服务器进行批量操作的过程中需要对其中某一台服务器进行特殊处理。此时，需要使用 Ansible 的任务委派功能。`delegate_to: 127.0.0.1`

## 控制服务器执行操作

使用 delegate_to 功能将任务委派到本地执行。除此之外，Ansible 还提供了 local_action 选项明确指定在控制服务器执行操作。

## run_once 保证任务仅执行一次

默认情况下，Ansible 会选择在组中的第一台服务器中执行`run_once`操作。

## 使用标签灵活控制 Play 的执行

在 Ansible 中，可以通过 tags 选项实现这个功能。

使用 tags 为每一个任务打上了一个标签 。使用 ansible-playbook 的`一skip-tags`选项与`一tags`选项指定需要执行的 task 或者需要跳过的 task。

## 使用 changed_when 控制对 changed 字段的定义

当 Shell 命令或模块运行时 它们往往会根据自己的判断报告是否对远程服务器进行了修改，然后通过返回值中的“changed” 字段返回给我们。

## 使用 failed_when 控制对 failed 宇段的定义

通过自定义的方式判断命令是否执行成功。

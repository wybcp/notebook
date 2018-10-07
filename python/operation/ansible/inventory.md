# [inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)

在 Ansible 中，将可管理的服务器集合称为 Inventory，即服务器管理。

| 名称                       | 默认值           | 描述                                                     |
| -------------------------- | ---------------- | -------------------------------------------------------- |
| ansible_host               | 主机的名字       | SSH 目的主机名或 IP                                      |
| ansible_port               | 22               | SSH 目的端口                                             |
| ansible_user               | root             | SSH 登录使用的用户名                                     |
| ansible_ssh_pass           | none             | SSH 认证所使用的密码                                     |
| ansible_connection         | smart            | ansible 使用何种连接模式连接到主机 ,smart、ssh、paramiko |
| ansible_private_key_file   | none             | SSH 认证所使用的私钥                                     |
| ansible_shell_type         | sh               | 命令所使用的 shell                                       |
| ansible_python_interpreter | /usr/bin/python3 | 主机上的 python 解释器                                   |

## hosts 文件

默认情况下， Ansible 读取`/etc/ansible/hosts`文件中的服务器配置，获取需要操作的服务器列表。

在 Ansible 中，有三种方式指定 hosts 文件，分别是:

- 默认读取 `/etc/ansible/hosts` 文件;
- 通过命令行参数的`-i <path>` 指定 hosts 文件;
- 通过 `ansible.cfg` 文件中的 inventory 选项指定 hosts 文件。

ansible 命令的`--list-hosts`选项用来显示匹配的服务器列表。 `$ ansible test --list-hosts`

在 hosts 文件中定义变量时，使用的是`var= value`格式定义。将变量保存在一个独立的文件时，使用的是`var: value`格式定义。

### 匹配模式

- 数字模式:

  ```hosts
  [webservers]
  www[01:50].example.com
  ```

- 字母范围:

  ```hosts
  [databases]
  db-[a:f].example.com
  ```

- 每一个 host 指定连接方式和用户:

  ```hosts
  [targets]

  localhost              ansible_connection=local
  other1.example.com     ansible_connection=ssh        ansible_user=mpdehaan
  other2.example.com     ansible_connection=ssh        ansible_user=mdehaan
  ```

### 分组

默认分组：

- `all`：所有的 host
- `ungrouped`：all 分组里面没有特定分组的 host

## host 和分组变量分离

变量文件是 YAML 格式。

```
/etc/ansible/hosts
/etc/ansible/group_vars/webservers
/etc/ansible/host_vars/foosball
```

Ansible 直接读取相对应的文件生成字典。

## python3

[python3](https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html)支持。

```hosts
# Example inventory that makes an alias for localhost that uses Python3
localhost-py3 ansible_host=localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3

# Example of setting a group of hosts to use Python3
[ubuntu16]
127.0.0.1

[py3-hosts]
ubuntu16

[py3-hosts:vars]
ansible_python_interpreter=/usr/bin/python3
```

运行时指定 python 解释器：
`$ ansible-playbook sample-playbook.yml -e 'ansible_python_interpreter=/usr/bin/python3'`

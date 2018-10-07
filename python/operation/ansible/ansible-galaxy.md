# ansible-galaxy

role 并不是某一个具体的东西，而是一个规范与抽象，是一种将复杂的 Playbook 分割成多个文件的机制，它大大简化了复杂 Playbook 的编写，使得 Playbook 复用变得简单。

利用 ansible-galaxy 快速地创建一个标准的 roles 目录结构，还可以通过它在<galaxy.ansible.com>上下载别人写好的 roles。

ansible-galaxy 的简单用法:

1. 初始化一个 roles 的目录结构:

   `ansible-galaxy init /etc/ansible/roles/websrvs`

2. 安装别人写好的 roles:

   ```bash
   ansible-galaxy install -p /etc/ansible/roles bennojoy.mysql
   #安装到指定目录
   ansible-galaxy -p ./roles install bennojoy.ntp
   ```

3. 列出已安装的 roles:

   `ansible-galaxy list`

4. 查看已安装 的 roles 信息:

   `ansible-galaxy info bennojoy.mysql`

5. 卸载 roles:

   `ansible-galaxy remove bennojoy.mysql`

## role 的目录结构

每个文件夹包含一个`main.yml`文件。

- `tasks` - contains the main list of tasks to be executed by the role.
- `handlers` - contains handlers, which may be used by this role or even anywhere outside this role.
- `defaults` - default variables for the role (see [Variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html) for more information).
- `vars` - other variables for the role (see [Variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html) for more information).
- `files` - contains files which can be deployed via this role.
- `templates` - contains templates which can be deployed via this role.
- `meta` - defines some meta data for this role.

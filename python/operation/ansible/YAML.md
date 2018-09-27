# YAML 语法

对于 Ansible，每一个 YAML 文件都是从一个列表开始。列表中的每一项都是一个键值对， 通常它们被称为一个 "哈希" 或 "字典"。

所有的 YAML 文件(无论和 Ansible 有没有关系)开始行都应该是 `---`。 这是 YAML 格式的一部分，表明一个文件的开始。

列表中的所有成员都开始于相同的缩进级别， 并且使用一个 `"- "` 作为开头(一个横杠和一个空格)：

- 数组

        ---
        # 一个美味水果的列表
        - Apple
        - Orange
        - Strawberry
        - Mango

一个字典是由一个简单的 `键: 值` 的形式组成(这个冒号后面必须是一个空格)：

- 对象

        ---
        # 一位职工的记录
        name: Example Developer
        job: Developer
        skill: Elite

通过以下格式来指定一个布尔值(true/fase)::

- 纯量(scalars)

        ---
        create_key: yes
        needs_agent: no
        knows_oop: True
        likes_emacs: TRUE
        uses_cvs: false

尽管 YAML 通常是友好的， 但是下面将会导致一个 YAML 语法错误：

    foo: somebody said I should put a colon here: so I did

你需要使用引号来包裹任何包含冒号的哈希值， 像这样：

    foo: "somebody said I should put a colon here: so I did"

然后这个冒号将会被结尾。

此外， Ansible 使用 "{{ var }}" 来引用变量。 如果一个值以 "{" 开头， YAML 将认为它是一个字典， 所以我们必须引用它，像这样：

    foo: "{{ variable }}"
# pip

包管理工具

## 常见命令

- `pip install django`: Install packages.`pip install -r requirements.txt`从 requirements 文件安装
- `pip download django`: Download packages.
- `pip uninstall django`: Uninstall packages.
- `pip freeze > requirements.txt`: Output installed packages in requirements format.
- `pip list`: List installed packages.
- `pip show django`: Show information about installed packages.
- `pip check django`: Verify installed packages have compatible dependencies.
- `pip config django`: Manage local and global configuration.
- `pip search django`: Search PyPI for packages.
- `pip wheel django`: Build wheels from your requirements.
- `pip hash django`: Compute hashes of package archives.
- `pip completion django`: A helper command used for command completion.
- `pip help django`: Show help for commands.

## mirror

阿里云镜像下载

- 临时下载：

    ```bash
    pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy
    ```

- 永久修改：

    ```bash
    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
    ```

修改 pip 的配置文件，将镜像源写入配置文件中 。

```bash
⚡ cat ~/.pip/pip.conf
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host = mirrors.aliyun.com
```

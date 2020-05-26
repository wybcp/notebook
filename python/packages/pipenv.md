# pipenv

Pipenv 是 Python 项目的依赖管理器。尽管 pip 可以安装 Python 包，但仍推荐使用 Pipenv，因为它是一种更高级的工具，可简化依赖关系管理的常见使用情况。

[使用 pip 来安装 Pipenv](https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html#virtualenvironments-ref)：

```bash
pip install --user pipenv
```

Pipenv 管理每个项目的依赖关系。要安装软件包时，请更改到您的项目目录并运行。

使用 `$ pipenv run` 可确保您的安装包可用于您的脚本。

```bash
pipenv run python main.py
```

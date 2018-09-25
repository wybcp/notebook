# zipfile

## 读取 zip

- namelist: 返回 zip 文件中包含的所有文件和文件夹的字符串列表;
- extract: 从 zip 文件中提取单个文件;
- extractall:从 zip 文件中提取所有文件。

```python
import zipfile
example_zip = zipfile.ZipFile(’example.zip’)
example_zip .namelist()
```

## 创建 zip

创建一个 zip 格式的压缩文件，必须以写模式打开 zip 文件，通过 write 方法来添加文件的。

```python
import zipfile
newZip = zipfile.ZipFile ('new.zip '，'w' )
newZip . write ( ’spam.txt’ )
newZip .close ()
```

## 使用 Python 的命令行工具

- -l:显示 zip 格式压缩包中的文件列表
- -c:创建 zip 格式压缩包
- -e: 提取 zip 格式压缩包
- -t: 验证文件是一个有效的 zip 格式压缩包

```bash
python -m zipfile -c monty.zip spam.txt eggs.txt
python -mzipfile -e monty.zip target-dir/
python -m zipfile -1 monty.zip
```

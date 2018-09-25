# shutil 处理文件夹

shutil(或称为 shell 工具)模块中包含一些函数，让你在 Python 程序中复制、移动、改名和删除文件。

shutil.copy(source, destination)，将路径 source 处的文件复制到路径 destination 处的文件夹(source 和 destination 都是字符串)。如果 destination 是一个文件名，它将作为被复制文件的新名字。该函数返回一个字符串，表示被复制文件的路径。

shutil.copytree(source, destination)，将路径 source 处的文件夹，包括它的所有文件和子文件夹，复制到路径 destination 处的文件夹。source 和 destination 参数都是字符串。该函数返回一个字符串，是新复制的文件夹的路径。

shutil.move(source, destination)，将路径 source 处的文件夹移动到路径 destination，并返回新位置的绝对路径的字符串。如果 destination 指向一个文件夹，source 文件将移动到 destination 中，并保持 原来的文件名。

- 用 os.unlink(path)将删除 path 处的文件。
- 调用 os.rmdir(path)将删除 path 处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹。
- 调用 shutil.rmtree(path)将删除 path 处的文件夹，它包含的所有文件和文件夹都会被删除，不可恢复地删除文件和文件夹。
- send2trash.send2trash()函数来删除文件和文件夹，发送到计算机的垃圾箱或回收站，而不是永久删除它们。

## 压缩文件处理

```python
import shutil

print(shutil.get_archive_formats())

# [('bztar', "bzip2'ed tar-file"),
#  ('gztar', "gzip'ed tar-file"),
#  ('tar', 'uncompressed tar file'),
#  ('xztar', "xz'ed tar-file"),
#  ('zip', 'ZIP file')]
```

### 创建压缩包

    shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)

    Docstring:
    Create an archive file (eg. zip or tar).

    'base_name' is the name of the file to create, minus any format-specific
    extension; 'format' is the archive format: one of "zip", "tar", "gztar",
    "bztar", or "xztar".  Or any other registered format.

    'root_dir' is a directory that will be the root directory of the
    archive; ie. we typically chdir into 'root_dir' before creating the
    archive.  'base_dir' is the directory where we start archiving from;
    ie. 'base_dir' will be the common prefix of all files and
    directories in the archive.  'root_dir' and 'base_dir' both default
    to the current directory.  Returns the name of the archive file.

    'owner' and 'group' are used when creating a tar archive. By default,
    uses the current owner and group.

### 读取压缩包

    shutil.unpack_archive(filename, extract_dir=None, format=None)
    Docstring:
    Unpack an archive.

    `filename` is the name of the archive.

    `extract_dir` is the name of the target directory, where the archive
    is unpacked. If not provided, the current working directory is used.

    `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
    or "xztar".  Or any other registered format.  If not provided,
    unpack_archive will use the filename extension and see if an unpacker
    was registered for that extension.

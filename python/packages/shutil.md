# shutil 处理文件夹

shutil(或称为 shell 工具)模块中包含一些函数，让你在 Python 程序中复制、移动、改名和删除文件。

shutil.copy(source, destination)，将路径 source 处的文件复制到路径 destination 处的文件夹(source 和 destination 都是字符串)。如果 destination 是一个文件名，它将作为被复制文件的新名字。该函数返回一个字符串，表示被复制文件的路径。

shutil.copytree(source, destination)，将路径 source 处的文件夹，包括它的所有文件和子文件夹，复制到路径 destination 处的文件夹。source 和 destination 参数都是字符串。该函数返回一个字符串，是新复制的文件夹的路径。

shutil.move(source, destination)，将路径 source 处的文件夹移动到路径 destination，并返回新位置的绝对路径的字符串。如果 destination 指向一个文件夹，source 文件将移动到 destination 中，并保持 原来的文件名。

- 用 os.unlink(path)将删除 path 处的文件。
- 调用 os.rmdir(path)将删除 path 处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹。
- 调用 shutil.rmtree(path)将删除 path 处的文件夹，它包含的所有文件和文件夹都会被删除，不可恢复地删除文件和文件夹。
- send2trash.send2trash()函数来删除文件和文件夹，发送到计算机的垃圾箱或回收站，而不是永久删除它们。

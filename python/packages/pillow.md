# pillow 图片处理

PIL (Python Imaging Library)是 Python 生态中最有名的图片处理相关库。

```bash
pip install Pillow
```

## Image 类

```python
In [4]: from PIL import Image

In [5]: example_image=Image.open('example.jpg')
```

Exif (Exchangeable image file format)是可交换图像文件格式的简称，可以记录照片的属性信息和拍摄数据 。

PIL.Exiffags.TAGS 和 PIL.Exiffags.GPSTAGS 这两个字典。 这两个字典的键是 16 位整数的 Exif 标签，值是 Exif 标签的描述字符串。

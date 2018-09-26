# Python-nmap

Python-nmap 是对 nmap 的封装。 Python-nmap 相对于 nmap, 主要的改进在于对输出结果的处理。Python-nmap 将 nmap 的输出结果保存到字典之中，我们只需要通过 Python 的字典就可以获取到 nmap 的输出信息。

```bash
pip install python-nmap
```

```python
In [1]: import nmap

In [2]: nm=nmap.PortScanner()

In [3]: nm.scan('10.166.224.14,140','22-1000')
Out[3]:
{'nmap': {'command_line': 'nmap -oX - -p 22-1000 -sV 10.166.224.14,140',
  'scaninfo': {'tcp': {'method': 'connect', 'services': '22-1000'}},
  'scanstats': {'timestr': 'Wed Sep 26 16:22:54 2018',
   'elapsed': '3.37',
   'uphosts': '0',
   'downhosts': '2',
   'totalhosts': '2'}},
 'scan': {}}
 ```
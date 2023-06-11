from collections import OrderedDict
d = OrderedDict([("b", 2), ("a", 1), ("c", 3)])
for k, v in d.items():
  print(k, v)
  
# 以下语句在python2中可能不按照添加的顺序打印
d = dict([("b", 2), ("a", 1), ("c", 3)])
for k, v in d.items():
  print(k, v)

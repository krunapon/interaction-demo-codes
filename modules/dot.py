import re

str = "hello world"

x1 = re.findall("he..o", str)
print(x1)

x2 = re.findall("w.l", str)
print(x2)

x3 = re.findall(".l", str)
print(x3)

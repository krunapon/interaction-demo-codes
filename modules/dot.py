import re

str = "hello world"

# Search for a sequence that starts with "he",
# followed by two (any) characters, and an "o":

x1 = re.findall("he..o", str)
print(x1)

x2 = re.findall("w.l", str)
print(x2)

x3 = re.findall(".l", str)
print(x3)

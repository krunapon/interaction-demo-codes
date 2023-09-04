import re

str1 = "hello world"
str2 = "please say hello"

#Check if the string starts with 'hello':
x1 = re.findall("^hello", str1)
if (x1):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x2 = re.findall("^hello", str2)
if (x2):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

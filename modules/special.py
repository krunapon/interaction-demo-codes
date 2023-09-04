import re

str = "This is 59 dollars"

#Find all digit characters:
x1 = re.findall("\d", str)
print(x1)

#Find anything that is not digit characters
x2 = re.findall("\D", str)
print(x2)

#Find anything that is alphanumeric characters
x3 = re.findall("\w", str)
print(x3)


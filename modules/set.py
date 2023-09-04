import re

str = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "h":
x1 = re.findall("[a-h]", str)
print(x1)

#Find only a and r
x2 = re.findall("[ar]", str)
print(x2)

#Find any characters that are not between "a" and "z"
x3 = re.findall("[^a-z]",str)
print(x3)


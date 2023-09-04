import re
str = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x1 = re.findall("falls|stays", str)
print(x1)
if (x1):
  print("Yes, there is at least one match!")
else:
  print("No match")

x2 = re.findall("Rain|Pain", str)
if (x2):
  print("Yes, there is at least one match!")
else:
  print("No match")

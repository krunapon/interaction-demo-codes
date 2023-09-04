import re

str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x1 = re.findall("p(.*)ly", str)
print(x1)
if (x1):
  print("Yes, there is at least one match!")
else:
  print("No match")

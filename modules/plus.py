import re
str = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 1 or more "x" characters:
x1 = re.findall("aix+", str)
print(x1)
if (x1):
  print("Yes, there is at least one match!")
else:
  print("No match")
x2 = re.findall("ain+", str)
print(x2)
if (x2):
  print("Yes, there is at least one match!")
else:
  print("No match")

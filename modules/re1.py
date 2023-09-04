import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print("x is {}".format(x))
if x:
    print("Match")
else:
    print("Does not match")

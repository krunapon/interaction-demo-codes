import re
# Open file
f = open('test.txt', 'r')
print(f.read())
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
print(strings)

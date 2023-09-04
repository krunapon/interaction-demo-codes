import re
s = 'Hi\nHello'
print(s)
raw_s = r'Hi\nHello'
print(raw_s)

string = '\n and \r are escape sequences.'
result1 = re.findall(r'[\n\r]', string)
print(result1)

result2 = re.findall('\n\r', string)
print(result2)


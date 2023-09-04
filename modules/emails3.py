import re
str = 'purple alice-b@google.com monkey dishwasher'
str2 = "manee@kku.ac.th"
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group()) ## 'alice-b@google.com'
match = re.search(r'[\w.-]+@[\w.-]+', str2)
if match:
    print(match.group()) ## 'alice-b@google.com'

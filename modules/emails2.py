import re
str1 = 'purple alice-b@google.com monkey dishwasher'
str2 = "kanda@kku.ac.th"
match1 = re.search(r'\w+@\w+.[^\s]+', str1)
if match1:
    print(match1.group())  ## 'b@google.com'
match2 = re.search(r'\w+@\w+.[^\s]+', str2)
if match2:
    print(match2.group())

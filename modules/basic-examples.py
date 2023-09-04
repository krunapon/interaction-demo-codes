import re
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
print(re.search(r'iii', 'piiig').group()) # found, match.group() == "iii"
print(re.search(r'igs', 'piiig')) # not found, match == None

## . = any char but \n
print(re.search(r'..g', 'piiig').group()) # found, match.group() == "iig"

## \d = digit char, \w = word char
print(re.search(r'\d\d\d', 'p123g').group()) # found, match.group() == "123"
print(re.search(r'\w\w\w', '@@abcd!!').group()) # found, match.group() == "abc"

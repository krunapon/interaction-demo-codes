import re
## i+ = one or more i's, as many as possible.
print(re.search(r'pi+', 'piiig').group()) # found, match.group() == "piii"
## In this example, note that it does not get to the second set of i's.
print(re.search(r'i+', 'piigiiii').group()) # found, match.group() == "ii"
## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
# found, match.group() == "1 2   3"
print(re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx').group())
# found, match.group() == "12  3"
print(re.search(r'\d\s*\d\s*\d', 'xx12  3xx').group())
print(re.search(r'\d\s*\d\s*\d', 'xx123xx').group()) # found, match.group() == "123"
## ^ = matches the start of string, so this fails:
print(re.search(r'^b\w+', 'foobar')) # not found, match == None
## but without the ^ it succeeds:
print(re.search(r'b\w+', 'foobar').group()) # found, match.group() == "bar"



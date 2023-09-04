import re

# this will match
print(re.match("c.*t", "cravat"))

# this won't
print(re.match("c.*t", "I have a cravat"))

# this will
print(re.search("c.*t", "I have a cravat"))

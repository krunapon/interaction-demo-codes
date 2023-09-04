import re

# We can use a static string as a replacement...
print(re.sub("lamb", "squirrel", "Mary had a little lamb."))

# Or we can capture groups, and substitute their contents back in.
print(re.sub("(.*) (BITES) (.*)", r"\3 \2 \1", "DOG BITES MAN"))

# count is a keyword parameter which we can use to limit replacements
print(re.sub("a", "b", "aaaaaaaaaa"))
print(re.sub("a", "b", "aaaaaaaaaa", count=1))

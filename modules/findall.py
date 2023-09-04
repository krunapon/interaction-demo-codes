import re
# Sometimes we want to find all the matches in a string.
print(re.findall("[^ ]+@[^ ]+", "Bob <bob@example.com>, "
                                "Jane <jane.doe@example.com>"))


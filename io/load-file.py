import json
with open('dump.txt', 'r') as f:
    x = json.load(f)
    print("{} is {} years old.".format(x["name"], x["age"]))


import json
with open('hobbies.txt', 'r') as f:
    x = json.load(f)
    print("{} has hobbies as {}".format(x["firstName"],
                                      (", ").join(x["hobbies"])))





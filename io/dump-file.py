import json
with open('dump.txt', 'w') as f:
    x = {'name':"manee", 'age':25}
    json.dump(x,f)

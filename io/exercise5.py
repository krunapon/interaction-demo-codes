import json
with open('hobbies.json', 'w') as f:
    x = { "firstName": "Jane", "lastName": "Doe",
          "hobbies": ["running", "sky diving", "singing"]}
    json.dump(x,f)





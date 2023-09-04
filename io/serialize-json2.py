import json
data = {
    "president": {
	"name": "Xi Jinping",
	"country": "China"
     }
}

json_string = json.dumps(data)

print(f"string is {json_string}")


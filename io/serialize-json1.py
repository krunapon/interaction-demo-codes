import json
data = {
    "president": {
	"name": "Xi Jinping",
	"country": "China"
     }
}
with open("data_file.json", "w") as write_file:
     json.dump(data, write_file)

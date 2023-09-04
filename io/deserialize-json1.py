import json
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(f"data is {data}")
    president = data["president"]
    print(f"president is {president}")
    country = president["country"]
    print(f"country is {country}")

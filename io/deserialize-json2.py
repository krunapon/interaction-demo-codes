import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos1 = json.loads(response.text)
title1 = todos1[0]['title'] 
print(f'title[0] is {title1}')
todos2 = response.json()
completed4 = todos2[3]['completed']
print(f'completed[3] is {completed4}')

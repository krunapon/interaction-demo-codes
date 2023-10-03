import re

str = "1: KKU 2: Khon Kaen University"
search_result = re.split(":", str)
print(search_result)
name1_str = search_result[1]
name1 = re.search("[a-zA-Z]+", name1_str)
name2 = re.search("[a-zA-Z].+", search_result[2])
print(f"The first name is {name1.group()}")
print(f"The second name is {name2.group()}")
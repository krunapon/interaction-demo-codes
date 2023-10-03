import re

str = "The rain in Spain"

search_result = re.search("[a-h]", str)
print(search_result)

findall_result = re.findall('[a-h]', str)
print(findall_result)

split_result = re.split('[a-h]', str)
print(split_result)
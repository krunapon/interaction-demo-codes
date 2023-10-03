import re

str = "This is 109 Baht"

search_result = re.search("\d{3}", str)
print(f"search_result has match with the string {search_result.group()}")

findall_result = re.findall("\s", str)
print(findall_result)

split_result = re.split("\W",str)
print(split_result)
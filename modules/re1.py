import re

full_txt = "The rain in Spain"
search_pattern = "^Spain"
search_result = re.search(search_pattern, full_txt)
print(f"The search result is ${search_result}")
if search_result:
    print("Search is matched")
else:
    print("Search is not matched")
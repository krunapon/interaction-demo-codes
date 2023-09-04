from functools import reduce
list = [47, 11, 42, 13]
add_list = reduce(lambda x,y: x+y, list)
print(add_list)
greater = lambda a,b: a if (a > b) else b
max_list = reduce(greater, list)
print(max_list)

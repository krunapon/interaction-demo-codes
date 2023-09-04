# using format() method 
print('I love {} and {}'.format('Mom', 'Dad'))

# using format() method and refering
# a position of the object
print('{1} and {0}'.format('Dad', 'Mom'))

print("Second argument: {1:3d}, first one: {0:7.2f}".
	format(47.42, 11))


print("a = {a:5d}, b = {b:8.2f}".
	format(a = 453, b = 59.058))

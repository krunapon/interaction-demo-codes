# we need to import the module in order to use it
import itertools

# unlike range, count doesn't have an upper bound, and is not restricted to integers
for i in itertools.count(1):
    print(i) # 1, 2, 3....
    if i == 3:
	    break

for i in itertools.count(1, 0.5):
    print(i) # 1.0, 1.5, 2.0....
    if i == 2.5:
	    break

# cycle repeats the values in another iterable over and over
i = 0
for animal in itertools.cycle(['cat', 'dog']):
    print(animal) # 'cat', 'dog', 'cat', 'dog'...
    i = i + 1
    if (i == 2):
	    break

# repeat repeats a single item
count = 0
for i in itertools.repeat(1): # ...forever
    print(i) # 1, 1, 1....
    count = count + 1
    if (count == 3):
	    break


for i in itertools.repeat(2, 3): # or a set number of times
    print(i) # 2, 2, 2

numbers = range(1,5)
animals = ['cat', 'dog'] 
# chain combines multiple iterables sequentially
for i in itertools.chain(numbers, animals):
    print(i) # print all the numbers and then all the animals

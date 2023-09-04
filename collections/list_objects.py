numbers = [1, 2, 3, 4, 5]
# we already saw how to add an element to the end
numbers.append(5)
print(numbers)
# count how many times a value appears in the list
numbers.count(5)
print(numbers.count(5))
# append several values at once to the end
numbers.extend([56, 2, 12])
print(numbers)
# find the index of a value
print(numbers.index(3))
# if the value appears more than once, we will get the index of the first one
print(numbers.index(2))
# insert a value at a particular index
numbers.insert(0, 45) # insert 45 at the beginning of the list
print(numbers)
# remove an element by its index and assign it to a variable
my_number = numbers.pop(0)
print(my_number)
# remove an element by its value
numbers.remove(12)
# if the value appears more than once, only the first one will be removed
numbers.remove(5)
print(numbers)

numbers = [1, 5, 2, 12, 14, 7, 18]

# a generator comprehension
doubles_generator = (2 * number for number in numbers)
print("double generator is " + str(doubles_generator))
print("sum doubles is " + str(sum(2 * number for number in numbers)))

# a set comprehension
doubles_set = {2 * number for number in numbers}
print("double set is " + str(doubles_set))

# a dict comprehension which uses the number as the key and the doubled number as the value
doubles_dict = {number: 2 * number for number in numbers}
print("double dict is " + str(doubles_dict))

numbers = [8, 11, 20, 21, 22]
odd_numbers = filter(lambda x: x % 2, numbers)
print(odd_numbers)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)

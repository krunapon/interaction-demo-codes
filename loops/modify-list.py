numbers = [1, 5, 2, 12, 14, 7, 18]

print("numbers are " + str(numbers))
doubles = []
for number in numbers:
    doubles.append(2 * number)
print("doubles are " + str(doubles))

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print("even numbers are " + str(even_numbers))

animals = ['aardvark', 'cat', 'dog', 'opossum']
vowel_animals = []
for animal in animals:
    if animal[0] in 'aeiou':
        vowel_animals.append(animal.title())
print("vowel animals are " + str(vowel_animals))

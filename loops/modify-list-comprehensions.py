numbers = [1, 5, 2, 12, 14, 7, 18]
print("numbers are " + str(numbers))

doubles = [2 * number for number in numbers]
print("doubles are " + str(doubles))

even_numbers = [number for number in numbers if number % 2 == 0]
print("even numbers are " + str(even_numbers))

animals = ['aardvark', 'cat', 'dog', 'opossum']
vowel_animals = [animal.title() for animal in animals if animal[0] in 'aeiou']
print("vowel animals are " + str(vowel_animals))

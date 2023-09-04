# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# a class method to create a Person object by birth year.

	def print(self):
		print(f'{self.name} is {self.age}')

	@classmethod
	def from_birth_year(cls, name, year):
		return cls(name, date.today().year - year)
	# a static method to check if a Person is adult or not.

	@staticmethod
	def is_adult(age):
		return age > 18


manee = Person('Manee', 17)
manee.print()
mana = Person.from_birth_year('Mana', 1996)
manee.from_birth_year('Chujai', 2008)
print("Mana is {} years old.".format(mana.age))
print("Manee is {} years old.".format(manee.age))
manee.is_adult(mana.age)
if Person.is_adult(manee.age):
    print("{} is an adult".format(manee.name))
else:
    print("{} is NOT an adult".format(manee.name))


class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def info(self):
		print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

	def make_sound(self):
		print("Meow")


class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def info(self):
		print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

	def make_sound(self):
		print("Bark")


if __name__ == "__main__":
	cat1 = Cat("Kitty", 2.5)
	dog1 = Dog("Thongdee", 4)

	for pet in (cat1, dog1):
		pet.info()
		pet.make_sound()

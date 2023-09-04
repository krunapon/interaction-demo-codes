class Dog:

    # class attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Access class 
print(f"species of Dog is {Dog.species}")



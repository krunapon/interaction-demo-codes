class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog objects
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Print name and age of each dog
print(f"{philo.name} is {philo.age} years old")
print(f"{mikey.name} is {mikey.age} years old")

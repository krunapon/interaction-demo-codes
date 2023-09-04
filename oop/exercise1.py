class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
john = Dog("John", 7)


def get_biggest_number(*args):
    return max(args)


oldest = get_biggest_number(philo.age, mikey.age, john.age)

print("The oldest dog is {} years old.".format(oldest))

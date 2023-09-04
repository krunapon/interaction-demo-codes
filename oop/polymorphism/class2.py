class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


if __name__ == "__main__":
    cat1 = Cat("Kitty", 2.5)
    dog1 = Dog("Thongdee", 4)
    pets = [cat1, dog1]
    for pet in pets:
        pet.info()
        pet.make_sound()


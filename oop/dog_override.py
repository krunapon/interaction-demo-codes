# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class CuteDog(Dog):
    def speak(self, sound):
        return "{} says {} quietly".format(self.name, sound)


george = CuteDog("George", 12)
print(george.speak("bark"))

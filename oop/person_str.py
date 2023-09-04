class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

    def __str__(self):
        return self.name + "'s age is: " + str(self.age)

class Student(Person):
    def display(self):
        print("I am a student whose name is " + self.name)

    def register(self, course):
        print("I register for course " + course)


manee = Student('Manee', 18)
manee.display()
manee.register("EN842004")
print(manee)



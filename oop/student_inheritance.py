# parent class
class Person:
    def __init__(self,name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def description(self):
        print("Person name is {}".format(self.__name))


# child class
class Student(Person):
    university = "KKU"

    def __init__(self, name, gpa):
        # call super() function
        self.__name = name
        self.__gpa = gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def description(self):
        print("Student name is {} and gpa is {}".format(self.__name, self.__gpa))


manee = Person("Manee")
chujai = Student("Chujai", 3.2)
manee.description()
manee.name = "Mana"
manee.description()
manee.set_name("Mana")
manee.description()
chujai.description()
chujai.set_gpa(3.5)
chujai.description()

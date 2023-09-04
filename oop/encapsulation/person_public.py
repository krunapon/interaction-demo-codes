class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
 
    def display(self):
        print(self.name)
        print(self.age)
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
print(person.age)

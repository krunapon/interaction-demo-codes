class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_salary(self):
        print("Salary is unknown")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def show_salary(self):
        print("Salary is", self.salary)

if __name__ == "__main__":
    p = Person("Manee", 23)
    x = Employee("Mana", 20, 100000)
    p.show_salary() # Salary is unknown
    x.show_salary() # Salary is 100000

# class Person:
#   def _protected_method(self):
#       print("protected method")
#   def __private_method(self):
#      print("privated method")
#if __name__ == "__main__":
#   p = Person("Manee", 23)
#   p._protected_method() # shows a warning
#   p.__private_method()  # throws Attribute error saying no such method exists

# Single level inheritance
#class Employee(Person):
# def __init__(self):
#   pass

# Multi-level inheritance
#class Manager(Employee):
# def __init__(self):
#    pass

# Multiple Inheritance
#class Enterprenaur(Person, Employee):
#  def __init__(self):
#   pass

#if __name__ == "__main__":
#   p = Person("Manee", 23)
#   print(p.name)

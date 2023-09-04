from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def geeks(self):
        return "parent class"


class Child(Parent):
    def geeks(self):
        return "child class"


try:
    r = Parent()
    print(r.geeks)
except Exception as err:
    print(err)

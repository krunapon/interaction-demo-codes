# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod


class Super1(ABC):
    def method1(self):
        print("Abstract Base Class")


class Subclass(Super1):
    def method1(self):
        super().method1()
        print("subclass ")


# Driver code
subclass1 = Subclass()
subclass1.method1()

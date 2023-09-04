import abc


class Parent:
    def geeks(self):
        pass


class Child(Parent):
    def geeks(self):
        print("child class")


# Driver code
print(issubclass(Child, Parent))
print(isinstance(Child(), Parent))

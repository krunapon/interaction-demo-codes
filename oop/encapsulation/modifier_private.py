class Modifiers:

    def __init__(self, name):
        self.__private_member = name  # Private Attribute

m = Modifiers("SKAUL05")
print(m.__private_member)

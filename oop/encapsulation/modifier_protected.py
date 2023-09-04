class Modifiers:

    def __init__(self,name):
        self._protected_member = name # Protected Attribute


m = Modifiers("KKU")
print(m._protected_member)

class Modifiers:

    def __init__(self,name):
        self.public_member = name

mod = Modifiers("KKU")
print(mod.public_member) #Accessing the Public Attribute of Modifier Class
mod.public_member = "Github" #Changing it's value
print(mod.public_member)

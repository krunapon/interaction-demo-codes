class Person(object):
    gender = "Unknown"
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def print(self):
        print("Name is {} Nationality is {} Gender is {}".
              format(self.name, self.nationality, self.gender))

class Male(Person):
    gender = "Male"

class Female(Person):
    gender = "Female"


piti = Person("Piti", "Chinese")
manee = Female("Manee", "Thai")
mana = Male("Mana", "Japanese")
piti.print()
manee.print()
mana.print()

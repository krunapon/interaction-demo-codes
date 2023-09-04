class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname

# but we can also access it from the class
print(Person.TITLES[1])

# we can access a class attribute from an instance
person = Person("Mrs", "Manee", "Deejai")
print(person.TITLES[0])



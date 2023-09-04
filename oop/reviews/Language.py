class Language:
    language_list = []

    def __init__(self, name, type):
        self.name = name
        self.type = type
        Language.language_list.append(self)

    def display(self):
        print("Language name is {} and type is {}"
              .format(self.name, self.type))

    def remove(self):
        Language.language_list.remove(self)

    @classmethod
    def print_languages(self):
        print("Now there are {} languages".
              format(len(Language.language_list)))
        for l in Language.language_list:
            l.display()

python = Language("Python", "interpreted")
java = Language("Java", "compiled")
Language.print_languages()

class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

class SmallBox(Box):
    def add(self, *items):
        for item in items:
            self.__items.append(item)

    def __init__(self, *items):
        self.__items = []
        for item in items:
            self.__items.append(item)

    def __str__(self):
        return str(self.__items)


if __name__ == '__main__':
    smbox1 = SmallBox(3, 4)
    smbox1.add(5, 6, 7)
    print(smbox1)



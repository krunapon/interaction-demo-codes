class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class DictBox:
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(
            dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)

    def display(self):
        for i in self._items:
            print("{} has value as {}".format(i, self._items.get(i).value))

dict1 = DictBox()
dict1.add(Item("pencil", "black"))
dict1.add(Item("pen", "blue"), Item("eraser", "white"))
dict1.add(Item("ruler", "brown"), Item("bottle", "orange"), Item("card", "yellow"))
dict1.display()

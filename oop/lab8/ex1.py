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

class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)

    def display(self):
        print("There are {} items".format(self.count()))
        for i in self._items:
            print("Item {} has value as {}".format(i.name, i.value))

lst1 = ListBox()
lst1.add(Item("pencil", "black"))
lst1.add(Item("pen", "blue"), Item("eraser", "white"))
lst1.add(Item("ruler", "brown"), Item("bottle", "orange"), Item("card", "yellow"))
lst1.display()

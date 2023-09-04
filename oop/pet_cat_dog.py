class Pet:
    # Initializer
    def __init__(self, name):

        # Animal class has one attribute: 'name'.
        self.name= name

    # Method
    def showInfo(self):
        print ("I'm " + self.name)

    # Method:
    def move(self):
        print ("moving ...")

class Cat(Pet):
    def __init__(self, name, owner, color):
        # Call to contructor of parent class (Animal)
        # to assign value to attribute 'name' of parent class.
        super().__init__(name)

        self.owner = owner
        self.color = color

    # Override method.
    def showInfo(self):
        super().showInfo()
        print (" and is  " + str(self.color))
        print (" belonging to " + str(self.owner))

    def move(self):
        print("Cat likes to walk more than run")


class Dog(Pet):
    def __init__(self, name, owner, color):
        # Call to contructor of parent class (Animal)
        # to assign value to attribute 'name' of parent class.
        super().__init__(name)

        self.owner = owner
        self.color = color

    # Override method.
    def showInfo(self):
        super().showInfo()
        print (" and is  " + str(self.color))
        print (" belonging to " + str(self.owner))

    def move(self):
        print("Cat likes to run more than walk")

    def eat_cat(self, cat):
        print("Dog {} eats cat {}".format(self.name, cat.name))

pet1 = Pet("Thongdaeng")
pet1.showInfo()
pet1.move()
cat1 = Cat("Thongdee", "Manee", "white");
cat1.showInfo();
cat1.move();
dog1 = Dog("Thongdum", "Mana", "black");
dog1.showInfo();
dog1.move();
dog1.eat_cat(cat1)




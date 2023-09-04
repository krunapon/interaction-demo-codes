class Vehicle:
  "A simple class for vehicle"

  #Constructor to initialize
  def __init__(self,company,color):
    self.company = company
    self.color = color

  #function to print car company and color
  def display(self):
    return 'This is a ' + self.color + " " + self.company + "."

class Car(Vehicle):
    def __init__(self, company, color, num_doors = 4):
        super().__init__(company, color)
        self.num_doors = num_doors

    def display(self):
        return super().display() +  " It has " + str(self.num_doors) + " doors."
          
class Truck(Vehicle):
    def __init__(self, company, color, dump_bed_area):
        super().__init__(company, color)
        self.dump_bed_area = dump_bed_area


    def display(self):
        return super().display() + " It has dump_bed_area as " + \
               str(self.dump_bed_area) + " cm x cm."

class SportCar(Car):
    def __init__(self, company, color, num_doors = 2):
        super().__init__(company, color)
        self.num_doors = 2


toyota1 = Vehicle("Toyota", "Gold")
honda1 = Car("Honda", "Bronze", 4)
isuzu1 = Truck("Isuzu", "Black", 100)
bmw1 = SportCar("BMW", "Red")
cars_list = []
cars_list.append(toyota1)
cars_list.append(honda1)
cars_list.append(isuzu1)
cars_list.append(bmw1)
for car in cars_list:
    print(car.display())



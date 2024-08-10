#!/usr/bin/env python

class Car:

    _maxspeed = 0
    __name = ""

    def __init__(self):
        self._maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self._maxspeed))


redcar = Car()
redcar.drive()
print(f' speed is {redcar._maxspeed}')
# will not change variable because its private
redcar._maxspeed = 10
redcar.drive()

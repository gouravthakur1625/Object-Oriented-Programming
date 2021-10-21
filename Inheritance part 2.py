# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:57:38 2021

@author: Hp
"""

class Vehicle:
    """Now we assign all Values in this method """
    def __init__ (self,model,price,milage):
        self.model = model 
        self.price = price
        self.milage = milage
    def show_car_details(self):
        print(f'{self.model} is the model of car')
        print(f'{self.price} is the price of the car')
        print(f'{self.milage} is the milage of car')
class Car(Vehicle):
    def __init__(self,model,price,milage,hp,tyre):
        super().__init__(model,price,milage)
        self.hp = hp
        self.tyre = tyre
    def show_details(self):
        print(f'The model of car is {self.model} and price is {self.price} and its horse power is {self.hp} with {self.tyre} tyres')
v1 = Vehicle('ABC12',12000000,190)
#v1.show_car_details()
c1 = Car('Tesla',50000000,440,557,4)
c1.show_details()
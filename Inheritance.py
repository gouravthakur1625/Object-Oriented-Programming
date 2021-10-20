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
    def show_details(self):
        print('Nothing new')
v1 = Vehicle('ABC12',12000000,190)
#v1.show_car_details()
c1 = Car('Abc007',12987 , 195)
c1.show_car_details()
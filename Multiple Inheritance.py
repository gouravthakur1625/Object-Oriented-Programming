# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 01:01:24 2021

@author: Hp
"""

class Computer:
    def __init__(self,model,memory,cost):
        self.model = model
        self.memory = memory 
        self.cost = cost
    def show_specification(self):
        print('The model is',self.model,'\n''The memory is',self.memory,'\n''The cost is',self.cost)
class laptop:
    def __init__(self,size,memory,processor):
        self.size = size
        self.memory = memory
        self.processor = processor
    def show_lap_spe(self):
        print('size',self.size,'\nmemory',self.memory,'\nprocessor',self.processor)
class Mobile(Computer,laptop):
    def assign(self,min_size):
        self.min_size = min_size
    def show_mob_spec(self):
        print('Minimum size of mobile is ',self.min_size)
c1 = Computer('Intel',156,15000)
c2 = laptop(15.6,512,'i5')
c3 = Mobile()
c3.assign(7)
c1.show_specification()
c3.show_mob_spec()
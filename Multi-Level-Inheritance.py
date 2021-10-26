# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 03:21:02 2021

@author: Hp
"""

class Cat:
    '''This is first class specify charactirstic of a Cat'''
    def meow(self):
        print('Cat always meow')
class Dog(Cat):
    '''In this class we specify characterstics of a Dog and inherit class Cat'''
    def bark(self):
        print('Dog always bark')
class Animal(Dog):
    """This is the class which Inherit the properties of class Cat and class Dog because
     this clas inheriting dog class and dog class is inheriting cat class"""
    def roar(self):
        print('Lion always Roar')
"""Now we can use properties of class Dog and cat in class Animal""" 
a1 = Animal()
a1.bark()
a1.meow()
a1.roar()
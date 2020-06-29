# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:09:50 2020

@author: 220316
"""

class Robot:
    
    def __init__(self,n,c,st,a,sp,h,w):
        self.name = n
        self.colour = c
        self.strength = st # Strength of attack (1-10)
        self.armour = a # Armour rating: restistance to attack (1-10)
        self.speed = sp # Speed (1-10)
        self.height = h # height in cm
        self.weight = w # weight in kg
        self.hp = w * a # How much damage it can take
    
    def print_stats(self):
        print(
            '\nName: '+self.name
            +'\nColour: '+self.colour
            +'\nStrength: '+str(self.strength)+'/10'
            +'\nArmour: '+str(self.armour)+'/10'
            +'\nSpeed: '+str(self.speed)+'/10'
            +'\nHeight: '+str(self.height)+' cm'
            +'\nWeight: '+str(self.weight)+' kg'
            )

r1 = Robot('Buster','blue',6,5,1,50,40)
r2 = Robot('Speedster','red',7,4,10,12,8)

r1.print_stats()

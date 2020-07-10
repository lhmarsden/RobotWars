# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:09:50 2020

@author: 220316
"""

from random import randint
import time

class Robot:
    
    registry = []
    
    def __init__(self,num,n,c,st,a,sp,h,w):
        self.registry.append(self) # Creating a registry to allow me to iterate through objects created in class
        self.number = num
        self.name = n
        self.colour = c
        self.strength = st # Strength of attack (1-10)
        self.armour = a # Armour rating: restistance to attack (1-10)
        self.speed = sp # Speed (1-10)
        self.height = h # height in cm
        self.weight = w # weight in kg
        self.hp = w * 15 # How much damage it can take
        self.hpr = self.hp # How much hp is remaining
    
    def print_stats(self):
        print(
            '\nNumber: '+str(self.number)
            +'\nName: '+self.name
            +'\nColour: '+self.colour
            +'\nStrength: '+str(self.strength)+'/10'
            +'\nArmour: '+str(self.armour)+'/10'
            +'\nSpeed: '+str(self.speed)+'/10'
            +'\nHeight: '+str(self.height)+' cm'
            +'\nWeight: '+str(self.weight)+' kg'
            +'\nHP: '+str(self.hpr)+'/'+str(self.hp)
            )


class Person:
    
    def __init__(self,n):
        self.name = n
    
    def select_robot(self, robots):
        print("\nPlease select a robot from the below choices by typing its number.")
        for robot in Robot.registry:
            robot.print_stats()
        selection = input()
        self.myRobot = robots[int(selection)]
        print(f'\nYou have selected {self.myRobot.name}')
 
# Calculate the damage an attack yields on opponent
def attack(r1,r2):
    if r1.speed > r2.speed:
        num_attacks = round(0.1*randint(1,10)*int(r1.speed/r2.speed))
    else:
        num_attacks = 1
    damage = 0
    for n in range(num_attacks):  
        damage += randint(1,10) * (1 + (r1.strength * (1-r2.armour/10)))
    return round(damage), num_attacks

def battle(r1,r2):
    print(f'\nGreat, {r1.name} will battle against {r2.name}!')
    
    ts = 3 # time to sleep between attacks in seconds
    
    while r1.hpr > 0 and r2.hpr > 0:
        
        if r1.speed > r2.speed:
            time.sleep(ts)
            damage, num_attacks = attack(r1,r2)
            if num_attacks > 1:
                print(f'\n{r1.name} attacked {r2.name} {num_attacks} times and did {damage} points of damage!')
            else:
                print(f'\n{r1.name} attacked {r2.name} and did {damage} points of damage!')
            r2.hpr -= damage 

            if r2.hpr <= 0:
                print(f'{r2.name} was destroyed! {r1.name} wins the battle!')
                break
            print(f'{r2.name} has {r2.hpr}/{r2.hp} hp remaining.')
        
                    
            time.sleep(ts)
            damage, num_attacks = attack(r2,r1)
            if num_attacks > 1:
                print(f'\n{r2.name} attacked {r1.name} {num_attacks} times and did {damage} points of damage!')
            else:
                print(f'\n{r2.name} attacked {r1.name} and did {damage} points of damage!')

            r1.hpr -= damage 
            if r1.hpr <= 0:
                print(f'{r1.name} was destroyed! {r2.name} wins the battle!')
                break
            print(f'{r1.name} has {r1.hpr}/{r1.hp} hp remaining.')
        
        else:
            
            time.sleep(ts)
            damage, num_attacks = attack(r2,r1)
            if num_attacks > 1:
                print(f'\n{r2.name} attacked {r1.name} {num_attacks} times and did {damage} points of damage!')
            else:
                print(f'\n{r2.name} attacked {r1.name} and did {damage} points of damage!')

            r1.hpr -= damage 
            if r1.hpr <= 0:
                print(f'{r1.name} was destroyed! {r2.name} wins the battle!')
                break
            print(f'{r1.name} has {r1.hpr}/{r1.hp} hp remaining.')
        
        
            time.sleep(ts)
            damage, num_attacks = attack(r1,r2)
            if num_attacks > 1:
                print(f'\n{r1.name} attacked {r2.name} {num_attacks} times and did {damage} points of damage!')
            else:
                print(f'\n{r1.name} attacked {r2.name} and did {damage} points of damage!')

            r2.hpr -= damage 
            if r2.hpr <= 0:
                print(f'{r2.name} was destroyed! {r1.name} wins the battle!')
                break
            print(f'{r2.name} has {r2.hpr}/{r2.hp} hp remaining.')
        
            
def main():
    
    robots = {}
    robots[1] = Robot(1,'Buster','blue',6,2,1,50,50)
    robots[2] = Robot(2,'Speedster','red',2,4,10,12,12)
    robots[3] = Robot(3, 'Robby', 'green',3,8,6,30,20)
    robots[4] = Robot(4, 'Geoff', 'black',4,9,3,25,20)
    
    p1 = Person('Player 1')
    p2 = Person('Player 2')
    
    
    p1.select_robot(robots)
    print("\nNow, please select a robot to battle against.")
    p2.select_robot(robots)
    
    battle(p1.myRobot, p2.myRobot)
    
    #print(p1)
    
    
if __name__ == "__main__":
    main()
        
       



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:30:23 2023

@author: Jeremy
"""

# enter type of tree
def tree_name():
    tree_species = {"silver maple": 3, "red maple": 4.5, "black birch": 3.5,
                    "green ash": 4, "black walnut": 4.5, "black cherry": 5, "cottonwood": 2, 
                    "shagbark hickory": 7.5, "basswood": 5, "red oak": 6.7, "white oak":5, 
                    "boxelder maple": 3, "norway maple": 4.5, "sugar maple": 5.5, "horsechestnut":6, 
                    "ironwood": 7, "catalpa": 1.5, "hackberry": 2, "flowering dogwood":7,
                    "beech":6, "tuliptree": 3, "norway spruce": 5, "white pine": 5, "scots pine": 3.5,
                    "quaking aspen": 2, "black willow": 2, "hemlock":6, "elm":4}
    while True:
        tree_type= input("What type of tree: ").lower()
        if tree_type in tree_species:
            return(tree_species[tree_type])
        else:
            print("this tree in not in our system")
       

#enter circumference and check measurements are correct
def diameter():
    while True:
        try:
            circum = float(input("Enter circumference in inches: "))
            if 1 <= circum <= 10000:
                return circum / 3.14
            else:
                print( "Please eneter a number between 1 and 10,000")  
        except ValueError:
            print("Enter a number")

# function takes name and measurement as parameters. It multiples the two parameters to obtain age 
def ager(name, measurement):
    age = name * measurement
    print(f"Your tree is {age}")

print("Let's age your tree") 
name = tree_name()
measurement = diameter()
ager(name, measurement)

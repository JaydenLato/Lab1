
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jayden Lato
# Date: 09/18/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'

import math as m # Importing the math module

radius = int(input("Input a radius of the circle: ")) # Asking the user for the raidus of the circle
area = m.pi * radius ** 2 # Calculating the radius of the circle and assigning it to area

print(area) # Printing the area of the circle
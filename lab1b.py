# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jayden Lato
# Date: 09/18/2026
# Purpose: Use arithmetic in python.
# Usage: python3 lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
#	Create another variable called "num2" and take its value from user. 
# Convert the values to integers using int() function

num1 = int(input("Input a number: ")) # Asking the user for num1
num2 = int(input("Input another number: ")) # Asking the user for num2

# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.

print(f"{num1 + num2}") # Adding num1 and num2
print(f"{num1 - num2}") # Subtracting num1 and num2
print(f"{num1 * num2}") # Multiplying num1 and num2
print(f"{num1 ** num2}") # num1 to the power of num2
print(f"{num1 / num2}") # Dividing num1 with num2
print(f"{num1 // num2}") # Dividing num1 and num2 but rounding to the nearest whole number
print(f"{num1 % num2}") # Dividing num1 and num2 but showing the remainder
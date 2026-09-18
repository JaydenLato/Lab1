# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jayden Lato
# Date: 09/18/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: python3 lab1a.py

# TO DO 1: Creating and using varibales
# create a variable called message.
# Set the variable to equal to "Welcome to PRG101".
# Print the variable message using print() statement.

message = "Welcome to PRG 101" # Variable message with the string "Welcome to PRG 101"
print(message) # Printing the variable message
print(f"{message} Python is the future.") # Concat message with “ Python is the future.”

# TO DO 2: Checking the type of a varibale
# Use the builtin type() function and print the type of this variable.

print(type(message)) # Printing the type of the message

# TO DO 3: Dynamic Typing:
# Create a varibel called `x` and assign it the value 10, then print the type of this variable.

x = 10 # Creating the variable x and assiging with the value of 10
print(x) # Printing the variable x

# TO DO 4: Dynamic Typing: 
# Now reassign a new value to the variable `x`, this value should be a string, e.g "hello", check the type of the variable `x` again.
# What did you observe?

x = "hello" # Reassigning variable x to the string "hello"
print(x) # Printing the new reassigned variable x

# The variable changed from being 10 to "hello", this is because the previous variable, 10 was overwritten with "hello" because it was written last
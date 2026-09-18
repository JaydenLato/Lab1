# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jayden Lato
# Date: 09/18/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py

#TO-DO 1:
#	Create a variable called "name" and assign it the value of your name.
# Use the string method .upper() to convert the name to upper case.
# Create another variable called “age”, the value of “age” should be your age
# The script, when executed, should print out "How are you yourname? Happy xxth birthday!" To print this output use .format() method. 

name = "Jayden Lato" # Variable with my name
name.upper() # Changing my name to be fully upper case
age = 18 # My current age
print(f"How are you, {name}? Happy {age}th birthday!") # Print statement with the name and age variables

#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
# Use indexing to return the first and 17th charecters of "words" to the user.

words = "The quick brown fox jumps over the lazy dog"
#        0123456789012345678901234567890123456789012
print(words[0]) # Prints the first letter of words
print(words[16]) # Prints the 17th letter of words

#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.

print(words[-23:-18]) # Prints "jumps"
print(words[-39:-34]) # Prints "quick"

#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
# Print "uick brown foxs ju" from "words".

print(words[2:15]) # Prints "e quick brown"
print(words[5:22]) # Prints "uick brown fox ju"
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jayden Lato
# Date: 09/18/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.

quantity = 10.29 # Quantity variable
stock = 8.8 # Stock variable

product = quantity * stock # Product Variable, Quantity multiplied by Stock
print(f"The product of quantity and stock is {product}") # 1 space before the answer
print("The product of quantity and stock is %s%.2f" % (" " * 4, product)) # 4 spaces before the answer
print("The product of quantity and stock is %s%.2f" % (" " * 7, product)) # 7 spaces before the answer and only goes to the hundredths (-.--)
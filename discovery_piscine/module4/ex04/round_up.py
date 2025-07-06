#!/usr/bin/env python3

# Import the math module to use math.ceil()
import math

# Prompt for a number and convert to float
num = float(input("Give me a number: "))

# Round up and print the result as an integer (so it shows 42 instead of 42.0)
print(int(math.ceil(num)))
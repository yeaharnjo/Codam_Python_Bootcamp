#!/usr/bin/env python3

# Define an array of numbers.
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new array by adding 2 to each element using a list comprehension
new_array = [x + 2 for x in original_array]

# Print the original array
print("Original array:", original_array)

# Print the new, modified array
print("New array:", new_array)
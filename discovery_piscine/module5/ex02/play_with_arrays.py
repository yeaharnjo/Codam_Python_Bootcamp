#!/usr/bin/env python3

# Define an array of numbers.
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new array by adding 2 to each element that is greater than 5. (newlist = [expression for item in iterable if condition == True])
new_array = [n + 2 for n in original_array if n > 5]

# Print the original array
print("Original array:", original_array)

# Print the new, modified array
print("New array:", new_array)
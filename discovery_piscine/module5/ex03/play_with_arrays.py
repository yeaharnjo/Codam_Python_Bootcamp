#!/usr/bin/env python3  

# Define the original array (list) of numbers
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new set by adding 2 to each element in original_array greater than 5
# The set automatically removes duplicates
new_set = {n + 2 for n in original_array if n > 5}

# Print the original list exactly as is
print(original_array)

# Print the new set, which shows only unique values. Convert the set to a sorted list before printing.
print(sorted(new_set))
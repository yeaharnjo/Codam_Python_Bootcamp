#!/usr/bin/env python3

# Prompt the user for their age and convert to integer
age = int(input("Please tell me your age: "))

# List of year increments
increments = [0, 10, 20, 30]

for inc in increments:
    if inc == 0:
        print(f'You are currently {age} years old.')
    else:
        print(f"In {inc} years, you'll be {inc + age} years old.")

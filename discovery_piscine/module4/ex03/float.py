#!/usr/bin/env python3


num = float(input("Give me a number: "))

# .is_integer() returns True if num has no decimal part (e.g., 42.0, 42.00)
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
    
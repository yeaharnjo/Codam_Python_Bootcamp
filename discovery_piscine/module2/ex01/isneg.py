#!/usr/bin/env python3

#Prompt 
number = float(input("Enter a number: "))

#Check
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative")
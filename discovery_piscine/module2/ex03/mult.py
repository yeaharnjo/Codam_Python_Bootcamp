#!/usr/bin/env python3

#Prompt
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

#Multiply
result = first * second

#Print the multiplication
print(f"{int(first)} x {int(second)} = {int(result)}")

#Check
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is positive and negative")


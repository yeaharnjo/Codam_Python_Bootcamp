#!/usr/bin/env Python3

num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))
print('Thank you!')

print(f"{float(num1)} + {float(num2)} = {float(num1 + num2)}")
print(f"{float(num1)} - {float(num2)} = {float(num1 - num2)}")
if num2 != 0:
    print(f"{float(num1)} / {float(num2)} = {float(num1 / num2)}")
else:
    print(f"{float(num1)} / {float(num2)} = undefined ")
print(f"{float(num1)} * {float(num2)} = {float(num1 * num2)}")

#!/usr/bin/env python3

try:
 # Prompt
 num = int(input("Enter a number less than 25\n"))

 # Check
 if num > 25:
    print("Error")
 else:
    # Use a while loop to display numbers up to 25
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1 # Increment number by 1 each loop
except ValueError:
   print("Please enter a valid integer.")
#!/usr/bin/env python3

table = 0
while table <= 10:
    print("Table of " + str(table) + ":", end=" ") # Stays on the same line
    num = 0
    while num <= 10:
        print(table * num, end=" ") # Numbers on the same line
        num += 1
    print()
    table += 1
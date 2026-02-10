#!/usr/bin/env python

print("Enter a number")

number = int(input())

i = 0
while i < 10:
    print(f"{i} x {number} = {i * number}")
    i += 1
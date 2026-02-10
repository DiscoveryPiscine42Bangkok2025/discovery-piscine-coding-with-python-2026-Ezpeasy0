#!/usr/bin/env python

print("Enter a number less than 25")
user_input = input()
number = int(user_input)

if number > 25:
    print("Error")
else:

    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1
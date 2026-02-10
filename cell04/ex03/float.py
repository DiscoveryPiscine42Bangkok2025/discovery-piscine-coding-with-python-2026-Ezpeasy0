#!/usr/bin/env python

user_input = input("Give me a number: ")

num = float(user_input)

if num == int(num):
    print("This number is an integer.")
else:
    print("This number is a decimal.")
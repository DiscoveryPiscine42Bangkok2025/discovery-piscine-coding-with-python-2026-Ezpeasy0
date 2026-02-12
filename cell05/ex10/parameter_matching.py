#!/usr/bin/env python
import sys

def main():

    if len(sys.argv) != 2:
        print("none")
        return

    passed_parameter = sys.argv[1]

    user_input = input("What was the parameter? ")

    if user_input == passed_parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()

 #./parameter_matching.py
 # ./parameter_matching.py "Hello"
   
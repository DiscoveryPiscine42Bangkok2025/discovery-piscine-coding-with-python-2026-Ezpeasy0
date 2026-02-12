#!/usr/bin/env python
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    target_string = sys.argv[1]

    z_count = target_string.count('z')

    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)

if __name__ == "__main__":
    main()
    #./string_are_arrays.py | cat -e
    #./string_are_arrays.py "The character Z is not found in this string" | cat -e
    #./string_are_arrays.py "The character z is found in this string" | cat -e
    #./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
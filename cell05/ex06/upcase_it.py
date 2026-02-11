#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    print(sys.argv[1].upper())
else:
    print("none")

#./upcase_it.py
#./upcase_it.py "world"
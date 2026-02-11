#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    print(sys.argv[1].lower())
else:
    print("none")

#./downcase_it.py
#./downcase_it.py "THEWORLD"
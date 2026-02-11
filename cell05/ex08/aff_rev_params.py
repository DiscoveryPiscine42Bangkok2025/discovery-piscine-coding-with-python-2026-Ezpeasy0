#!/usr/bin/env python
import sys

if len(sys.argv) < 3:
    print("none")
else:
    for i in range(len(sys.argv) - 1, 0, -1):
        print(sys.argv[i])

#./aff_rev_params.py "cou" | cat -e
#./aff_rev_params.py "python" "psicine" "hello" | cat -e
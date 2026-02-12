#!/usr/bin/env python
import sys

def main():
    params = sys.argv[1:]
    
    if not params:
        print("none")
        return

    for p in params:
        if not p.endswith("ism"):
            print(f"{p}ism")

if __name__ == "__main__":
    main()
    
    #./append_it.py | cat -e
    # ./append_it.py "parallel" "egoism" "human" | cat -e
#!/usr/bin/env python
import sys

def main():
    params = sys.argv[1:]
    
    if not params:
        print("none")
        return

    print(f"parameters: {len(params)}")

    for p in params:
        print(f"{p}: {len(p)}")

if __name__ == "__main__":
    main()

    #./count_it.py | cat -e
    # ./count_it.py "Game" "of" "Thrones" | cat -e
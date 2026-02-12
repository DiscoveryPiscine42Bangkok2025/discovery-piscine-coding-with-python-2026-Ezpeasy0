#!/usr/bin/env python
import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]

    matches = re.findall(re.escape(keyword), search_string)
    count = len(matches)

    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()

    #./scan_it.py | cat -e
    #./scan_it.py "the" | cat -e
    #./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
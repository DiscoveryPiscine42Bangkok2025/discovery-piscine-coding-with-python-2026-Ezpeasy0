#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    print("none")
else:
    table_num = 0
    while table_num <= 10:
        print(f"Table de {table_num}:", end="")
        
        multiplier = 0
        while multiplier <= 10:
            print(f" {table_num * multiplier}", end="")
            multiplier += 1
            
        print() 
        table_num += 1
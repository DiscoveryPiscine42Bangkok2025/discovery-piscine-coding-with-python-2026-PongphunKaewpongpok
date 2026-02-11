#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    str_input = input("What was the parameter? ")
    if str_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")

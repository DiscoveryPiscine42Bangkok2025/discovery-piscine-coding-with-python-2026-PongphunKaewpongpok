#!/usr/bin/env python3

import sys

def shrink(str):
    return str[0:8]

def enlarge(str):
    return str + "Z" * (8-len(str))


if len(sys.argv) <= 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        print(enlarge(shrink(sys.argv[i])))
#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        is_ism = sys.argv[i].find("ism")
        if is_ism == -1:
            print(sys.argv[i] + "ism")
#!/usr/bin/env python3

import sys, re

if len(sys.argv) != 2:
    print("none")
else:
    z_list = re.findall("z", sys.argv[1])
    if len(z_list) == 0:
        print("none")
    else:
        print("z" * len(z_list))
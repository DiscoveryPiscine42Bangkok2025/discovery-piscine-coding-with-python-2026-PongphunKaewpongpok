#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    num_list = []
    steps = 1
    if int(sys.argv[1]) >= int(sys.argv[2]):
         steps = -1
        
    for i in range(int(sys.argv[1]), int(sys.argv[2])+steps, steps):
        num_list.append(i)
    
    print(num_list)
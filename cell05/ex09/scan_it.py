#!/usr/bin/env python3

import sys, re

if len(sys.argv) != 3:
    print("none")
else:
    str_keyword = sys.argv[1]
    target_word = sys.argv[2]

    word_count = len(re.findall(str_keyword, target_word))
    if word_count == 0:
        print("none")
    else:
        print(word_count)

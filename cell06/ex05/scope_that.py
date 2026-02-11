#!/usr/bin/env python3

def add_one(num):
    num = num+1

some_number = 0
print("Before:", some_number)
add_one(some_number)
print("After:", some_number)
# Changing variable will not affect to it global variable but still change in that called function.
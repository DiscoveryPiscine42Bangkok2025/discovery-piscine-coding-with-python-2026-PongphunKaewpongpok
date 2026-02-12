#!/usr/bin/env python3

def greetings(value="noblestranger"):
    if isinstance(value, str):
        print(f"Hello, {value}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
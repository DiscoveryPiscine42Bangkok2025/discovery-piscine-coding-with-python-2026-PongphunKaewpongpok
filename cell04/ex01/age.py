#!/usr/bin/env python3

age_input = int(input("Please tell me your age: "))

print(f"You are currently {age_input} years old.")
for i in range(10, 31, 10):
    print(f"In {i} years, you'll be {age_input+i} years old.")
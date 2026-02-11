#!/usr/bin/env python3

first_num = int(input("Give me the first number: "))
second_num = int(input("Give me the second number: "))

print("Thank you!")
divide_num = float(first_num/second_num)
if divide_num.is_integer():
    divide_num = int(divide_num)

print(f"{first_num} + {second_num} =", first_num+second_num)
print(f"{first_num} - {second_num} =", first_num-second_num)
print(f"{first_num} / {second_num} =", divide_num)
print(f"{first_num} * {second_num} =", first_num*second_num)
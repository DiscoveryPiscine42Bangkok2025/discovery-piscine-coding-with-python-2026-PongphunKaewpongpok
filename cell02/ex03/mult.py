#!/usr/bin/env python3

first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
result_num = first_num * second_num

print(first_num, "*", second_num, "=", result_num)
if result_num > 0:
    print("The result is positive.")
elif result_num < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
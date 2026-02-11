float_input = float(input("Give me a number: "))

if float_input.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
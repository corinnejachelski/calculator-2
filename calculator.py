"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def calculator(input_string):
    """creates a calculator to reference functions in arithmetic.py"""
    #statement = input("Enter your arithmetic argument: ")
    statement = input_string.split(" ")
    first_token = statement [0]
    second_token = int(statement[1])
    third_token = int(statement[2])
    if first_token == "q":
        quit
    else:
        if first_token == "+":
            output = add(second_token, third_token)
        elif first_token == "-":
            output = subtract(second_token, third_token)
        elif first_token == "/":
            output = divide(second_token, third_token)
        elif first_token == "square":
            output = square(second_token, third_token)
        elif first_token == "cube":
            output = cube(second_token, third_token)
        elif first_token == "pow":
            output = power(second_token, third_token)
        elif first_token == "mod":
            output = mod(second_token, third_token)
        print(output)
        return output

calculator("mod 4 2")
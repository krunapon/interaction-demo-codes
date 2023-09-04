import math
import pdb

ADD = "+"
SUB = "-"
MUL = "*"
DIV = "/"
QUIT = "q"


def calculator(a, b, operator=ADD, output_format=float):
    if operator == ADD or operator == "":
        result = a + b
    elif operator == SUB:
        result = a - b
    elif operator == MUL:
        result = a * b
    elif operator == DIV:
        try:
            result = a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None

    if output_format == int:
        result = round(result)
    else:
        result = float(result)

    return result


def get_operator():
    in_operator = input("Enter an operation ('+', '-', '*', '/'):")
    if in_operator == ADD or in_operator == SUB or \
            in_operator == MUL or in_operator == DIV or in_operator == "":
        return in_operator
    else:
        print("Operation must be ADD, SUB, MUL or DIV.")
        return None


def get_the_first_operand():
    while True:
        try:
            operand1 = input("Please enter the first operand ('q' to quit):")
            if operand1.lower() == "q":
                exit(0)
            return float(operand1)
        except ValueError:
            print("Please enter a number")


def get_the_second_operand():
    while True:
        try:
            operand2 = input("Please enter the second operand:")
            return float(operand2)
        except ValueError:
            print("Please enter a number")


def get_format():
    r_format = input("Enter output format (float, int):")
    if r_format == 'int':
        return int
    else:
        return float


def robust_calculator():
    while True:
        op1 = get_the_first_operand()
        op2 = get_the_second_operand()
        operator = get_operator()
        if operator is None:
            continue
        requested_format = get_format()
        output = calculator(op1, op2, operator, requested_format)
        if output is not None:
            if operator == "":
                operator = ADD
            print("{} {} {} = {}".format(op1, operator, op2, output))
        else:
            print("We cannot perform your requested calculation")


robust_calculator()

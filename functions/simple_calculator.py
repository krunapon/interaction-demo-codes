import math
ADD, SUB, MUL, DIV = range(4)
def calculator(a, b, operation=ADD, output_format=float):
    if operation == ADD:
        result = a + b
    elif operation == SUB:
        result = a - b
    elif operation == MUL:
        result = a * b
    elif operation == DIV:
        result = a / b
    else:
        raise ValueError("Operation must be ADD, SUB, MUL or DIV.")
    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = round(result)
    else:
        raise ValueError("Format must be float or int.")
    return result
result = calculator(2, 3)
print("2 + 3 is {}".format(result))
result = calculator(2, 3, MUL)
print("2 * 3 is {}".format(result))
result = calculator(2, 3, SUB, int)
print("2 - 3 is {}".format(result))

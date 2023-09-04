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


def flexible_calculator(operation=ADD, output_format=float, *args):
    try:
        if not args:
            raise ValueError("At least one number must be entered.")
    except ValueError as err:
        print("%s" % err)
        return None

    result = args[0]

    for n in args[1:]:
        if operation == ADD:
            result += n
        elif operation == SUB:
            result -= n
        elif operation == MUL:
            result *= n
        elif operation == DIV:
            result /= n
        else:
            raise ValueError("Operation must be ADD, SUB, MUL or DIV.")

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = round(result)
    else:
        raise ValueError("Format must be float or int.")

    return result


answer = calculator(2, 3)
print("calculator(2, 3) = {}".format(answer))
answer = calculator(2, 3, MUL)
print("calculator(2, 3, MUL) = {}".format(answer))
answer = calculator(2, 3, SUB, int)
print("calculator(2, 3, SUB, int) = {}".format(answer))
answer = flexible_calculator(ADD, int, 1, 2, 3)
print("flexible_calculator(ADD, int, 1, 2, 3) = {}".format(answer))
answer = flexible_calculator(ADD, int, 1, 2, 3, 4)
print("flexible_calculator(ADD, int, 1, 2, 3, 4) = {}".format(answer))
answer = flexible_calculator(SUB, float, 1, 2, 3, 4, 5)
print("flexible_calculator(SUB, float, 1, 2, 3, 4, 5) = {}".format(answer))
answer = flexible_calculator(ADD, int, 1)
print("flexible_calculator(ADD, int, 1) = {}".format(answer))
answer = flexible_calculator(MUL, int, 2, 3, 4)
print("flexible_calculator(MUL, int, 2, 3, 4) = {}".format(answer))
answer = flexible_calculator(DIV, float, 10, 5, 2)
print("flexible_calculator(DIV, float, 10, 5, 2) = {}".format(answer))
answer = flexible_calculator(DIV, float)
print("flexible_calculator(DIV, float) = {}".format(answer))
answer = flexible_calculator(DIV, float, 5, 0)
print("flexible_calculator(DIV, float, 5,0) = {}".format(answer))

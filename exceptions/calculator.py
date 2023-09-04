while True:
    try:
        num1 = int(input("Please enter the first operand:"))
        break
    except ValueError:
        print("Please enter a number")


while True:
    try:
        num2 = int(input("Please enter the second operand:"))
        break
    except ValueError:
        print("Please enter a number")

operator = input("Please enter an operator (+,-,*,/):")
if operator == "+":
    print("Result of {} {} {} is {}".format(num1, operator, num2,
                                                num1 + num2))
elif operator == "-":
    print("Result of {} {} {} is {}".format(num1, operator, num2,
                                                    num1 - num2))
elif operator == "*":
    print("Result of {} {} {} is {}".format(num1, operator, num2,
                                                    num1 * num2))
elif operator == "/":
    try:
        result = num1 / num2
        print("Result of {} {} {} is {}".format(num1, operator, num2, num1/num2))
    except ZeroDivisionError:
            print("Cannot divide by zero")
else:
    print("Unknown operator")


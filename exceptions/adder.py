try:
    n1 = float(input("Enter the first number:"))
    if n1 < 1 or n1 > 10:
        raise ValueError("Please enter only the numbers in the range [1,10]")
    n2 = float(input("Enter the second number:"))
    if n2 < 1 or n2 > 10:
        raise ValueError("Please enter only the numbers in the range [1,10]")
    answer = n1 + n2
    print(f'The answer of {n1} + {n2} is {answer}')
except ValueError as err:
    print("Please try to enter a valid number %s" % err)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


try:
    n = int(input("Enter an integer:"))
    if n <= 0:
        raise ValueError("{} is not a positive integer"
                         .format(n))
    print("factorial({}) is {}".format(n, factorial(n)))
except ValueError as err:
    print("Please enter a positive integer. %s" % err)


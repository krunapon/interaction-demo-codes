def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter an integer:"))
print("fibonacci({}) is {}".format(n, fibonacci(n)))


def fibonacci(n):
    current, next = 0, 1

    for i in range(n):
        current, next = next, current + next

    return current


n = int(input("Enter an integer:"))
print("fibonacci({}) is {}".format(n, fibonacci(n)))

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return None


print(multiply("2", "3"))
print(multiply(2,3))

def fact(n: int) -> int:
    return 1 if n == 1 else n * fact(n-1)


if (__name__ == '__main__'):
    print("fact({}) is {}".format(2, fact(2)))
    print("fact({}) is {}".format("a", fact("a")))

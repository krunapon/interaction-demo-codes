def test(a):
    if a == 0:
        print("a is 0")
    else:
        print("a is not 0")
        return None
    print("come here")
    return 3


b = test(3)
print("b is {}".format(b))

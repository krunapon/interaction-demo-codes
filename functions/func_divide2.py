def divide(dividend, divisor):
    if not divisor:
        return None, None # instead of dividing by zero

    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
a = 4
b = 0
print("Attempting to divide {} / {}".format(a, b))
o1, o2 = divide(a,b)
print(f"{o1} and {o2}")

def simple_func():
    print("hello")

result = simple_func()
print(result)

def divide(dividend, divisor):
    try:
        if not divisor:
            raise ValueError("The divisor cannot be zero!")
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    except Exception as err:
        print(err)
 

a = 4
b = 0
print("Attempting to divide {} / {}".format(a, b))
divide(a,b)

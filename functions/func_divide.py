def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
# you can do this
q, r = divide(35, 4)
print("q is {} and r is {}".format(q, r))
# but you can also do this
result = divide(67, 9)
q1 = result[0]
q2 = result[1]
print("result is {} q1 is {} and q2 is {}".format(result, q1, q2))
# by the way, you can also do this
a, b = (1, 2)
print("a is {} b is {}".format(a, b))
# or this
c, d = [5, 6]
print("c is {} d is {}".format(c, d))

import sys
import pdb

def divide(dividend, divisor):
    if divisor != 0:
       #pdb.set_trace()
       return dividend / divisor 
    else:
       print("Cannot perform division by zero")

while True:
    dividend = input("Please enter the dividend:")
    #pdb.set_trace()
    if dividend < 0:
	break
    divisor = input("Please enter the divisor:")
    if divisor < 0:
	break	
    answer = divide(dividend, divisor)
    if answer is not None:
       print('The answer is: {}'.format(answer))

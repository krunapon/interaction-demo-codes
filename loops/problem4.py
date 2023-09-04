# Write a program which finds the factorial of a given number.
# E.g. 3 factorial, or 3! is equal to 3 x 2 x 1; 5! is equal to 5 x 4 x 3 x 2 x 1, etc..
# Your program should only contain a single loop.
number = int(input("Enter a number to find the factorial:"))
factorial = 1
for cur_count in range(1, number + 1):
    factorial = factorial * cur_count
print ("Factorial of %d is %d" % (number, factorial))

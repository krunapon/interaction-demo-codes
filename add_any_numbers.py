# this function definition starts a new block
def add_any_numbers(a,b):
   # this instruction is inside the block
   c = a + b
   return c

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
result = add_any_numbers(num1, num2)

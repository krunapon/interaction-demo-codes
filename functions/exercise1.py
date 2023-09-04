# 1. Create a function called func_a, which prints a message.
# 2. Call the function.
# 3. Assign the function object as a value to the variable b,
#    without calling the function.
# 4. Now call the function using the variable b.
def func_a(message):
    print(message)
print("Hello, Python!")
b = func_a
b("Hi, Python!")



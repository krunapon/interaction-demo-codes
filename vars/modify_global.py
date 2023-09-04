a = 0 # a global variable

def my_function():
    global a  
    a = 3
    print(a)

my_function()

print(a) # a global variable

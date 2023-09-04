name = "True"

# This is shorthand for checking if name evaluates to True:
if name:
    print("Hello1, %s!" % name)

# It means the same thing as this:
if bool(name) == True:
    print("Hello2, %s!" % name)

# This won't give us the answer we expect:
if bool(name) == True:
    print("Hello3, %s!" % name)

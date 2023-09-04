import random
# set a predictable seed
random.seed(3)
print("Generating random number with this seed = 3")
print(random.random())
print(random.random())
print(random.random())

# now try it again
random.seed(3)
print("Generating random number with this seed = 3")
print(random.random())
print(random.random())
print(random.random())


# and now try a different seed
random.seed("different")
print("Generating random number with this seed = 'different'")
print(random.random())
print(random.random())
print(random.random())


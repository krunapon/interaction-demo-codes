animals = ('cat', 'dog', 'fish', 'cat')

# we can access a single element
print(animals[0])

# we can get a slice
print(animals[1:]) # note that our slice will be a new tuple, not a list
print(animals[:-1])
# we can count values or look up an index
print(animals.count('cat'))
print(animals.index('dog'))

# ... but this is not allowed:
# animals.append('canary')
# animals[1] = 'gerbil'

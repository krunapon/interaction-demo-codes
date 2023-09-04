marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 } 
print(marbles)
colours = list(marbles) # the keys will be used by default 
print(colours)
counts = tuple(marbles.values()) # but we can use a view to get the values 
print(counts)
marbles_set = set(marbles.items()) # or the key-value pairs
print(marbles_set)

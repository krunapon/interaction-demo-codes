# 1. Convert a list which contains the numbers 1, 1, 2, 3 and 3, and convert it to a tuple a.
a = tuple([1, 1, 2, 3, 3])

# 2. Convert a to a list b. Print its length.
b = list(a)
print(len(b))

# 3. Convert b to a set c. Print its length.
c = set(b)
print(len(c))

# 4. Convert c to a list d. Print its length.
d = list(c)
print(len(d))

# 5. Create a range which starts at 1 and ends at 10. Convert it to a list e and print the list. 
e = list(range(1,11))
print(e)

# 6. Create the directory dict from these pairs 
# {"manee": "1234", "mana": "4567", "chujai":"6789"}
# Create a list t which contains all the key-value pairs 
# from the dictionary as tuples. Print list t
directory = {"manee": "1234", "mana": "4567", "chujai": "6789"} 
t = list(directory.items())
print(t)

# 7. Create a list v of all the values in the dictionary. Print list v
v = list(directory.values())
print(v)

# 8. Create a list k of all the keys in he dictionary. Print list k
k = list(directory)
print(k)

# 9. Create a string s which contains the word "antidisestablishmentarianism". Use the sorted function on it. What is the output type? Concatenate the letters in the output to a string s2. Print s2
s = "antidisestablishmentarianism"
s2 = "".join(sorted(s))
print(s2)

# 10. Split the string "the quick brown fox jumped over the lazy dog" into a list w of individual words.
# Print these words
print("the quick brown fox jumped over the lazy dog".split(" "))

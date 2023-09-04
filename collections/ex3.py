# 1. Create a set a which contains the first four positive integers and a set b which contains the first four odd positive integers.
a = {1, 2, 3, 4}
b = {1, 3, 5, 7}

# 2. Create a set c which combines all the numbers which are in a or b (or both).
c = a | b

# 3. Create a set d which contains all the numbers in a but not in b.
d = (a - b)

# 4. Create a set e which contains all the numbers in b but not in a.
e = (b - a)

# 5. Create a set f which contains all the numbers which are both in a and in b.
f = (a & b)

# 6. Create a set g which contains all the numbers which are either in a or in b but not in both.
g = (a ^ b)

# 7. Print the number of elements in c.
print(len(c))

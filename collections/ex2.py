# 1. Create a tuple a which contains the first four positive integers and a tuple b which contains the next four positive integers.
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

# 2. Create a tuple c which combines all the numbers from a and b in any order.
c = a + b

# 3. Create a tuple d which is a sorted copy of c.
d =  sorted(c)

# 4. Print the third element of d.
print(d[2])

# 5. Print the last three elements of d without using its length.
print(d[-3:])

# 6. Print the length of d.
print(len(d))

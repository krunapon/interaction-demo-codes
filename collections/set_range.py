# 1. Create a set a which contains the first four positive integers and a set b which contains the first four odd positive integers.
a = {1, 2, 3, 4}
b = {1, 3, 5, 7}

# 2. Create a set c which combines all the numbers which are in a or b (or both).
c = a | b

# 3. Create a set d which contains all the numbers in a but not in b.
d = (a - b)

# 4. Create a range a which starts from 0 and goes on for 20 numbers.
print(list(range(0,20)))

# 5. Create a range b which starts from 3 and ends on 12.
print(list(range(3,13)))

# 6. Create a range c which contains every third integer starting from 2 and ending at 50.
print(list(range(2,51,3)))
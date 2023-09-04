numbers = [22, 33, 44, 11]
# these return a modified copy, which we can print
print(sorted(numbers))
print(list(reversed(numbers)))

# the original list is unmodified
print(numbers)

# now we can modify it in place
numbers.sort()
numbers.reverse()
print(numbers)

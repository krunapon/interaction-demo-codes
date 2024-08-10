def count_trailing_zeros(n):
    if n == 0:
        return 1
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count


first = 4**5**6
second = 5**6**4
third = 5**4**6
forth = 6**5**4
result = first * second - third * forth
print(result)
print(count_trailing_zeros(result))
print(count_trailing_zeros(first * second))
print(count_trailing_zeros(third * forth))

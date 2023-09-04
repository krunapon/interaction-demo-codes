total = 0
product = 1

for i in range(1, 10 + 1):
    num = float(input("Please enter number %d: " % i))
    total += num
    product *= num

average = total/10

print("Sum: %g\nProduct: %g\nAverage: %g" % (total, product, average))

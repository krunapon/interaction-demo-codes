from fact import fact

while True:
    n = int(input("Please enter n:"))
    if n <= 0:
        break
    print(fact(n))

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


while True:
    try:
        n1 = float(input("Enter the first number:"))
	if n1 == "quit":
	    break
        n2 = float(input("Enter the second number:"))
        if n2 == "quit":
	    break
        op = input("Enter +,-,*,/:")
	if op == "quit":
	    break
        result = 0
        if op == "+":
            result = add(n1, n2)
        elif op == "-":
            result = subtract(n1, n2)
        elif op == "*":
            result = multiply(n1, n2)
        elif op == "/":
            result = divide(n1, n2)
        else:
            print("Unknown operator")
	    continue
    except ValueError:
        print("Please enter only numbers")

filename = input("Enter a filename:")
with open(filename, "r") as reader:
    for line in reader:
        print(line, end='')


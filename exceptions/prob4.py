str = input("Enter the list of numbers (delimited by a comma):")
list = str.split(",")
print(list)
index = int(input("Enter an index:"))
try:
    print(list[index])
except IndexError as ie:
    print("The list has no element at index %d." % index)

my_number = None
my_string = ""
if my_number is not None:
    print(my_number) # could still be zero
else:
    print("my_number is None")

if my_string is None:
    print("I haven't got a string at all!")
elif not my_string: # another false value, i.e. an empty string
    print("My string is empty!")
else:
    print("My string is '%s'." % my_string)

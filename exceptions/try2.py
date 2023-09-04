try:
    age = int(input("Please enter your age: "))
    if age < 0:
       print("{} is not a valid age. Age must be positive or zero."
                   .format(age))
    else:
       print("I see that you are %d years old." % age)
except:
    print("You entered incorrect age input")
finally:
    print("bye")

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey, that wasn't a number!")
    exit
else:
    print("I see that you are %d years old." % age)
finally:
    print("It was really nice talking to you.  Goodbye!")

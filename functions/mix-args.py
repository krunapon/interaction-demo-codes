def print_everything(name,
 time="morning", *args, **kwargs):
    print("Good %s, %s." % (time, name))

    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print("%s: %s" % (k, v))


print_everything("Manee")
print_everything("Mana", "evening", "coffee", "milk", coffee="black coffee",
                 milk="hazelnut milk")

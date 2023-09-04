def print_args(*args):
    for arg in args:
        print(arg, end = ' ')
    print()


my_list = ["one", "two", "three"]
print_args(*my_list)

my_dict = {"name": "Jane", "surname": "Doe"}


def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print("%s: %s" % (k, v))
    print(my_dict["name"], my_dict["surname"])
    print(kwargs["name"], kwargs["surname"])


print_kwargs(**my_dict)




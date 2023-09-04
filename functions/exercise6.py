
def make_greeting2(**kwargs):
    for k, v in kwargs.items():
        if k == "formal":
            if v is True:
                fullname = "%s %s" % (my_dict["name"],
                                      my_dict["surname"])
        else:
            fullname = my_dict["name"]
        if k == "time":
            if v is None:
                greeting = "Hello"
            else:
                greeting = "Good %s" % v
    return "%s, %s!" % (greeting, fullname)


def make_greeting(title, name, surname, formal=True, time=None):
    if formal:
        fullname = "%s %s" % (title, surname)
    else:
        fullname = name
    if time is None:
        greeting = "Hello"
    else:
        greeting = "Good %s" % time
    return "%s, %s!" % (greeting, fullname)

my_dict = {
    "title": "Mr",
    "name": "John",
    "surname": "Smith",
    "formal": False,
    "time": "evening",
}

print(make_greeting("Mr", "John", "Smith"))
print(make_greeting("Mr", "John", "Smith", False))
print(make_greeting("Mr", "John", "Smith", False, "evening"))
print(make_greeting("Mr", "Mana", "Deejai", True, None))
print(make_greeting2(**my_dict))

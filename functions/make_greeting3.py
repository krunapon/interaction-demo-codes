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


print(make_greeting(title="Mr", name="John", surname="Smith"))
print(make_greeting(title="Mr", name="John", surname="Smith",
                    formal=False, time="evening"))
# this is OK
print(make_greeting("Mr", "John", surname="Smith"))
# this will give you an error
#print(make_greeting(title="Mr", "John", "Smith"))
print(make_greeting(surname="Smith", name="John", title="Mr"))
print(make_greeting("Mr", "John", "Smith", time="evening"))


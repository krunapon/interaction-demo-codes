person = {}

for prop in ["name", "surname", "age", "height", "weight"]:
    person[prop] = input("Please enter your %s: " % prop)

print(person)

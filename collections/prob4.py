univ_names = {}
while True:
    name = input("Enter short university name:")
    if name == "quit":
        break
    full_name = input("Enter full university name:")
    if name in univ_names:
        f_name = univ_names[name]
        print(f"{name} is already mapped to {full_name}")
    else:
        univ_names[name] = full_name

print(univ_names)

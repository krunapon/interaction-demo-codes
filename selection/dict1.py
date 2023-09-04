course_code = input("Please enter course code:")
DEPARTMENT_NAMES = {
    "CSC": "Computer Science",
    "MAM": "Mathematics and Applied Mathematics",
    "STA": "Statistical Sciences", # Trailing commas like this are allowed in Python!
}

if course_code in DEPARTMENT_NAMES: # this tests whether the variable is one of the dictionary's keys
    print("Department: %s" % DEPARTMENT_NAMES[course_code])
else:
    print("Unknown course code: %s" % course_code)

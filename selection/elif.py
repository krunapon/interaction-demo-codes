mark = 90
if mark >= 80:
    grade = 'A'
elif mark >= 65:
    grade = 'B'
elif mark >= 50:
    grade = 'C'
else:
    grade = 'D'
print("mark is %d grade is %s" % (mark, grade))

ids = [6, 12, 21, 3]
for id in ids:
    if id < 10:
        student_id = "s_00" + str(id)
    else:
        student_id = "s_0" + str(id)
    print(student_id)

student_name = input("Please enter a student name: ")
midterm_mark = float(input("Please enter the student's midterm exam mark (0-100): "))
final_mark = float(input("Please enter the student's final exam mark (0-100): "))
MIDTERM_WEIGHT = 0.4
FINAL_WEIGHT = 0.6
mark = MIDTERM_WEIGHT * midterm_mark + FINAL_WEIGHT * final_mark
if 80 <= mark <= 100:
	grade = "A"
elif 70 <= mark < 80:
        grade = "B"
elif 60 <= mark < 70:
        grade = "C"
elif 50 <= mark < 60:
        grade = "D"
else:
        grade = "F"

print("%s has total mark as %.2f and grade as %s" % (student_name, mark, grade))

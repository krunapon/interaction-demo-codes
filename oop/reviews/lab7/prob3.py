class KKUStudent:
    students_list = []

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        KKUStudent.students_list.append(self)

    def graduate(self):
        print("{} has graduated.".format(self.name))
        KKUStudent.students_list.remove(self)

        if len(KKUStudent.students_list) == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} students registered.".format(
                len(KKUStudent.students_list)))


    def display(self):
        """Greeting by the robot"""
        print("My name is {} and now I have GPA as {}".format(self.name, self.gpa))

    @classmethod
    def print_students(cls):
        """Prints the current list of students"""
        print("=== The current list of students is as following ===")
        for s in cls.students_list:
            s.display()

    def __lt__(self, other):
        # s1 < s2 calls s1.__lt__(s2)
        return self.gpa < other.gpa

    def __eq__(self, other):
        # s1 == s2 calls s1.__lt__(s2)
        return self.gpa == other.gpa

manee = KKUStudent('Manee', 3.2)
mana = KKUStudent('Mana', 3.4)
chujai = KKUStudent('Chujai', 2.8)
KKUStudent.print_students()
print("=== Now let's sort students by their GPA ===")
sorted_students = sorted(KKUStudent.students_list)
for s in sorted_students:
    s.display()
manee.graduate()
KKUStudent.print_students()


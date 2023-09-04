class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def description(self):
        print("{} {} {}".format(self.number, self.name, self.surname))

class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)
    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)

    def description(self):
        print("=== Student ===")
        super(Student, self).description()
        print("Classes are {}".format(self.classes))


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)

    def description(self):
        print("=== Lecturer ===")
        super(Lecturer, self).description()
        print("Courses taught are {}".format(self.courses_taught))

jane = Student(Student.POSTGRADUATE, "Jane", "Smith", "SMTJNX045")
jane.enrol("PhD Seminar 1")
jane.description()
bob = Lecturer(StaffMember.PERMANENT, "Bob", "Jones", "123456789")
bob.assign_teaching("Object-oriented programming")
bob.description()

from student import Student
from teacher import Teacher

students = []
teachers = []

def add_student(name, student_id):
    student = Student(name, student_id)
    students.append(student)

def add_teacher(name, teacher_id):
    teacher = Teacher(name, teacher_id)
    teachers.append(teacher)

def display_all_students():
    print("---- Students ----")
    for student in students:
        student.display_info()
        print()

def display_all_teachers():
    print("---- Teachers ----")
    for teacher in teachers:
        teacher.display_info()
        print()


add_student("Büşra Tozak", 1)
students[0].add_course("Math")
students[0].add_course("Science")

add_student("Betül Ön", 2)
students[1].add_course("Math")
students[1].add_course("Science")

add_student("Sihamettin Kaya", 3)
students[2].add_course("History")
students[2].add_course("English")

add_teacher("Merve Alpagat", 101)
teachers[0].add_class("Math")
teachers[0].add_class("Science")

add_teacher("Fatma Tanır", 102)
teachers[1].add_class("History")
teachers[1].add_class("English")

display_all_students()
display_all_teachers()

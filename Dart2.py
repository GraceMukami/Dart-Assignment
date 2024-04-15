class Student:
    def __init__(self, name, age, grade_level):
        self.name = name
        self.age = age
        self.grade_level = grade_level

    def print_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade Level: {self.grade_level}")


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def print_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")


class School:
    def __init__(self):
        self.student = None
        self.teacher = None

    def create_student(Self, name, age, grade_level):
        self.student = Student(name, age, grade_level)

    def create_teacher(self, name, age, subject):
        self.teacher = Teacher(name, age, subject)

    def print_info(self):
        if self.student:
            print("Student Information:")
            self.student.print_info()
        else:
            print("No student information available.")
        
        if self.teacher:
            print("\nTeacher Information:")
            self.teacher.print_info()
        else:
            print("No teacher information available.")



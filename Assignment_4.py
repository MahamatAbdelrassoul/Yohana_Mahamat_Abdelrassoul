# Assignment 4:
#University System Display infomation of
#Classes: Person (parent), and subclasses Student, Lecturer, Staff.

# The Person class is the base class.
# Student, Lecturer, and Staff inherit from Person and add their own attributes.
# Each class has a display_info method to show its information.


# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f'Student ID: {self.student_id}, Course: {self.course}')

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, lecturer_id, department):
        super().__init__(name, age)
        self.lecturer_id = lecturer_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f'Lecturer ID: {self.lecturer_id}, Department: {self.department}')

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f'Staff ID: {self.staff_id}, Position: {self.position}')

# Create objects and display their information
student = Student('Andrew', 22, '2300723456', 'Software Engineering')
lecturer = Lecturer('Dr. Kanagwa', 45, 'LEC456', 'Network')
staff = Staff('Mr. Samuel', 35, 'STF789', 'Administrator')

print('\n--- Student Information ---')
student.display_info()
print('\n--- Lecturer Information ---')
lecturer.display_info()
print('\n--- Staff Information ---')
staff.display_info()

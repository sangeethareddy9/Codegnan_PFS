class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived Class - Student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        print("\nStudent Details")
        self.display_person()
        print("Student ID:", self.student_id)
        print("Course:", self.course)


# Derived Class - Professor
class Professor(Person):
    def __init__(self, name, age, emp_id, course):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.course = course
        self.students_assigned = []

    def assign_student(self, student):
        self.students_assigned.append(student)

    def display_professor(self):
        print("\nProfessor Details")
        self.display_person()
        print("Professor ID:", self.emp_id)
        print("Course Teaching:", self.course)
        print("Number of Students Assigned:", len(self.students_assigned))

        print("\nAssigned Students:")
        for student in self.students_assigned:
            print(student.name, "-", student.student_id, "-", student.course)


# University Class
class University:
    def __init__(self, university_name, university_id, location):
        self.university_name = university_name
        self.university_id = university_id
        self.location = location

    def display_university(self):
        print("University Details")
        print("University Name:", self.university_name)
        print("University ID:", self.university_id)
        print("Location:", self.location)


# Object creation
university1 = University("Alliance University", "UNI101", "Hyderabad")

student1 = Student("Kundana", 20, "PFS01", "Python Programming")
student2 = Student("Rahul", 21, "PFS02", "Python Programming")
student3 = Student("Sneha", 19, "PFS03", "Python Programming")

professor1 = Professor("Bhanu", 40, "45673", "Python Programming")

# Assign students to professor
professor1.assign_student(student1)
professor1.assign_student(student2)
professor1.assign_student(student3)

# Display details
university1.display_university()
student1.display_student()
student2.display_student()
student3.display_student()
professor1.display_professor()

class College:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.faculty = {}

    def add_student(self, student_id, name, age, department):
        self.students[student_id] = {
            'name': name,
            'age': age,
            'department': department,
            'courses': []
        }

    def add_course(self, course_id, course_name, faculty_id):
        self.courses[course_id] = {
            'course_name': course_name,
            'faculty_id': faculty_id,
            'students': []
        }

    def add_faculty(self, faculty_id, name, department):
        self.faculty[faculty_id] = {
            'name': name,
            'department': department,
            'courses': []
        }

    def enroll_student(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            self.students[student_id]['courses'].append(course_id)
            self.courses[course_id]['students'].append(student_id)
        else:
            print("Invalid student ID or course ID.")

    def assign_faculty_to_course(self, faculty_id, course_id):
        if faculty_id in self.faculty and course_id in self.courses:
            self.faculty[faculty_id]['courses'].append(course_id)
            self.courses[course_id]['faculty_id'] = faculty_id
        else:
            print("Invalid faculty ID or course ID.")

    def get_student_details(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Department: {student['department']}")
            print("Enrolled Courses: ", student['courses'])
        else:
            print("Student not found.")

    def get_course_details(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            print(f"Course ID: {course_id}")
            print(f"Course Name: {course['course_name']}")
            print(f"Faculty ID: {course['faculty_id']}")
            print("Enrolled Students: ", course['students'])
        else:
            print("Course not found.")

    def get_faculty_details(self, faculty_id):
        if faculty_id in self.faculty:
            faculty = self.faculty[faculty_id]
            print(f"Faculty ID: {faculty_id}")
            print(f"Name: {faculty['name']}")
            print(f"Department: {faculty['department']}")
            print("Assigned Courses: ", faculty['courses'])
        else:
            print("Faculty not found.")

# Example usage
college = College()

# Adding students
college.add_student(1, 'Alice', 20, 'Computer Science')
college.add_student(2, 'Bob', 22, 'Mechanical Engineering')

# Adding courses
college.add_course(101, 'Data Structures', 1)
college.add_course(102, 'Thermodynamics', 2)

# Adding faculty
college.add_faculty(1, 'Dr. Smith', 'Computer Science')
college.add_faculty(2, 'Dr. Johnson', 'Mechanical Engineering')

# Enrolling students in courses
college.enroll_student(1, 101)
college.enroll_student(2, 102)

# Assigning faculty to courses
college.assign_faculty_to_course(1, 101)
college.assign_faculty_to_course(2, 102)

# Getting details
college.get_student_details(1)
college.get_course_details(101)
college.get_faculty_details(1)

from student import student
from courses import courses


class sys_management:
    def __init__(self) -> None:
        self.students = []
        self.courses = []
        self.mark = {}

    def add_student(self, num):
        for i in range(num):
            id = input("enter the student id: ")
            name = input("enter the student name: ")
            dob = input("enter the DOB: ")
            new_student = student(id, name, dob)
            self.students.append(new_student)

    def add_courses(self, num):
        for i in range(num):
            course_id = input("Enter Course ID :")
            course_name = input("Enter Course Name :")

            new_courses = courses(course_id, course_name)
            self.courses.append(new_courses)

    def display_students(self):
        print("list of student: ")
        for student in self.students:
            print(f"{student.id},{student.name},{student.dob}")

    def display_courses(self):
        print("list of courses: ")
        for course in self.courses:
            print(f"{course.id},{course.name}")

    def input_student_marks(self):
        print("\nSelect a student:")
        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student.name}")

        student_index = int(input("Enter the student's index: ")) - 1
        selected_student = self.students[student_index]

        print("\nSelect a course:")
        for index, course in enumerate(self.courses, start=1):
            print(f"{index}. {course.name}")

        course_index = int(input("Enter the course's index: ")) - 1
        selected_course = self.courses[course_index]

        mark = float(
            input(
                f"Enter the marks for {selected_student.name} in {selected_course.name}: "
            )
        )

        key = (selected_student.id, selected_course.id)
        self.mark[key] = mark

    def showStudentMarks(self):
        print("\nSelect a student:")
        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student.name}")

        student_index = int(input("Enter the student's index: ")) - 1
        selected_student = self.students[student_index]

        print("\nSelect a course:")
        for index, course in enumerate(self.courses, start=1):
            print(f"{index}. {course.name}")

        course_index = int(input("Enter the course's index: ")) - 1
        selected_course = self.courses[course_index]

        key = (selected_student.id, selected_course.id)

        if (
            key in self.mark
        ):  # check if marks are available for the selected student and course
            print(
                f"{selected_student.name}'s marks in {selected_course.name}: {self.mark[key]}"
            )
        else:
            print(
                f"No marks available for {selected_student.name} in {selected_course.name}"
            )

    def run(self):
        student_num = int(input("enter the number of students in the class: "))
        self.add_student(student_num)
        courses_num = int(input("enter the number or course: "))
        self.add_courses(courses_num)

        while True:
            print("\nStudent Mark Management System")
            print("1. Input Student Marks")
            print("2. List Courses")
            print("3. List Students")
            print("4. Show Student Marks for a Given Course")
            print("5. Exit")
            choice = int(input("enter your choice: "))
            if choice == 1:
                self.input_student_marks()
            elif choice == 2:
                self.display_courses()
            elif choice == 3:
                self.display_students()
            elif choice == 4:
                self.showStudentMarks()
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main = sys_management()
    main.run()

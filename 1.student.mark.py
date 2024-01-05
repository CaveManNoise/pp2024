def inputNumberOfStudents(): # input the number of students in the class
    return int(input("Enter the number of students in the class: "))

def inputStudentInformation(): # input student information: ID, name, and date of birth
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth: ")
    return {'id': student_id, 'name': name, 'dob': dob}

def inputNumberOfCourses(): # input the number of courses
    return int(input("Enter the number of courses: "))

def inputCourseInformation(): # input course information: ID and name
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return {'id': course_id, 'name': name}

def inputStudentMarks(students, courses, marks): # input student marks for a selected course
    print("\nSelect a student:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}")

    student_index = int(input("Enter the student's index: ")) - 1
    selected_student = students[student_index]

    print("\nSelect a course:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course['name']}")

    course_index = int(input("Enter the course's index: ")) - 1
    selected_course = courses[course_index]

    mark = float(input(f"Enter the marks for {selected_student['name']} in {selected_course['name']}: "))

    key = (selected_student['id'], selected_course['id']) # use a tuple (student_id, course_id) as the key to store marks in the dictionary
    marks[key] = mark

def listCourses(courses): # list all courses
    print("\nList of Courses:")
    for course in courses:
        print(f"{course['id']}. {course['name']}")

def listStudents(students): # list all students
    print("\nList of Students:")
    for student in students:
        print(f"{student['id']}. {student['name']}")

def showStudentMarks(students, courses, marks): # show student marks for a given course
    print("\nSelect a student:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}")

    student_index = int(input("Enter the student's index: ")) - 1
    selected_student = students[student_index]

    print("\nSelect a course:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course['name']}")

    course_index = int(input("Enter the course's index: ")) - 1
    selected_course = courses[course_index]

    key = (selected_student['id'], selected_course['id'])
    
    if key in marks: # check if marks are available for the selected student and course
        print(f"{selected_student['name']}'s marks in {selected_course['name']}: {marks[key]}")
    else:
        print(f"No marks available for {selected_student['name']} in {selected_course['name']}")

def main():
    students = []
    courses = []
    marks = {}

    # input the number of students and their information
    num_students = inputNumberOfStudents()
    for _ in range(num_students):
        student_info = inputStudentInformation()
        students.append(student_info)

    # input the number of courses and their information
    num_courses = inputNumberOfCourses()
    for _ in range(num_courses):
        course_info = inputCourseInformation()
        courses.append(course_info)

    while True:
        print("\nStudent Mark Management System")
        print("1. Input Student Marks")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Given Course")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            inputStudentMarks(students, courses, marks)
        elif choice == "2":
            listCourses(courses)
        elif choice == "3":
            listStudents(students)
        elif choice == "4":
            showStudentMarks(students, courses, marks)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
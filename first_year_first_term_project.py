# $12.11.2022 - $20.11.2022
# Zeynep Meryem Sertgoz

import os
import time


def wait():
    print("\nYour wish is processing... After the operation please press enter for MENU.\n")
    time.sleep(0.5)


def convert_list_to_file(list1, file):
    with open(file, 'w', encoding="utf-8") as output:
        for i in list1:
            line = ""
            for j in i:
                line = line + j + ";"
            new_line = line.rstrip(";") + "\n"
            output.write(new_line)


def convert_file_to_list(file):
    with open(file, 'r', encoding="utf-8") as output:
        list1 = []
        for line in output:
            line = line.strip("\n")
            line_words = line.split(";")
            list1.append(line_words)
    return list1


def list_courses(file, element_index):
    with open(file, 'r', encoding="utf-8") as output:
        for line in output:
            line_elements = line.split(";")
            print(line_elements[element_index])


while True:
    operation = input(
        "\n MENU "
        "\n Please enter next of the number that operation you want. "
        "\n 1 = List all the courses. "
        "\n 2 = List all the course that have at least one student registered. "
        "\n 3 = Add a new course. "
        "\n 4 = Search a course by course code. "
        "\n 5 = Search a course by name(e.g. if “programming” is entered for a name, you should list all "
        "the courses where their names contain the word “programming”). "
        "\n 6 = Register a student to a course (Hint: This option can take student id and course code as parameters). "
        "\n 7 = List all the students their registered courses. A student will be listed with a blank list even "
        "s/he has not registered for any courses. If a student has registered to courses, you should list those "
        "courses under his/her name. "
        "\n 8 = List top 3 most crowded courses. "
        "\n 9 = List top 3 students with the most course registrations. "
        "\n 10 = Search a student by name or by id."
        "\n 11 = Clear the screen."
        "\n 12 = EXIT \n")
    wait()
    if operation == "1":  # List all the courses.
        list_courses('course.txt', 1)
    elif operation == "2":  # List all the course that have at least one student registered.
        with open('course.txt', 'r') as output:
            for line in output:
                lineElements = line.split(";")
                if int(lineElements[3]) > 0:
                    print(lineElements[1])
    elif operation == "3":  # Add a new course.
        with open('course.txt', 'a', encoding='utf-8') as output:
            courseID = input("Please write the id of new course.")
            courseName = input("Please write the name of new course.")
            courseInstructor = input("Please write the instructor name of new course.")
            courseInfo = courseID + ";" + courseName + ";" + courseInstructor + ";0\n"
            output.write(courseInfo)
    elif operation == "4":  # Search a course by course code.
        course_list = convert_file_to_list('course.txt')
        courseID = input("Please write the id of course.")
        exist = False
        for course in range(len(course_list)):
            if courseID == course_list[course][0]:
                exist = True
                which = course
        if exist:
            print(course_list[which])
        else:
            print("There is no such course.")
    elif operation == "5":  # Search a course by name(e.g. if “programming” is entered for a name, you should list all the courses where their names contain the word “programming”).
        course_list = convert_file_to_list('course.txt')
        courseName = input("Please write the name that you want to search.")
        course = False
        for c in range(len(course_list)):
            if courseName in course_list[c][1] or courseName in course_list[c][1].upper() or courseName in \
                    course_list[c][1].lower():
                print(course_list[c])
                course = True
        if not course:
            print("There is no such course.")
    elif operation == "6":  # Register a student to a course (Hint: This option can take student id and course code as parameters).
        studentID = input("Please write the id of new student.")
        print("Please choose the course below and write the course ID only.")
        list_courses('course.txt', 0)
        courseID = input()
        student_list = convert_file_to_list('student.txt')
        course_list = convert_file_to_list('course.txt')
        is_student_exist = False
        is_course_exist = False
        # for 4 choice as truth table
        for student_id in range(len(student_list)):
            if studentID == student_list[student_id][0]:
                is_student_exist = True
                which_student = student_id
        for course_id in range(len(course_list)):
            if courseID == course_list[course_id][0]:
                is_course_exist = True
                which_course = course_id
        if is_course_exist == False:
            print("A new course? Please first go to 3rd process and add the course.")
        else:
            if is_student_exist == False:
                studentName = input("Please write the name of new student.")
                student_list.append([studentID, studentName, courseID])
            else:
                studentName = student_list[which_student][1]
                try:
                    courseID in student_list[which_student][2]
                    enrolled = True
                except:
                    enrolled = False
                if not enrolled:
                    try:
                        student_list[which_student][2]
                        element = student_list[which_student][2]
                        new_course = "," + courseID
                        student_list[which_student][2] = element + new_course
                    except:
                        student_list[which_student].append(courseID)
                    course_list[which_course][3] = str(int(course_list[which_course][3]) + 1)
                    print("Congratulations, the student enrolled.")
                else:
                    print("This student is already registered this course. :)")
        convert_list_to_file(course_list, 'course.txt')
        convert_list_to_file(student_list, 'student.txt')
    elif operation == "7":  # List all the students their registered courses. A student will be listed with a blank list even s/he has not registered for any courses. If a student has registered to courses, you should list those courses under his/her name.
        student_list = convert_file_to_list("student.txt")
        for student in student_list:
            print("Student : " + student[1])
            print(student[2:])
            print()
    elif operation == "8":  # List top 3 most crowded courses.
        course_list = convert_file_to_list('course.txt')
        for i in range(0, len(course_list)):
            for j in range(0, len(course_list) - i - 1):
                if int(course_list[j][3]) < int(course_list[j + 1][3]):
                    x = course_list[j]
                    course_list[j] = course_list[j + 1]
                    course_list[j + 1] = x
        for i in range(3):
            print(course_list[i][1])
    elif operation == "9":  # List top 3 students with the most course registrations.
        student_list = convert_file_to_list('student.txt')
        for i in range(0, len(student_list)):
            for j in range(0, len(student_list) - i - 1):
                if len(student_list[j]) < len(student_list[j + 1]):
                    x = student_list[j]
                    student_list[j] = student_list[j + 1]
                    student_list[j + 1] = x
        for i in range(3):
            print(student_list[i][0], "-->", student_list[i][1])
    elif operation == "10":  # Search a student by name or by id.
        student_list = convert_file_to_list('student.txt')
        studentName = input("Please write the word that you want to search.")
        student = False
        for c in range(len(student_list)):
            for l in range(len(student_list[c])):
                if studentName in student_list[c][l] or studentName in student_list[c][l].upper() or studentName in \
                        student_list[c][l].lower():
                    print(student_list[c])
                    student = True
        if not student:
            print("There is no student alike.")
    elif operation == "11":  # Clear the screen.
        os.system("cls")
    elif operation == "12":  # EXIT
        os.system("cls")
        break
    else:
        print("Please enter valid process.")
    input("\nPlease press enter for continue")

"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Zakaria Omer Tafesh
Delivery Date : 18-6-2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark


class Student:
    # TODO 3 define static variable indicates total student count

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user_inout)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self):
        pass

    # TODO 5 define a method to enroll new course to student courses list

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        pass

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        pass


# in Global Scope
# TODO 8 declare empty students list

while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:
        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 10 create student object and append it to students list

        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 11 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 14 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 15 call a function to exit the program
        pass

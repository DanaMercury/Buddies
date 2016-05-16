### Assumption: All kids should be prepared to work together and have something to learn from each other
     # Assign students partners
     #      -each kid
     #           *skill: math, reading, science, social studies, other
     #           *skill level: high, medium, low
     #           *social: leader
     #           -support: if paired with {student name}
     #      -evaluation
     #           -kid of partners
     #           -teacher of groups

# import random.choice
import random
import math
from sys import exit
import csv

class Teacher():

    def __init__(self, first_name,last_name):   #pass teacher's first and last name
        self.first_name = first_name
        self.last_name = last_name
        self.classrooms = dict()

    def add_classroom(self, classroom_data):
        self.classrooms["ClassroomID_" + classroom_data[0]] = Classroom(classroom_data[1])

class Classroom():

    def __init__(self, classname):   #need a name for the class e.g., homeroom
        self.class_name = classname
        self.students = dict()

    def add_student(self,student_data):
        self.students["StudentID_" + student_data[0]] = Student(student_data[1], student_data[2])    #Pass student_firstname, student_lastname

    def list_participants(self):     #uses students attribute to print list of students who are present and participating
        participant_list = []
        for k,v in self.students.items():
            if v.attendance == True and v.participation == True:
                participant_list.append(v.studentname)
        return participant_list

    def group_students(self):
        student_groups = []
        groups_wanted = input("How many groups do you want?")
        groups_wanted = int(groups_wanted)
        num_of_kids = len(self.list_participants())
        if num_of_kids <= 1:
            print("There needs to be at least 2 students in your class")
            exit()
        if groups_wanted * 2 - 1 > num_of_kids:
            print("There aren't enough students to have at least 2 groups")
            exit()
        available = self.list_participants()
        if num_of_kids % groups_wanted == 0:
            num_in_group = int((num_of_kids) / (groups_wanted))
            for i in range(groups_wanted):
                picked_kids = random.sample(available, num_in_group)
                student_groups.append(picked_kids)
                for kid in picked_kids:
                    available.remove(kid)
        else:
            approx_groups = ((num_of_kids) / (groups_wanted))
            decision_point = round(approx_groups - int(approx_groups), 1)
            if decision_point <= .5:
                num_in_group = math.floor(approx_groups)
            else:
                num_in_group = math.ceil(approx_groups)
            for i in range(groups_wanted-1):
                picked_kids = random.sample(available, num_in_group)
                student_groups.append(picked_kids)
                for kid in picked_kids:
                    available.remove(kid)
            student_groups.append(available)
        for group in student_groups:
            print(group)

class Student():
### Student Characteristics
    def __init__(self, first, last):    # student's first and last name needed
        self.first = first
        self.last = last
        self.studentname = self.first + "_" + self.last
        self.attendance = True             #default attendance to present
        self.participation = True             #default participation to active

    def change_attendance(self):
        self.attendance = not self.attendance

    def change_participation(self):
        self.participation = not self.participation

teachers = dict()
classroom_teacher = dict()

with open('teachers.csv') as teachersfile, open('classrooms.csv') as classroomsfile, open('students.csv') as studentssfile:
    teachersCSV = csv.reader(teachersfile, delimiter = ",")
    next(teachersCSV, None)
    classroomsCSV = csv.reader(classroomsfile, delimiter=",")
    next(classroomsCSV, None)
    studentsCSV = csv.reader(studentssfile, delimiter=",")
    next(studentsCSV, None)

    for row in teachersCSV:
        teachers["TeacherID_"+row[0]] = Teacher(row[1], row[2])

    for row in classroomsCSV:
        teacherID = "TeacherID_" + row[2]
        if teacherID not in teachers.keys():
            print("Error - the teacher is not in the teachers.CSV", row)
            exit()
        teachers[teacherID].add_classroom(row)
        classroom_teacher["ClassroomID_"+row[0]] = teacherID

    for row in studentsCSV:
        classroomID = "ClassroomID_" + row[4]
        if classroomID not in classroom_teacher.keys():
            print("Error - the classroom is not in the classrooms.CSV", row)
            exit()
        teachers[classroom_teacher[classroomID]].classrooms[classroomID].add_student(row)


testlist = teachers["TeacherID_1"].classrooms["ClassroomID_2"].list_participants()

teachers["TeacherID_1"].classrooms["ClassroomID_2"].students["StudentID_20164"].change_attendance()
teachers["TeacherID_1"].classrooms["ClassroomID_2"].students["StudentID_20163"].change_participation()

print(teachers["TeacherID_1"].classrooms["ClassroomID_2"].list_participants())

teachers["TeacherID_1"].classrooms["ClassroomID_2"].group_students()


"""
for k,v in teachers.items():
    print(k,v.first_name,v.last_name)
    for k,v in v.classrooms.items():
        print(k,v.class_name, v.list_participants)
        for k,v in v.students.items():
            print(k,v.first,v.last,v.attendance,v.participation)
"""
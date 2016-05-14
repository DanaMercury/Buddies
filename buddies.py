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

    def list_participants(self):        #pass list of all students(roster) --> returns list of students who are present and participating
        participant_list = []
        for student in self.students:
            if student.attendance == True and student.participation == True:
                participant_list.append(student)
        return(participant_list)


### Determine how many groups there should be
def req_atleast2kids(num_in_group):
    if num_in_group <= 1:
        print("There needs to be at least 2 kids a group")
        exit()

def req_atleast2groups(num_in_group, num_of_kids):
    if num_in_group * 2 > num_of_kids:
        print("There aren't enough kids to have at least 2 groups")
        exit()

def group_upordown(decision_point, org):
        if decision_point <= .5:
            groups = math.floor(org)
        else:
            groups = math.ceil(org)
        return(groups)

def num_of_groups(classroom, num_in_group): #Determine num of groups based on num of kids and num of kids wanted in each group
        req_atleast2kids(num_in_group)
        num_of_kids = len(classroom)
        req_atleast2groups(num_in_group, num_of_kids)
        if num_of_kids % num_in_group == 0:
            is_divisible = True
            groups = int((num_of_kids) / (num_in_group))
            #print("Make " + str(groups) + " groups, so that " + str(num_in_group) + " kids will be in each group")
        else:
            is_divisible = False
            #print("Not all groups can have " + str(num_in_group) + " kids")
            org = ((num_of_kids) / (num_in_group))
            decision_point = round(org - int(org), 1)
            groups = group_upordown(decision_point, org)
            #print("Divide "+str(num_of_kids)+" kids into "+str(groups)+" groups")
        #print(classroom, num_in_group, is_divisible, groups)
        return(classroom, num_in_group, is_divisible, groups)

### Determine the size of each group
def make_groups(classroom, num_in_group, is_divisible, groups):
        all = []
        if is_divisible == True:
            for i in range(groups):
                picked_kids = random.sample(classroom, num_in_group)
                all.append(picked_kids)
                for kid in picked_kids:
                    classroom.remove(kid)
        else:
            for i in range(groups-1):
                picked_kids = random.sample(classroom, num_in_group)
                all.append(picked_kids)
                for kid in picked_kids:
                    classroom.remove(kid)
            all.append(classroom)
        print(all)
        return(all)



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

"""
for k,v in teachers.items():
    print(k,v.first_name,v.last_name)
    for k,v in v.classrooms.items():
        print(k,v.class_name)
        for k,v in v.students.items():
            print(k,v.first,v.last,v.attendance,v.participation)
"""
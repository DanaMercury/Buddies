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

with open('studentnames.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    list_of_newstudents = []

    firstline = True
    for row in readCSV:
        if firstline:
            firstline = False
            continue
        else:
            newstudent = [row[0], row[1]]
            list_of_newstudents.append(newstudent)

class Teacher():
    def __init__(self, teachersname):   #need the teachers name
        self.classrooms = []

    def add_classroom(self, classroomname):    #Pass Student.studentID, Student.student_info
        self.classrooms.append(classroomname)
        #print("You are the teacher for "+ str(self.classrooms[0]))
        return(self.classrooms)

class Student():
### Student Characteristics
    def __init__(self, first, last):    # student's first and last name needed
        ### need to add studentID as key
        self.first = first
        self.last = last
        self.studentID = self.first + "_" + self.last
        self.attendance = True             #default attendance to present
        self.participation = True             #default participation to active
        self.student_info = [self.studentID, self.attendance, self.participation]

    def change_attendance(self):
        self.attendance = not self.attendance
        self.student_info = [self.studentID, self.attendance, self.participation]

    def change_participation(self):
        self.participation = not self.participation
        self.student_info = [self.studentID, self.attendance, self.participation]

d = dict()

for student in list_of_newstudents:
    objectname = 'Student' + str(student[0])
    first = student[0]
    last = student[1]
    d[objectname] = Student(first, last), first, last

class Classroom():

    def __init__(self, classname):   #need a name for the class e.g., homeroom
        self.students = []
        self.roster = []
        self.participant_list = []

    def add_student(self,studentID, student_info):    #Pass Student.studentID, Student.student_info
        student_tup = (studentID, student_info)
        self.students.append(student_tup)

    def create_roster(self):        #returns list of all students in the class
        for student in self.students:
            self.roster.append(student[1][0])
        #print(self.roster)
        return(self.roster)

    def update_student_changes(self,studentID, student_info):   #pass Student.studentID, Student.student_info
        student_tup = (studentID, student_info)
        for student in self.students:
            if student[1][0] == studentID:
                #print("Found the student")
                i = self.students.index(student)
                self.students[i] = student_tup
            else:
                pass
                #print(str(student) + " is not who I'm looking for")
        return(self.students)

    def list_participants(self):        #pass list of all students(roster) --> returns list of students who are present and participating
        self.create_roster()
        self.participant_list = self.roster
        for student in self.students:
            if student[1][1] == False or student[1][2] == False:
                self.participant_list.remove(student[1][0])
        #print("The participants today are "+str(self.participant_list))
        return(self.participant_list)

"""
    class Team():
        def add_default_team_info(self):  ###pass through a list of number of teams
            for i in self.num_of_teams:
                self.team_name[0] = "Team" + "i"
                self.teams.append(self.team_info)

        def change_team_name(self, oldteamname, newteamname):    ### pass old team name and new team name
            for team in self.teams:
                if oldteamname ==  self.team_name:
                    self.team_name.append(newteamname)
"""

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

#Testing ground

MsMercury = Teacher("Ms.Mercury")
x= MsMercury.add_classroom("Homeroom")
Homeroom = Classroom(x[0])

d.get("StudentDana")[0].change_attendance()

for k,v in d.items():
    Homeroom.add_student(v[0].studentID, v[0].student_info)

#for student in Homeroom.students:
#    print(student)

y = Homeroom.list_participants()
z = (num_of_groups(y, 2))
make_groups(*z)


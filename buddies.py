### Assumption: All kids should be prepared to work together and have something to learn from each other
     # Assign students partners
     #      -each kid
     #           *skill: math, reading, science, social studies, other
     #           *skill level: high, medium, low
     #           *social: leader
     #           -support: if paired with {student name}
     #      -instance
     #           -group size: uneven groups are okay
     #           -groups
     #           *support: if no leader
     #      -evaluation
     #           -kid of partners
     #           -teacher of groups

# import random.choice
import random
import math
from sys import exit

class Student():

    def __init__(self, first, last):    # student's first and last name needed
        ### need to add studentID as key
        self.first = first
        self.last = last
        self.studentID = self.first + " " + self.last
        self.attendance = True             #default attendance to present
        self.participation = True             #default participation to active
        self.student_info = [self.studentID, self.attendance, self.participation]
"""
    def change_attendance(self):
        self.attendance = not self.attendance
        self.student_info = [self.studentID, self.attendance, self.participation]

    def change_participation(self):
        self.participation = not self.participation
        self.student_info = [self.studentID, self.attendance, self.participation]
"""

"""Determine how many groups there should be """
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
        print("Make " + str(groups) + " groups, so that " + str(num_in_group) + " kids will be in each group")
    else:
        is_divisible = False
        print("Not all groups can have " + str(num_in_group) + " kids")
        org = ((num_of_kids) / (num_in_group))
        decision_point = round(org - int(org), 1)
        groups = group_upordown(decision_point, org)
        print("Divide "+str(num_of_kids)+" kids into "+str(groups)+" groups")
    #print(classroom, num_in_group, is_divisible, groups)
    return(classroom, num_in_group, is_divisible, groups)

"""Determine the size of each group"""
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

"""Testing ground"""
Dana = Student("Dana", "Mercury")
Jer = Student("Jeremiah", "Mercury")
Bro = Student("Brocat", "Mercury")
Sis = Student("Nina", "Leon-Guerrero")
Ern = Student("Ernie", "Leon-Guerrero")

LGclassroom = [Dana.student_info[0], Jer.student_info[0], Bro.student_info[0], Sis.student_info[0], Ern.student_info[0]]
Testclassroom = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven"]

x= num_of_groups(Testclassroom, 4)
make_groups(*x)




"""
class Classroom():

    def __init__(self,teachername):   #need a teacher for the classroom
        self.teachername = teachername
        self.students = []
        self.attendance = []
        self.participants = []

    def add_student(self,studentID, student_info):    #Pass Student.studentID, Student.student_info
        student_tup = (studentID, student_info)
        self.students.append(student_tup)
        self.attendance.append(student_tup)
        self.participants.append(student_tup)

    def change_attendance(self, studentID):
        for student in self.students:
            if student[0] == studentID:
                student[1][1] = not student[1][1]
                print("changed attendance")

    def change_participation(self):
        self.participation = not self.participation
        self.student_info = [self.studentID, self.attendance, self.participation]

### Change to update all class info, not just student ###
### Pass through full classlist ###
    def update_student_info(self, studentID, student_info):
        for student in self.students:
            if studentID in self.students:
                self.students.remove(student)
                self.participants.remove(student)
                self.add_student(studentname, studentinfo)

    def print_class_roster(self):
         for student in self.students:
             print(student[1][0])

    #def create_attendance_list(self):
    #    for student in self.students:
    #        if student[1][1] == False:
    #            self.participants.remove(student)
    #    return self.participants

    def print_class_attendance(self):
        for student in self.students:
            print(student[1][0], student[1][1])

    def create_participant_list(self):
        for student in self.participants:
            if student[1][2] == False:
                self.participants.remove(student)
        return self.participants


### Change to update all class info, not just student ###
### Pass through full classlist ###
    def update_participant_list(self, studentname, studentinfo):      ### need to replace studentname with studentID
        for student in self.students:
            if student[0] == studentname:
                self.participants.remove(student)
        self.add_student(studentname, studentinfo)

    def print_participants(self):
        temp = self.create_participant_list()
        for student in self.participants:
            print(student[1][0])


class Team():

    def __init__(self, numonteam, eventname):
        self.numonteam = numonteam
        numonteam = int(numonteam)
        self.eventname = eventname
        self.teams = []
        self.team_info = [self.team_name, self.team_members]


    def pick_team_size(self, participant_list):       #feed in Classroom.participants
        self.num_of_participants = count(self.participant_list)
        if self.num_of_participants % self.numonteam == 0:
            self.num_of_teams = self.num_of_participants/self.numonteam
            print(self.num_of_teams)
            return self.num_of_teams


    def add_default_team_info(self):  ###pass through a list of number of teams
        for i in self.num_of_teams:
            self.team_name[0] = "Team" + "i"
            self.teams.append(self.team_info)


    def change_team_name(self, oldteamname, newteamname):    ### pass old team name and new team name
        for team in self.teams:
            if oldteamname ==  self.team_name:
                self.team_name.append(newteamname)
                ### exit out and stop looking ###



    def place_participants(self):
    #counts num of students in the participant_list and sorts them into random groups
        for team in teams:
            teamname_members = random.choice(3, self.participant_list) #select three from the participant list
            self.participant_list.remove()


# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))


LG = Classroom("Ms. LG")

LG.add_student(Dana.studentID,Dana.student_info)
LG.add_student(Jer.studentID,Jer.student_info)
LG.add_student(Bro.student_info,Bro.student_info)

print(LG.students)
print("")

LG.change_attendance(studentID=Dana.studentID)
print(LG.students)

print("")
LG.change_attendance(studentID=Dana.studentID)
print(LG.students)

### testing of update_student_info

"""
"""
print(Dana.student_info)
#print(Jer.student_info)
#LG.print_class_roster()
LG.print_class_attendance()

print("")

Dana.change_attendance()
#Jer.change_attendance()

LG.update_student_info(Dana.studentname, Dana.student_info)
#LG.update_student_info(Jer.studentname, Jer.student_info)

print(Dana.student_info)
#print(Jer.student_info)

#LG.print_class_roster()
LG.print_class_attendance()
"""

###testing of participant list

"""
LG.create_participant_list()

print(Dana.student_info)
Dana.change_participation()
print(Dana.student_info)


print("")
LG.update_participant_list(Dana.studentID, Dana.student_info)
LG.print_participants()

print("")

print(Dana.student_info)
"""
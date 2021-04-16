import random
import re
import os

NUM_OF_CLASSES = 29

NumberOfStudents = 0
Occupied = [False] * 22
FirstNames = [""] * 22
LastNames = [""] * 22
StudentID = [""] * 22
Absences = [-1] * 22
FinalProject = [-1.0] * 22
Assignments = [-1.0] * 22
Exams = [-1.0] * 2
for i in range(2):
    Exams[i] = [-1.0]*22

def DisplayWelcomeMessage():
    print("*************************************************")
    print("*\t\t\t\t\t\t*")
    print("*\tWelcome\t\t\t\t\t*")
    print("*\tto\t\t\t\t\t*")
    print("*\tCOSC 1330 Computer Programming\t\t*")
    print("*\tRegistration System\t\t\t*")
    print("*\t\t\t\t\t\t*")
    print("*\tClass Size Limit : 22\t\t\t*")
    print("*************************************************")
    print("")
def DisplayCommands():
    print("*********************************")
    print("*  Please select a command :\t*")
    print("* (R)egister\t\t\t*")
    print("* (W)ithdraw\t\t\t*")
    print("* (D)isplay seating chart\t*")
    print("* (V)iew class roster\t\t*")
    print("* (E)nter grades\t\t*")
    print("* (G)rade report\t\t*")
    print("* (L)ist commands\t\t*")
    print("* (Q)uit\t\t\t*")
    print("*********************************")
    print("")
def DisplaySeatingChart():
    name = ""
    print("COSC 1330 Computer Programming Seating Chart\n\n")
    for i in range(11,0,-1):
        var = ()
        name = "Empty"
        if(Occupied[i-1]):
            name = LastNames[i-1] + "," + FirstNames[i-1]
            name = name.upper()
        print(((str(i) + ";") + name).ljust(30),end = "",flush = True)
        print((str(i+11) + ";").rjust(30),end = "",flush = True)
        name = "Empty"
        if(Occupied[i+11-1]):
            name = LastNames[i+11-1] +"," + FirstNames[i+11-1]
            name = name.upper()
        print(name + "\n")
def DisplayClassRoster():
    name = ""
    print("COSC 1330 Computer Programming Class Roster\n")    
    print("Student Name ".ljust(30),end = "",flush = True)
    print("Student ID ".ljust(10),end = "",flush = True)
    print("Seat".rjust(10))
    print("------------".ljust(30),end = "",flush = True)
    print("----------".ljust(10),end = "",flush = True)
    print("----".rjust(11))

    for seat in range(22):
        if Occupied[seat -1]:
            name = LastNames[seat-1] + ", " + FirstNames[seat-1]
            print(name.ljust(30),end = "",flush = True)
            print(StudentID[seat-1].ljust(10),end = "",flush = True)
            print(str(seat).rjust(11))
    return
def IsRegistered(ID):
    for i in range(22):
        if StudentID[i] == ID:
            return True
    return False
def GetSeat(ID):
    for i in range(23):
        if StudentID[i] == ID:
            return i+1
    return 0
def DisplayGradeReport():
    seat = 0
    name = ""
    ID = GetStudentID()
    ast = "******"
    avg = 0.0
    if IsRegistered(ID):
        seat = GetSeat(ID)
        name = str(LastNames[seat-1] + ", " + FirstNames[seat-1]).upper()
        print("Grade Report for : " + name + " ; Student ID: {}".format(ID))
        if(Absences[seat-1] != -1):
            print("Attendance Average: {}".rjust(25).format(Absences[seat-1]))
        else:
            print("Attendance Average: {}".rjust(25).format(ast))
        if(Assignments[seat-1] != -1.0):
            print("Assignments Average: {}".rjust(25).format(Assignments[seat-1]))
        else:
            print("Assignments Average: {}".rjust(25).format(ast))
        if(Exams[0][seat - 1] != -1.0):
            print("Midterm Exam: {}".rjust(25).format(Exams[0][seat - 1]))
        else:
            print("Midterm Exam: {}".rjust(25).format(ast))
        if(Exams[1][seat -1] != -1.0):
            print("Final Exam: {}".rjust(25).format(Exams[1][seat - 1]))
        else:
            print("Final Exam: {}".rjust(25).format(ast))
        if(FinalProject[seat-1] != -1.0):
            print("Semester Project: {}".rjust(25).format(FinalProject[seat-1]))
        else:
            print("Semester Project: {}".rjust(25).format(ast))
        print("")
        avg = (Absences[seat - 1] * .10) + (Assignments[seat - 1] * .50) + (Exams[0][seat - 1] * .15) + (Exams[1][seat - 1] * .15) + (FinalProject[seat - 1] * .10)
        if Absences[seat - 1] != -1 and Assignments[seat - 1] != -1.0 and Exams[0][seat-1] != -1.0 and Exams[1][seat - 1] != -1.0 and FinalProject[seat - 1] != -1.0:
            print("Final Average:  {}     Final Grade:   {}".format(avg,GetLetterGrade(avg)))
    else:
        print("Error: Student is not registered")
def GetSeatAssignment():
    seat = random.randint(1,22)
    while Occupied[seat-1]:
        seat = (seat + 1)% 22
    return seat + 1
def CheckStudentID(ID):
    pattern = r"[Aa][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
    if(re.search(pattern,ID)):
        return True
    return False
def GetStudentID():
    ID = ""
    while(not CheckStudentID(ID)):
        ID = input(str("Enter Student ID:\n"))
        ID = ID.upper()
        if(CheckStudentID(ID)):
            break
    return ID
def Enroll():
    ID = GetStudentID()
    if(IsRegistered(ID)):
        print("Student is already registered!")
        return
    seat = GetSeatAssignment()
    Occupied[seat-1] = True
    StudentID[seat-1] = ID
    FirstNames[seat-1] = input(str("Enter first name:   "))
    LastNames[seat-1] = input(str("Enter last name:   "))
    global NumberOfStudents
    NumberOfStudents += 1
    return
def Withdraw():
    ID = GetStudentID()
    if(not IsRegistered(ID)):
        print("Student is not registered!")
        return
    seat = GetSeat(ID)
    Occupied[seat-1] = False
    FirstNames[seat-1]  =  ""
    LastNames[seat-1] = ""
    StudentID[seat-1] = ""
    Absences[seat-1] = 0
    FinalProject[seat-1] = -1.0
    Assignments[seat-1] = -1.0
    global NumberOfStudents
    NumberOfStudents -= 1
    return
def SetMidtermExamGrades(ID):
    seat = GetSeat(ID)
    grade = -1.0
    while  grade < 0 or grade > 110:
       grade = IntInput("Enter Midterm Exam Grade as a number")
    Exams[0][seat -1] = grade
def IntInput(Message):
    try:
        var = float(input(Message + ":  "))
        return var
    except:
       return IntInput(Message)
    return -1
def SetFinalExamGrades(ID):
    seat = GetSeat(ID)
    grade = -1
    while  grade < 0 or grade > 110:
        grade = IntInput("Enter Final Exam Grade as a number")
    Exams[1][seat-1] = grade
def SetNumberOfAbsences(ID):
    abs = -1
    seat = GetSeat(ID)
    absAvg = 0.0

    while(abs < 0 or abs > 29):
        abs = IntInput("Enter number of absences as a number")
    absAvg = ((29 - abs)/29) *100
    absAvg = float("{0:.2f}".format(absAvg))
    Absences[seat-1] = absAvg
def SetClassAssignmentsGrade(ID):
    seat = GetSeat(ID)
    grade = -1
    while  grade < 0 or grade > 110:
        grade = IntInput("Enter Class Assignments Grade as a number")
    Assignments[seat-1] = grade
def SetSemesterProjectGrade(ID):
    seat = GetSeat(ID)
    grade = -1
    while  grade < 0 or grade > 110:
        grade = IntInput("Enter Semester Project Grade as a number")
    FinalProject[seat-1] = grade
def GetLetterGrade(average):
    letter = ''
    if(average >= 89.5): letter = 'A'
    elif(average >= 79.5): letter = 'B'
    elif(average >= 69.5): letter = 'C'
    elif(average >= 59.5): letter = 'D'
    elif(average < 59.5): letter = 'F'
    return letter
def EnterGradesMessage():
    print("**************************************************")
    print("* Please select a sub - command:                 *")
    print("*                                                *")
    print( "* (A)bsences                                     *")
    print("* (C)lass assignments                            *")
    print("* (M)idterm exam                                 *")
    print("* (F)inal exam                                   *")
    print("* (S)emester project                             *")
    print("* (L)ist commands                                *")
    print("* (Q)uit                                         *")
    print("**************************************************")
    print("")
def EnterGrades():
  #  os.system('cls')
    command = ''
    ID = GetStudentID()
    if not IsRegistered(ID): 
        print("Error: Student is not currently registered!") 
        return
    EnterGradesMessage()
    while not command == 'q':
        command = str(input("Enter sub-command:  "))
        command = command.lower()
        
        if(command == 'm'): SetMidtermExamGrades(ID)
        elif(command == 'f') : SetFinalExamGrades(ID)
        elif(command == 'a') : SetNumberOfAbsences(ID)
        elif(command == 'c') : SetClassAssignmentsGrade(ID)
        elif(command == 's') : SetSemesterProjectGrade(ID)
        elif(command == 'l') : EnterGradesMessage()
        elif(not command == 'q') : 
            print("Error: Invalid Command - {}".format(command))
    return
def Main():
    command = ''
    DisplayWelcomeMessage()
    DisplayCommands()
    global NumberOfStudents

    while command != 'q':
        command = str(input("\nEnter a command:   "))
        command = command.lower()
        #os.system('cls')

        if command == 'e' :  EnterGrades() 
        elif command == 'g' : DisplayGradeReport()
        elif command == 'd' : DisplaySeatingChart()
        elif command == 'r' :
            if NumberOfStudents == 22:
                print("Error: Class is FULL!")
            else:
                Enroll()
                DisplaySeatingChart()
        elif command == 'w' :
            Withdraw()
            DisplaySeatingChart()
        elif command == 'v' : DisplayClassRoster()
        elif command == 'l' : DisplayCommands()
        elif command != 'q' :
            print("Error: Invalid Command - {}".format(command))
            DisplayCommands()
    return
Main()
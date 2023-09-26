def NOnumbers(inputString):
    return any(char.isdigit() for char in inputString) #def for the validation disallow numbers 



def getStudentDetails(): # user input recall later
    while True:
        first_name = input(" Student's name :") 
        surname = input(" Student's surname :")
        if(len(first_name) == 0 or len(surname) == 0 or NOnumbers(first_name) or NOnumbers(surname) ): # validation user must enter name cant  
            print('Please enter a valid student name without numbers:')          #leave it blank and enter, numbers also not allowed
            continue
        else:
            break
    return first_name, surname

def isStudentInDB(student_list, first_name, surname): # checks if student is in datbase
    for student in student_list:
        if student[0] == first_name and student[1] == surname:
            return True
    return False 
def inputValidGrade():
    valid_inputs  = ['A','B','C','D']
    while True:
        grade = input('Please enter a grade (A/B/C/D) : ') # user input line for grade
        grade = grade.upper()
        if grade not in valid_inputs: # validation 
            print('Invalid Grade')
            continue
        else:
            break
    return grade

def inputValidCreditHours():
    while True:
        try:
            credit_hours = float(input('Please enter credit hours (>0) : ')) # get credit hours
        except (TypeError, ValueError):
            print('Invalid credit hours')
            continue
        if(credit_hours < 0):
            print('Invalid credit hours')
            continue
        else:
            break
    return credit_hours
            
def getStudentDetailsInDB(student_list):
    while(True):
        first_name, surname = getStudentDetails()   
        if(not isStudentInDB(student_list, first_name, surname)): # check if student in db
            print('Student not in DB')
            continue
        else:
            break
    return first_name, surname

def main(student_list): # the main function
    choice = 'C'
    grade_dic = {'A':4.0, 'B':3.0,'C':2.0,'D':1.0} # grade to mark mapper
    while(choice!='X'): # until user quits
       #------------ print(student_list) # show db at each instance used for debugging whats in list-  --#
        choice = input("Choose A, R, L, or G ('X' for exit) : ") # make choice upper case
        choice = choice.upper()
        if(choice == 'A'): # add student
            first_name, surname = getStudentDetails()   # get details    
            print('Student ' + first_name + ' ' + surname + ' has been added')
            if [first_name,surname,0,0] in student_list:
                print('Student '+ first_name + ' ' + surname + '  already exists') # message validation for existing student
                continue
            else:
                student_list.append([first_name,surname,0,0]) # add student with inital QP and credit as 0 
        if(choice == 'L'): # display db                       # prevents previous errors in the program and none is displayed 
            
            sort_studs = sorted(student_list,key=lambda x: x[2]/(x[3]+1), reverse=True) # sorted with greater GPA

            for student in sort_studs: # print sorted results
                try:
                    print(student[1]+', '+student[0] + ' - GPA : ' + str(round(student[2]/float(student[3]),2)))
                except ZeroDivisionError:
                    print(student[1]+', '+student[0] + ' - GPA : ' + "None") # surname first as specified

        if(choice =='R'): # remove from db
            first_name, surname =getStudentDetails()      
            if(not isStudentInDB(student_list, first_name, surname)): # check if student in db
                print('Student not found')
                continue
            else:
                for i in range(0,len(student_list)):
                    if student_list[i][0] == first_name and student_list[i][1]==surname:
                        del student_list[i] # delete student if in dp
                        print('Student ' + first_name + ' ' + surname + ' has been removed!')
                        break

        if(choice == 'G'): # add grade
            first_name, surname = getStudentDetailsInDB(student_list)   
            grade = inputValidGrade() # get grade and validate it
            credit_hours = inputValidCreditHours()
            for i in range(0,len(student_list)):
                if student_list[i][0] == first_name and student_list[i][1] == surname:
                    QP = grade_dic[grade] * credit_hours # calculate QP
                    student_list[i][2] = student_list[i][2] + QP # add QP
                    student_list[i][3] = student_list[i][3] + credit_hours # add credit hours
                    print(str(QP) + '  QPs added to ' + first_name + ' ' + surname)
                    break
            
        
                   

        if(choice == 'X'):
            print('Thank You ! Good bye')
            
if __name__ == "__main__": 
    student_list = []
    main(student_list)

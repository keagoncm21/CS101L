########################################################################
##
## CS 101 Lab
## Program # 2
## Keagon Madison
## kcmc2f@umkc.edu
##
## Algorithm: 1. Get user input for lab, exam, and attendance grades.
##            2. Make sure the inputs are valid numbers with an if statement.
##            3. Calculate the weighted grade and output the grade.             
##            4. Find the letter grade and output the corresponding letter grade.
##
##
## PROBLEM : Program needs to ouput a weighted and letter grade using user input with no numbers above 100 and below 0.
##
## Comments: Program will output weighted and letter grades based on the user input. 
## It also has a built in correction system to make sure the user puts in correct values.
##
########################################################################
print('**** Welcome to the LAB grade calculator! ****\n')
      
name = input('We are calculating grades for ==> ') #Getting the user's name

labs = int(input('\nEnter the Labs grade ==> ')) #Getting lab grade from user
if labs > 100:
    print('The lab value must be 100 or less. It has been changed to 100.')
elif labs < 0:
    print('The lab value must be 0 to 100. It has been changed to 0.')

exams = int(input('\nEnter the Exams grade ==> '))#Getting exams grade from user
if exams > 100:
    print('The exam value must be 100 or less. It has been changed to 100.')
elif exams < 0:
    print('The exam value must be 0 to 100. It has been changed to 0.')

attendance = int(input('\nEnter the Attendance grade ==> '))#Getting attendance grade from user
if attendance > 100:
    print('The attendance value must be 100 or less. It has been changed to 100.')
elif attendance < 0:
    print('The attendance value must be 0 to 100. It has been changed to 0.')

weightGrade = float((labs * .7) + (exams * .2) + (attendance * .1)) #calculating weighted grade
print('\nThe weighted grade for', name,'is:',weightGrade, '%') #outputting weighted grade as a percentage

letterGrade = 'a' #finding letter grade
if weightGrade >= 90:
    letterGrade = 'A'
elif weightGrade >= 80:
    letterGrade = 'B'
elif weightGrade >= 70:
    letterGrade = 'C'
elif weightGrade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'F'

print('The letter grade for', name,'is: ',letterGrade) #outputting letter grade

print('\n**** Thanks for using the LAB grade calculator! ****')

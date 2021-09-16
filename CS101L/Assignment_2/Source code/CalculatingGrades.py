########################################################################
##
## CS 101 Lab
## Program # 2
## Keagon Madison
## kcmc2f@umkc.edu
##
## PROBLEM : Program needs to ouput a weighted and letter grade using user input.
########################################################################
print('**** Welcome to the LAB grade calculator! ****\n')
      
name = input('We are calculating grades for ==> ')

labs = int(input('\nEnter the Labs grade ==> '))
if labs > 100:
    print('The lab value must be 100 or less. It has been changed to 100.')
elif labs < 0:
    print('The lab value must be 0 t0 100. It has been changed to 0.')

exams = int(input('\nEnter the Exams grade ==> '))
if exams > 100:
    print('The exam value must be 100 or less. It has been changed to 100.')
elif exams < 0:
    print('The exam value must be 0 t0 100. It has been changed to 0.')

attendance = int(input('\nEnter the Attendance grade ==> '))
if attendance > 100:
    print('The attendance value must be 100 or less. It has been changed to 100.')
elif attendance < 0:
    print('The attendance value must be 0 t0 100. It has been changed to 0.')

weightGrade = float((labs * .7) + (exams * .2) + (attendance * .1))
print('\nThe weighted grade for', name,'is:',weightGrade)

letterGrade = 'a'
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

print('The letter grade for', name,'is: ',letterGrade)

print('\n**** Thanks for using the LAB grade calculator! ****')

'''
CS 101 Lab
Program 8 - Weighted Grades
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
A weighted grade calculator needs to be created. It will display the low, high, mean and standard deviation of the scores.
Along with the total weighted grade. 
The program will provide 8 total options in a menu to the user to navigate the program:     1 -Add Test 2 -Remove Test 3 -Clear Tests 4 -Add Assignment 5 -Remove Assignment 6 -Clear Assignments D -Display Scores Q -Quit

ALGORITHM:
There are four functions. usrchoice(), addtest(), removetest(), and display().
usrchoice() displays the options and allows the user to decide on their choice. It returns the input of the choice.
addtest() allows the user to input scores to either their tests or assignments based on what option they chose previously. It returns the input of the score.
removetest() takes one parameter. This parameter is the list from Main. It will remove an option from the list based on what a user inputs, then returns the updated list.
display() takes two parameters. The parameters are both lists. The function will do the math for all the scores. It then will display the scores to the user.
The main function is where all the functions are called.

ERROR HANDLING:
Used plenty of try and except blocks to catch value errors and zero division errors. While loops were also used to keep users from entering things that wouldn't work.

OTHER COMMENTS:
There might be another way to use try and except in display() in order to shorten the amount of lines needed

'''
import math

def usrchoice():
    '''This function displays the options and allows the user to decide on their choice. It returns the input of the choice.'''
    print('Grade Menu:')
    print('1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit')
    userchoice = input('Enter your choice: ')
    if userchoice.isalpha():#if the input is a letter, it is capitalized
        userchoice.upper()
    while userchoice not in ['1','2','3','4','5','6','D','Q']: #the user choice must be one of the given options, otherwise they will be asked again for a valid option.
        print('Invalid option, try again.\n')
        print('1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit')
        userchoice = input('Enter your choice: ')
        if userchoice.isalpha():
            userchoice.upper()
    return userchoice

def addtest():
    '''This function will allow the user to input scores to either their tests or assignments based on what option they chose previously. It returns the input of the score.'''
    x = True
    while x == True:
        try:
            testinput = float(input('Enter a score 0 - 100: ')) 
            while testinput < 0: #test input must be in the valid range. It not, the user will be asked again until a valid option is given.
                print('Value must be in the range 0 - 100.\n')
                testinput = float(input('Enter a score 0 - 100: '))
            x = False
        except ValueError: #if the wrong value is given, the user will be asked again for a new input.
            print('Wrong type of input, try again.\n')
    return testinput

def removetest(tstlist):
    '''This function takes one parameter. This parameter is the list from Main. It will remove an option from the list based on what a user inputs, then returns the updated list.'''
    tlist = tstlist
    x = True
    while x == True:
        try: #the user will put in options until a valid value, is given within the right range of 1-100
            testinput = float(input('Enter a score between 0 - 100 that you wish to remove: '))
            while testinput not in tlist:
                print('\nScore not found.\n')
                return tlist
            while testinput < 0:
                print('Value must be in the range 0 - 100.\n')
                testinput = float(input('Enter a score between 0 - 100 that you wish to remove: '))
                
            x = False
        except ValueError:
            print('Wrong type of input, try again.\n')
    tlist.remove(testinput)
    return tlist

def display(tslist, aslist):
    '''This function takes two parameters. The parameters are both lists. The function will do the math for all the scores. It then will display the scores to the user.'''
    tlist = tslist
    alist = aslist
    testcount = len(tlist)
    assignmentcount = len(alist)
    maxtest = 0
    maxassignment = 0
    mintest = 1000
    minassignment = 1000
    avgtest = 0
    avgassign = 0
    tstd = 0
    astd = 0
    finalscore = 0

    for i in tlist: #iterates through the test list and finds the max, min, and average.
        if i > maxtest:
            maxtest = round(i,2)
        if i < mintest:
            mintest = round(i,2)
        avgtest += i
    
    for i in alist: #iterates through the assignment list and finds the max, min, and average
        if i > maxassignment:
            maxassignment = round(i,)
        if i < minassignment:
            minassignment = round(i,2)
        avgassign += i
    
    finalscore = round( ((avgassign * .4) + (avgtest * .6)), 2) #finds final weighted score
    try: # if the numbers were put in before display was called, this will run through with the correct math, otherwise it will fill in empty spaces with N/A 
        avgtest = round(avgtest/testcount, 2)
    except ZeroDivisionError:
        avgtest = 'N/A'
        stdtest = 'N/A'
        mintest = 'N/A'
        maxtest = 'N/A'
    try:
        avgassign = round(avgassign/assignmentcount, 2)
    except ZeroDivisionError:
        avgassign = 'N/A'
        astd = 'N/A'
        minassignment = 'N/A'
        maxassignment = 'N/A'
    
    if tstd != 'N/A': #gets the standard deviation as long as information was entered previously. 
        for i in tlist:
            tstd += (i - avgtest)**2
        try:
            tstd = round(math.sqrt(tstd / testcount), 2)
        except ZeroDivisionError:
            tstd = 'N/A'
    if astd != 'N/A':
        for i in alist:
            astd += (i - avgassign)**2
        try:
            astd = round(math.sqrt(astd / assignmentcount), 2)
        except ZeroDivisionError:
            astd = 'N/A'

    print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Type', '#', 'Min', 'Max', 'Avg', 'Std'))
    print('{:=<70}'.format(''))
    print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Tests', testcount, mintest, maxtest, avgtest, tstd))
    print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Programs', assignmentcount, minassignment, maxassignment, avgassign, astd))
    print('Weighted grade is {}'.format(finalscore))

if __name__ == '__main__':
    '''The 'Main' function. Where the other functions are called based on choices chosen in the usrchoice() function'''
    runagain = True
    testlist = []
    assignmentlist = []
    while runagain == True:
        choice = usrchoice()
        if choice == '1':
            testlist.append(addtest())
        elif choice == '2':
            testlist = removetest(testlist)
        elif choice == '3':
            print('\nTests Cleared.\n')
            testlist.clear()
        elif choice == '4':
            assignmentlist.append(addtest())
        elif choice == '5':
            assignmentlist = removetest(assignmentlist)
        elif choice == '6':
            print('\nAssignments Cleared.\n')
            assignmentlist.clear()
        elif choice == 'D':
            display(testlist, assignmentlist)
        elif choice == 'Q':
            runagain = False
            print('\nHave a great day!')
        print()

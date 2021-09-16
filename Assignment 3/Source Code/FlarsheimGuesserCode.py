########################################################################
##
## CS 101 Lab
## Program 3
## Name: Keagon Madison
## Email: kcmc2f@umkc.edu
##
## PROBLEM : The program must figure out what number a user chooses using remainders 
##           (3,5,7) given by the user.
##
## ALGORITHM : 
##      1. Create a while loop to allow the user to replay
##      2. Ask user for a number 1-100 
##      3. Use while loop to check if valid
##      4. Ask user for remainder of the number by 3. Use while loop to validate.
##      5. Ask user for remainder of the number by 5. Use while loop to validate.
##      6. Ask user for remainder of the number by 7. Use while loop to validate.
##      7. Create a while loop to check if the guess is == to the user number or not.
##      8. Make a for loop within the while loop to go through all the numbers 1 - 100
##      9. Use if statements in the for loop to see if the remainders match up with the user remainders.
##      10. Ask user if they'd like to play again. Use a while loop to validate their answer.
##
## ERROR HANDLING:
##      There are several while loops used to make sure the user input is within certain parameters for the program to work without issues.
##
## OTHER COMMENTS:
##      The program had to be made up of several while loops in order to provide all the error handling necessary. 
##      In the end, a majority, if not all errors are handled by the program. 
##      Could maybe come back to the program when I have more knowledge to handle the errors in a better and/or more simple way.
########################################################################
again = 'Y'
#this while loop is what allows the user to play again based on there answer == 'Y' or not
while again == 'Y':
    guess = -1
    print('* * *Welcome to the Flarsheim Guesser!* * *\n')
    userNum = int(input('Choose a number from 1 to 100: '))

    #Makes sure the userNum is not greater than 100 or less than 1
    while (userNum > 100) or (userNum < 1):
        print('Your number is not a number from 1 to 100. Try again.')
        userNum = int(input('Choose a number from 1 to 100: '))

    print()
    #Getting user input for the remainder of the number when divided by 3.
    #Includes error handling to make sure the remainder is a possible number.
    rem3 = int(input('What is the remainder of your number when divided by 3?: '))
    while (rem3 > 2) or (rem3 < 0):
        if rem3 > 2:
            print('The remainder must be less than 3.\n')
        else:
            print('The remainder must be 0 or greater.\n')
        rem3 = int(input('What is the remainder of your number when divided by 3?: '))
        print()
    
    #Getting user input for the remainder of the number when divided by 5.
    #Includes error handling to make sure the remainder is a possible number.
    rem5 = int(input('What is the remainder of your number when divided by 5?: '))
    while (rem5 > 4) or (rem3 < 0):
        if rem5 > 4:
            print('The remainder must be less than 5.\n')
        else:
            print('The remainder must be 0 or greater.\n')
        rem5 = int(input('What is the remainder of your number when divided by 5?: '))
        print()

    #Getting user input for the remainder of the number when divided by 7.
    #Includes error handling to make sure the remainder is a possible number.
    rem7 = int(input('What is the remainder of your number when divided by 7?: '))
    while (rem7 > 6) or (rem7 < 0):
        if rem7 > 6:
            print('The remainder must be less than 7.\n')
        else:
            print('The remainder must be 0 or greater.\n')
        rem7 = int(input('What is the remainder of your number when divided by 7?: '))
        print()

    # This is the part that guesses what the number is by comparing each 
    # number between 1 - 100 with the remainders given by the user
    while guess != userNum:
        for i in range(0,101):
            if (i % 3) == rem3:
                if (i % 5) == rem5:
                    if (i % 7) == rem7:
                        guess = i
                        print('Your number is {}'.format(guess))
                
    # Asks user if they would like to play again or not. If a letter other 
    # than Y or N is chosen, it asks for the user to try again
    again = input('\nWould you like to play again? (Y or N): ')
    while (again != 'Y') and (again != 'N'):
        print('{} is not a valid answer.\n'.format(again))
        again = input('Would you like to play again? (Y or N): ')
    print()
                    
print('\n* * *Thanks for playing!* * *')
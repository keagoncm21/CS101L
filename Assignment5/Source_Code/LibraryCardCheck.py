########################################################################
##
## CS 101 Lab
## Program # 5
## Name: Keagon Madison
## Email: kcmc2f@umkc.edu
##
## PROBLEM : A library card must be verified based on its digits and characters and the index of those digits and characters. 
##
## ALGORITHM : 
##      1. The program will use multiple functions to check if library cards are valid.
##      2. The user will enter their library card in the main function.
##      3. The card number will be put through a series of functions all checking each individual part of the card.
##      4. If the card has numbers/characters that are not valid, the program will proceed to inform the user what is invalid.
##      5. The user will be given a chance to re-enter their card or enter another card and the program will continue to see if the cards are valid.
##
##
## ERROR HANDLING:
##      Had to check if the values were characters or not within the get_check_digit function to purposefully throw off the equation.
##      A lot of if/else statements to make sure characters are valid and match what they need to be.
## OTHER COMMENTS:
##      Can probably go back later with real error handling to make the code more viable.
##
########################################################################


import string


def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    value = string.ascii_uppercase.index(char)
    return value

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    zero = character_value(idnumber[0])
    one = character_value(idnumber[1])
    two = character_value(idnumber[2])
    three = character_value(idnumber[3])
    four = character_value(idnumber[4])
    five = idnumber[5]
    if five.isalpha():#checks if the values are chars
        five = 11
    six = idnumber[6]
    if six.isalpha():
        six = 11
    seven = idnumber[7]
    if seven.isalpha():
        seven = 11
    eight = idnumber[8]
    if eight.isalpha():
        eight = 11
    checkdigit = (1 * zero + 2 * one + 3 * two + 4 * three + 5 * four + 6 * int(five) + 7 * int(six) + 8 * int(seven) + 9 * int(eight)) % 10
    return checkdigit


def is_valid(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if 11 in (idnumber[5], idnumber[6], idnumber[7], idnumber[8]):
        return False
    if idnumber[9].isalpha() == True:
        return False
    if (get_check_digit(idnumber) != int(idnumber[9])):
        return False
    else:
        return True
    


def verify_check_digit(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    
    if len(idnumber) != 10: #makes sure the length is correct
        return False, 'The length of the number given must be 10'

    elif (idnumber[0].isalpha() and idnumber[1].isalpha() and idnumber[2].isalpha() and idnumber[3].isalpha() and idnumber[4].isalpha()) != True: #makes sure the first characters are letters
        counter = 0
        index = 0
        character = ''
        for i in idnumber:
            if True != i.isalpha():
                character = idnumber[counter]
                break
            counter += 1 
        return False, 'The first 5 characters must be A-Z, the invalid character at {} is {}'.format(counter, character)

    elif (idnumber[5] not in ('1','2','3')) or (idnumber[5].isalpha() == True): #Makes sure the sixth character is valid
        return False, 'The sixth character must be a 1 2 or 3'
    
    elif (idnumber[6] not in ('1','2','3','4')) or ((idnumber[6].isalpha() == True)): #makes sure the seventh character is valid
        return False, 'The seventh character must be 1 2 3 or 4'

    elif is_valid(idnumber) == False: #checks if the check digit matches.
        return False, 'The check digit {} does not match the calculated value {}'.format(idnumber[9], get_check_digit(idnumber))

    else:
        return True, ''


def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if int(idnumber[5]) == 1:
        return 'School of Computing and Engineering'
    elif int(idnumber[5]) == 2:
        return 'School of Law'
    elif int(idnumber[5]) == 3:
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'


def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    if int(idnumber[6]) == 1:
        return 'Freshman'
    elif int(idnumber[6]) == 2:
        return 'Sophomore'
    elif int(idnumber[6]) == 3:
        return 'Junior'
    elif int(idnumber[6]) == 4:
        return 'Senior'
    else:
        return 'Invalid Grade'




if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        
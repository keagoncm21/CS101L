########################################################################
##
## CS 101 Lab
## Program 4
## Name: Keagon Madison
## Email: kcmc2f@umkc.edu
## Date: 9/30/2021
## PROBLEM : A slot machine needs to be created. There are 3 different reels. The user can enter a total amount of chips and how much they want to wager. 
##          Their wager will be tripled with two matching reels and it will be mulitplied by 10 with 3 matches. At the end their max chips and rounds it took to lose their starting chips will be posted.
##          Then the user will need to be asked if they want to play again. 
##
## ALGORITHM : 
##      1. The program will use a series of functions to perform a majority of the tasks needed to run a slot machine.
##      2. The user will enter the total amount of chips they want and the amount they want to major.
##      3. The slot machine has three reels which will equal random numbers.
##      4. If two numbers are matched, the user entered wager is tripled. If three numbers are matched, the user entered wager is mulitplied by 10.
##      5. If there are no matched numbers, the user will lose their wager.
##      6. The user will be asked if they want to play again if their bank is diminished down to zero. A while loop is in place to check if they want to play again or not.
##      7. The user will also be given stats about their max chips and how many turns it took to lose them all. 
##
## ERROR HANDLING:
##      Had to use .upper() in order to allow for any case of N, NO, Y, or YES. For every user input, I had to use while loops to make sure their input was valid.
##
## OTHER COMMENTS:
##      As is, the program runs fine. For more depth, I could come back to add exit message and a welcome message. I could also probably add slightly better visuals for the reels. 
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    again = input('Would you like to play again?[(Y/YES) or (N/NO)]: ')
    again = again.upper()

    while (again != 'YES') and (again != 'Y') and (again != 'N') and (again != 'NO'): #Checks if the user chose a valid answer
        print('The value entered is not valid.')
        again = input('Would you like to play again?[(Y/YES) or (N/NO)]: ')
        again = again.upper()

    if (again == 'NO') or (again == 'N'): #returns true or false depending on the user's answer
        return False
    else:
        return True 
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How much would you like to wager?: '))
    while (wager > bank) or (wager < 1): #Validates the user's input.
        print('The value must be above zero and less than your total chips.')
        wager = int(input('How much would you like to wager?: '))

    return wager    #was 1        

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1,10) #returns random numbers as random reels
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)

    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc: #this will check for matches of pairs or trios
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    chips = int(input('How many chips would you like to play with?: '))
    while (chips <= 0) or (chips >= 101): #This makes sure the amount of chips entered is valid
        print('That is not a valid amount of chips. The amount must be between 1 and 100 (inclusive).')
        chips = int(input('How many chips would you like to play with?: '))

    return chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3: #calculates payout based on matches
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        originalBank = bank
        maxBank = 0
        lastMax = bank
        spins = 0

        while bank > 0:

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            spins += 1 # adds of the amount of spins

            if bank > lastMax: #compares the max bank to the new bank and if the new bank is larger, the max bank will be replaced.
                lastMax = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", originalBank, "in", spins, "spins")
        print("The most chips you had was", lastMax)
        playing = play_again()
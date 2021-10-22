'''
CS 101 Lab
Program #7
Name: Keagon Madison
Email: kcmc2f@umkc.edu
Start Date: 10/21/2021

PROBLEM:
Program must read through one of two files based on what the user chooses. Then the program must print out lines based on the combined mpg also given by the user.
The program will be full of lots of Try and except blocks to stop any possible exceptions rather than crash the program.

ALGORITHM:
There are three functions, getfile(), getfuelecon()), and getouput().
getfile() retrieves a file based on userinput. It reads the file, and returns it in a way the rest of the program can use it to ouput to the other file.
getfuelecon() asks the user what combined mpg they want in a car. The program validates the user's answer.
getouput() goes through the file from getfile() and then outputs lines of cars to a user decided output file based on the given mpg. 


ERROR HANDLING:
Each function includes try and except blocks to catch errors and allow the program to fix them rather than the program crashes.

OTHER COMMENTS:
There is probably better ways for me to read the file in less lines and take up less space overall. 




'''
def getfile():
    '''function retrieves the file designated by the user to go through the vehicle options'''
    while True:
        try:
            filename = input('Enter file name: ')
            with open(filename) as content: #opens the file given by the user, then closes it after the info is returned
                return [[i.strip() for i in x.strip().split('\t')] for x in content.readlines()] #line makes each line readable to the program, then returns the content

        except FileNotFoundError: #catches errors incase the user enters a wrong file name.
            print('File not found, {}'.format(filename))
        except IOError: #given when there is a failed input or ouput fails
            print('IO error found for file {}'.format(filename))

def getfuelecon():
    '''Function gets the desired combined mpg the user wants'''
    while True:
        try:
            usrmpg = float(input('Enter combined mpg: '))
            while (usrmpg <= 0) or (usrmpg > 100): #when the mpg given by the user matches the requirements it will skip this, if not the program will ask the user to re-enter the information until it is acceptable
                print('Invalid input. Must be between 1 and 100 (inclusive)')
                usrmpg = float(input('Enter combined mpg: '))
            return usrmpg
        except ValueError: #if a wrong value is applied, it will be caught here
            print('Value error for {} has been found. Try again.')
            
def getoutput(mpg, file):
    '''Outputs the vehicles that match requirements to a designated output file'''
    while True: #while loop will continue until there is a break or it is deemed false
        try:
            usrout = input('Enter the name of the file you want to output to: ')
            with open('{}'.format(usrout), 'w') as fout: #opens the file to write. It will close the file when everything in it is done running
                for x in file[1:]:
                    try:
                        if mpg <= float(x[7]): #as long as the mpg of the vehicles in the list have greater or equal combined mpg they will be listed to the user.
                            fout.write('{:<5}{:<40}{:<40}{:>10}.000\n'.format(x[0], x[1], x[2], x[7]))
                    except:#if any error is caught in the file, it will be shown here. 
                        print('Part of file invalid. Could not convert {} {} {}'.format(x[0],x[1],x[2]))
            break
        except IOError: #in case an IO error is caught, the program will inform the user here
            print('IOError, continue on.')        
        

if __name__ == '__main__': # Where the main program resides and runs
    contents = getfile()
    combmpg = getfuelecon()
    getoutput(combmpg, contents)
    
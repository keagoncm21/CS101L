'''
CS 101 Lab
Program 9 - Dictionaries
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
This week you’ll read in a datafile containing crime information for 2019.  
You will need to create the functions given below with the function signature given.  
Function signature means the definition of the name of the function as well as any parameters and return values.  
There will again be a unit test file to assist you.Each one will also show an example in the shell.  
Once you write a function you can just hit F5 and then call the function from the shell to test it with different values.

ALGORITHM:
There are 12 functions. 
month_from_number():Finds the corresponding string to a month's number.
read_in_file():It reads the file given by the user and then outputs the contents of the file.
askfile():Asks the user for a file name and outputs that name.
create_reported_date_dict():takes a list, which is the list of lists returned from the read_in_file function above and returns a dictionary where the key is a date of the year found in index 1, 
    and the value is how many times a crime occurred on that data as read from the file.
create_reported_month_dict():The create_reported_month_dictfunction takes a list, which is the list of lists returned from the read_in_file function above and returns a dictionary where the key is the month of the offense,
     and the value is how many times a crime occurred on that data as read from the file.
create_offense_dict():Function takes a list, and returns a dictionary where the key the offense (Arson, Burglary, etc)
    and the value is how many times that offense occurs.
create_offense_by_zip():This function takes a list, it is the list returned from read_in_file function and returns a dictionary where the key the offense (Arson, Burglary, etc) and the value is another dictionary. 
    This sub dictionary has a key for the zip code, and a value that is how many times this offense occurs in this zip code.
maxmonth():Finds the month with the most amount of crime and returns it.
maxmonthcrime():Returns the amount of crime for the month that has the most
topoffensecount():Gets the crime with the most offenses and finds the number of offenses from that crime. Returns both the crime and the number of offenses.
crimefind():Has the user enter a crime. The function checks to make sure the crime is in the list and returns the user's inputted crime.
printcrime():Prints the offenses of the user given crime per zipcode.
The main function is where all the functions are called.

ERROR HANDLING:
I used a try/except block to catch any filenotfound/IOErrors when getting the file. Other than that I used while loops to catch any other errors.

OTHER COMMENTS:
There's a couple functions I think I could combine with more time and coding knowledge. 

'''

import csv

def month_from_number(monthint):
    '''Finds the corresponding string to a month's number'''
    monthlist = ['January', 'February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    count = 1
    for i in monthlist:
        if count == monthint:
            return str(i)
        count += 1

def read_in_file(userfile):
    '''It reads the file given by the user and then outputs the contents of the file'''
    contentlist = []
    try: #error handling to keep filenotfound and Io errors from stopping the program
       with open(userfile, encoding = 'utf-8') as csvfile: #opens and reads the file
           reader = csv.reader(csvfile)
           for i in reader:
               contentlist.append(i)
       return contentlist
    except FileNotFoundError:
        print('File was not found.')
        return 'Broke'
    except IOError:
       print('IOError found')
       return 'Broke'

def askfile():
    '''Asks the user for a file name and outputs that name'''
    filename = input('Enter a file name: ')
    content = read_in_file(filename)
    while content == 'Broke': #if the readinfile function catches an error when used in this function. It will be called again, until the error is no longer present
        print('Try entering the file name again.')
        filename = input('Enter a file name: ')
        content = read_in_file(filename)
    return content
        
def create_reported_date_dict(csvlist):
    ''' takes a list, which is the list of lists returned from the read_in_file function above and returns a dictionary where the key is a date of the year found in index 1, 
    and the value is how many times a crime occurred on that data as read from the file'''
    dictlist = {}
    klist = csvlist[0].index('Reported_Date')
    for i in csvlist[1:]: #creating new dictionary of reported crime and how much it occured
        if i[klist] in dictlist:
            dictlist[i[klist]] += 1
        if i[klist] not in dictlist:
            dictlist[i[klist]] = 1
    return dictlist

def create_reported_month_dict(csvlist):
    '''The create_reported_month_dictfunction takes a list, which is the list of lists returned from the read_in_file function above and returns a dictionary where the key is the month of the offense,
     and the value is how many times a crime occurred on that data as read from the file.'''
    dictlist = {}
    for i in csvlist[1:]: #creating new dictionary for the crimes in a month.
        month = int(i[1][:2])
        if month in dictlist:
            dictlist[month] += 1
        if month not in dictlist:
            dictlist[month] = 1
    return dictlist

def create_offense_dict(csvlist):
    '''Function takes a list, and returns a dictionary where the key the offense (Arson, Burglary, etc)
    and the value is how many times that offense occurs'''
    crimedict = {}
    klist = csvlist[0].index('Offense')
    for i in csvlist[1:]: #creating a new dictionary that goes through the different offenses and marks the times they occured.
        if i[klist] in crimedict:
            crimedict[i[klist]] += 1
        if i[klist] not in crimedict:
            crimedict[i[klist]] = 1
    return crimedict

def create_offense_by_zip(csvlist):
    '''This function takes a list, it is the list returned from read_in_file function and returns a dictionary where the key the offense (Arson, Burglary, etc) and the value is another dictionary. 
    This sub dictionary has a key for the zip code, and a value that is how many times this offense occurs in this zip code.'''
    zipdict = {}
    for i in csvlist[1:]: #getting offenses per zip code to put in a dictionary
        offense = csvlist[0].index('Offense')
        zipc = csvlist[0].index('Zip Code')
        if i[offense] in zipdict:
            offdict = zipdict[i[offense]]
            if i[zipc] in offdict:
                offdict[i[zipc]] += 1
            if i[zipc] not in offdict:
                offdict[i[zipc]] = 1
        else:
            zipdict[i[offense]] = {i[zipc]:1}
    return zipdict

def maxmonth(cmonth):
    '''Finds the month with the most amount of crime and returns it.'''
    max = 0
    for k,v in cmonth.items():
        if v > max:
            max = k
    return max

def maxmonthcrime(cmonth):
    '''Returns the amount of crime for the month that has the most'''
    max = 0
    for k,v in cmonth.items():
        if v > max:
            max = v
    return max

def topoffensecount(offenses):
    '''Gets the crime with the most offenses and finds the number of offenses from that crime. Returns both the crime and the number of offenses.'''
    amount = 0
    crime = ''
    for k,v in offenses.items():
        if v > amount:
            amount = v
            crime = k
    return (crime, amount)

def crimefind(zipoff):
    '''Has the user enter a crime. The function checks to make sure the crime is in the list and returns the user's inputted crime.'''
    usercrime = input('Enter a crime: ').title()
    while usercrime not in zipoff:
        print('Crime not found. Try another one.')
        usercrime = input('Enter a crime: ').title()
    return usercrime

def printcrime(zipoffs, useroffs):
    '''Prints the offenses of the user given crime per zipcode.'''
    print('{} offenses by Zip Code:'.format(useroffs))
    print('{:<25}{:>25}'.format('Zip Code','# of Offenses'))
    print('{:=<50}'.format(''))
    for k,v in zipoffs[useroffs].items():
        print('{:<25}{:>25}'.format(k, v))

if __name__ == '__main__':
    '''Where a majority of functions are called to put the program together.'''
    content = askfile()
    crimemonth = create_reported_month_dict(content)
    maxedmonth = month_from_number(maxmonth(crimemonth))
    maxedmonthvalue = maxmonthcrime(crimemonth)
    offenses = create_offense_dict(content)
    crimename, crimenumber = topoffensecount(offenses) #unpacking topoffensecount()
    zipoffenses = create_offense_by_zip(content)

    print('The month with the highest number of crimes is {} with {} offenses.'.format(maxedmonth, maxedmonthvalue))
    print('The offense wit hthe highest number of crimes is {} with {} offenses.'.format(crimename, crimenumber))
    print()

    useroffense = crimefind(zipoffenses)
    printcrime(zipoffenses, useroffense)


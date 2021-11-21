'''
CS 101 Lab
Program 11 - Clock Class
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
We’ll use our skills to create a clock class that can keeptrack of hours, minutes and seconds.   
Then you should be able to create an instance with values for hour, minutes and seconds.  
You’ll want to make a new class with a __ini__ method.  
You’ll want to set the attributes for hour, minute, and second in the init.

ALGORITHM:
There is a class called Clock(). This class will have three methods. These methods are __init__, __str__ and tick.
__init__ sets attributes for hour, minute, second, and clocktype.
__str__ returns the time in a 24 hour format style.
tick increments the seconds, minutes, and hours based on the current time.
In the main function the user will enter their inputs for the time and type of clock. A lot of error handling will be used to keep the user's answers on track.
A while loop will be used with the time import to print the time every second. 

ERROR HANDLING:
Several try and excepts are used to catch value errors. While loops will be used as well to repeatedly ask the user for input if the input is invalid.

OTHER COMMENTS:
Some areas could probably shortened by combining while loops or using less in general.
'''
import time #imported to use '.sleep'

class Clock():
    '''Class keeps track of time by the second after the user sets a current time.'''
    def __init__(self,hour,minute,second, clock_type = 0):
        '''Sets attributes for hour, minute, second, and clocktype'''
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def __str__(self):
        '''Returns the time in a 24 hour format style'''
        return ('{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second))

    def tick(self):
        '''Increments the seconds, minutes, and hours based on the current time.'''
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        else:
            return('{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second))
        if self.minute ==60:
            self.minute = 0
            self.hour += 1
        else:
            return('{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second))
        if self.clock_type == 0:
            if self.hour == 24:
                self.hour = 0
        elif self.clock_type == 1: #allows for a 12 hour timer.
            if self.hour == 12:
                self.hour = 0
            
        

if __name__ == '__main__':
    try:
        clocktype = int(input('What type of clock?(1 for 12 hr. 0 for 24 hr.): ')) #gives the option between 12 and 24 hour timer
    except ValueError:
        clocktype = 3
    while clocktype not in (1,0):
        try:
            print('Try again.')
            clocktype = int(input('What type of clock?(1 for 12 hr. 0 for 24 hr.): '))
        except ValueError:
            clocktype = 3


    if clocktype == 0: #if the user chose 0 the following steps occur to allow a 24 hour timer
        try:
            hours = int(input('What is the current hour?: '))
        except ValueError:
            hours = 'g'
        while hours not in (range(0,24)):
            try:
                print('Try again.')
                hours = int(input('What is the current hour?: '))
            except ValueError:
                hours = 'g'
         
        try:
            minutes = int(input('What is the current minute?: '))
        except ValueError:
            minutes = 'g'
        while minutes not in (range(0,60)):
            try:
                print('Try again.')
                minutes = int(input('What is the current minute?: '))
            except ValueError:
                minutes = 'g'

        try:
            seconds = int(input('What is the current second?: '))
        except ValueError:
            seconds = 'g'
        while seconds not in (range(0,60)):
            try:
                print('Try again.')
                seconds = int(input('What is the current second?: '))
            except ValueError:
                seconds = 'g'


    if clocktype == 1:#if the user chose 1 the following steps occur to allow a 12 hour timer
        try:
            hours = int(input('What is the current hour?: '))
        except ValueError:
            hours = 'g'
        while hours not in (range(0,12)):
            try:
                print('Try again.')
                hours = int(input('What is the current hour?: '))
            except ValueError:
                hours = 'g'
         
        try:
            minutes = int(input('What is the current minute?: '))
        except ValueError:
            minutes = 'g'
        while minutes not in (range(0,60)):
            try:
                print('Try again.')
                minutes = int(input('What is the current minute?: '))
            except ValueError:
                minutes = 'g'

        try:
            seconds = int(input('What is the current second?: '))
        except ValueError:
            seconds = 'g'
        while seconds not in (range(0,60)):
            try:
                print('Try again.')
                seconds = int(input('What is the current second?: '))
            except ValueError:
                seconds = 'g'


    times = Clock(hours, minutes, seconds, clocktype)

    while True: #prints the time each time a second goes by infinitely until the user stops the program manually.
        print(times)
        times.tick()
        time.sleep(1)
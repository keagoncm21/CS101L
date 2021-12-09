'''

CS 101 Lab
Program 13 - Unit Testing
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
Create a new python program, called Grades.py. Create another one called Assignment15_Grades.py.
Create multiple functions (total, average, and median) in Grades.py and then test those functions within Assignment15_Grades.py


ALGORITHM:
Three functions called total, average and median.
Total will return a total of the values in a list.
Average will return the average value of a list.
Median will return the median value(s) of a list.

ERROR HANDLING:
Unit testing will find possible errors on Assignment15_Grades.py file.

OTHER COMMENTS:
There may be more unit testing I could add later on.


'''

import math

def total(values : list):
    ''' '''
    total = 0
    for i in values:
        total += i
    return total

def average(values : list):
    ''' '''
    if len(values) == 0:
        return math.nan
    return total(values) / len(values)

def median(values : list):
    ''' '''
    if len(values) == 0 :
        raise ValueError

    values.sort()
    print(values)

    if len(values) % 2 == 1 :
        index=int(len(values)/2)
        return values[index]
    else:
        index=int(len(values)/2)
        total = values[index]+values[index-1]
        return total/2







    




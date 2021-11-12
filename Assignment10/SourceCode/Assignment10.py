'''
CS 101 Lab
Program 10 - Top Words/WordCount
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
In this assignment you will ask the user for a text file to read.  You’ll want to read all the words and output a count of the words that are used the most( We’ll only be concerned with words that have a length greater than 3 ).

Requirements:
●Don’t forget to remove any punctuation from the beginning and ending of the word.    In the previous sentence word should be counted once.  Not word followed by a period.
●Output the top 10 words that are used most.    With the most frequently used words at the top.  Exclude all words that are 3 characters or less.
●Output the number words that appear only once ( How many words are only used once and Only words more than 3 characters ).
●Output how many unique words there are ( Only words more than 3 characters ).
●Recover gracefully from the user providing an invalid file.

ALGORITHM:
There are 5 functions. 
openfile(): Retrieves a file that is from user input.
cleanwords(): Removes punctuation from words.
wordcount(): Function finds the word count of words used one time each.
toptenwords(): Finds the top ten words that are used the most.
uniquewords(): Finds whe number of words that are used (greater than 3 in length) and doesn't count a word if it appears a second time.

ERROR HANDLING:
I used a try/except block to catch any filenotfound erros when getting the file.

OTHER COMMENTS:
There are probably quicker and easier ways to program some of the functions without the large amount of for loops.
'''
import string

def openfile():
    '''Retrieves a file that is from user input'''
    while True:
        try:
            txtname = input('Enter the name of a file to read: ')
            txtFile = open(txtname)
            content = txtFile.read().splitlines()   #reads the file and seperates it into lines
            return content
        except FileNotFoundError: #if the file isn't found, the user will be asked to try again
            print('File not found. Try again.\n')

def cleanwords(file):
    '''Removes punctuation from words'''
    newcontent = []
    for i in file:
        i = i.translate(str.maketrans('', '', string.punctuation)) #switches out punctuation with empty spaces
        newcontent.append(i)
    return newcontent


def wordcount(file):
    '''Function finds the word count of words used one time each'''
    newlst = []
    newlst2 = []
    lstcnt = []
    count = 0
    for i in file:
        newlst.append(i.split(' ')) 

    for x in newlst:
        for z in x:
            newlst2.append(z.lower())
    for y in newlst2:
            if len(y)> 3:
                if y.lower() not in lstcnt: #if words are greater than 3 in length and are not already in lstcnt, they are added. 
                    lstcnt.append(y.lower())
                    count += 1

    return count, newlst2

def toptenwords(file):
    '''Finds the top ten words that are used the most'''
    topdict = {}
    count = 10
    count2 = 10
    for i in file: 
        if len(i)> 3:
            topdict.update({i: file.count(i)}) #topdict is created in order to allow for top 10 words
        count2 -= 1
    print('{:<10}{:^20}{:>10}'.format('#','Word','Freq.'))
    print('{:=<40}'.format(''))
    topdictsorted = dict(sorted(topdict.items(), key=lambda x: x[1], reverse=True)) #sorts the dictionary from top to bottom to have the top used words first
    for k,v in topdictsorted.items(): #if the count is greater than zero, the keys and values are printed
        if count > 0:
            print('{:<10}{:^20}{:>10}'.format(count,k,v))
        count -= 1
            

def uniquewords(file):
    '''Finds whe number of words that are used (greater than 3 in length) and doesn't count a word if it appears a second time'''
    count = 0
    editlst = []
    editlst2 = []
    for y in file:
        editlst.append(y)
    for g in editlst: 
        if len(g)> 3:
            if editlst.count(g) == 1:
                editlst2.append(g.lower()) #as long as the words are found using count() only once. they are added into the editlst2 list.
                count += 1
    return count




if __name__ == '__main__':
    '''Main. Where all the functions are called to bring the program together'''
    tFile = openfile()
    tFile = cleanwords(tFile)
    uniquecount, tFileUnique = wordcount(tFile)
    uniquecnt = uniquewords(tFileUnique)
    toptenwords(tFileUnique)
    print('There are {} words that only occur once, and {} unique words in the document.'.format(uniquecount,uniquecnt))
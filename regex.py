import re

#one = open('huckleberryfin.txt', 'r')
one = open('janeEyre.txt', 'r')
book = one.read().replace('\n',' ')
one.close()

#dictionary
two = open('allNamesUppercase.txt', 'r')
namelist = two.read().reaplce('\n', ' ')
two.close()


### TO DO ###
# Account for UC (uppercase) words at start of sentence/start of quote,dialogue
# Titles such as: Mr., Ms., Mrs., Dr., Judge, Uncle, Aunt, King, Queen, Captain,
#                 Mister, Miss, Missus, Doctor, Captain, Lady, Lord, etc...


def findNames():
    #create a list with pairs of UC words
    #names = re.findall("[A-Z][a-z]+ [A-Z][a-z]+", book)

    #create a dict with key=name; value=occurrences 
    names = {}
    
    #match titles/full names/first name
    for match in re.finditer("[Mr.|Mrs.|Ms.|Dr.|Jr.]* [A-Z][a-z]+ [A-Z]*[a-z]* [Jr.|Snr.]*", book):
        #need to split match.group by ' ' then check if actually name when no title before
        addToDict(match.group(),names)

    #match beginning of sentences
    for match in re.finditer("..[A-Z][a-z]+", book):
        if not(match.group()[0] in ".\":;\'-"):
            addToDict(match.group()[2:],names)

    #debugging
    print names #debugging
    print "len: %d" % len(names)

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;


if __name__=="__main__":
    findNames()

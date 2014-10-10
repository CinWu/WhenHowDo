import re

#dictionary
one = open('allNamesUppercase.txt', 'r')
namelist = one.read().split()
one.close()


### TO DO ###
# Account for UC (uppercase) words at start of sentence/start of quote,dialogue
# Titles such as: Mr., Ms., Mrs., Dr., Judge, Uncle, Aunt, King, Queen, Captain,
#                 Mister, Miss, Missus, Doctor, Captain, Lady, Lord, etc...


def findNames(website):
    #create a list with pairs of UC words
    #names = re.findall("[A-Z][a-z]+ [A-Z][a-z]+", book)

    #create a dict with key=name; value=occurrences 
    names = {}
    
    #match titles/full names/first name
    for match in re.finditer("[Mr.|Mrs.|Ms.|Dr.|Jr.]* [A-Z][a-z]+ [A-Z]*[a-z]* [Jr.|Snr.]*", website):
        #need to split match.group by ' ' then check if actually name when no title before
        parts = match.group().split()
        for part in parts:
            n = False
            if not(part.index('.') != -1):
                return
            if part in namelist:
                n = True
            else:
                n = False
        if n == True:
            addToDict(match.group(),names)

    #match beginning of sentences
    for match in re.finditer("..[A-Z][a-z]+", website):
        if not(match.group()[0] in ".\":;\'-"):
            addToDict(match.group()[2:],names)

    #debugging
    print names #debugging
    print "len: %d" % len(names)

def findDates(website):
    dates = {"^January$|^February$|^March$|^April$|^May$|^June$|^July$|^August$|^September$|^October$|^November$|^December$|^Jan.$|^Feb.$|^Mar.$|^Jun.$|^Jul.$|^Aug.$|^Sept.$|^Oct.$|^Nov.$|^Dec.$\s+[\d]{1,}+,\s+[\d]{1,}"}
    for match in re.finditer(" "):
         parts = match.group().split()
         addToDict(match.group(),dates)
   

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;


if __name__=="__main__":
    #findNames()

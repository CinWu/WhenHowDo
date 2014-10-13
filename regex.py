import re

#test on book
#test = open('janeEyre.txt', 'r')
#book = test.read().replace('\n',' ')
#test.close()

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
    
    #match titles/full names
    for match in re.finditer("(?<!\. )[Mr.|Mrs.|Ms.|Dr.|Jr.]?( )?[A-Z][a-z]+(\s[A-Z][a-z]+)+ [Jr.|Snr.]*", website):
        #isName is a function that tells if valid name or not
        if isName(match.group()):
            #remExtras removes whitespace/other random chars
            addToDict(remExtras(match.group()),names)
    
    #match beginning of sentences
    for match in re.finditer("..[A-Z][a-z]+", website):
        if not(match.group()[0] in ".:;") and (match.group().upper() in namelist):
            addToDict(remExtras(match.group()),names)

    names = narrow(names)

    #debugging
    return names #debugging
#    print "len: %d" % len(names)

def isName(name):
    #split name by whitespace
    parts = name.split()
    #loop through and see if each part is a valid part of a name minus titles (can tell by if '.' in index
    n = True
    for part in parts:
        if (part.upper() in namelist) or ('.' in part):
            n = True
        else:
            n = False
    return n


def findDates(website):
    dates = {}
    for match in re.finditer("January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Jun|Jul|Aug|Sept|Oct|Nov|Dec\s[\d]{1,}|[\d]{4,4}",website):
         parts = match.group().split()
         addToDict(match.group(),dates)
    print dates
    return dates     
   

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;

#housekeeping, cleans the name of ., spaces, etc
def remExtras(string):
    name = re.search("([(Mr.)|(Mrs.)|(Ms.)|(Dr.)|(Jr.)])?[A-Z][a-z]+(\s[A-Z][a-z]+)+( [Jr.|Snr.])*", string)
    if ( name == None ):
        return string
    return name.group()

def narrow(dict):
    freq = []
    for v in dict.values():
        if (v not in freq):
            freq.append(v)
    freq = sorted(freq)
    
    length = len(freq)  
    #will take top 10
    while (len(freq) > length-10 and len(freq) > 0):
        freq.pop()

    for k,v in dict.items():
        if ( v in freq ):
            del dict[k]
    return dict

#if __name__=="__main__":
#    findNames(book)


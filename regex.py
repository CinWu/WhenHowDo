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
    for match in re.finditer("(?<!\. )[Mr.|Mrs.|Ms.|Dr.|Jr.]* [A-Z][a-z]+ [A-Z][a-z]+ [Jr.|Snr.]*", website):
        #isName is a function that tells if valid name or not
        if isName(match.group()):
            addToDict(match.group(),names)
 
    #match beginning of sentences
    for match in re.finditer("..[A-Z][a-z]+", website):
        if not(match.group()[0] in ".:;") and (match.group().upper() in namelist):
            addToDict(match.group()[2:],names)
    
    #Frequency and narrowing down search
    frqnames = {}
    for k,v in names.items():
        if (v not in frqnames):
            frqnames[v] = [k]
        else:
            frqnames[v].append(k)
    size = len(frqnames)/2
    i = 0
    while( len(frqnames) > 10 or len(frqnames) > size):
        if i in frqnames:
            del frqnames[i]
        i += 1
    names = {}
    for k,v in frqnames.items():
        for n in v:
            if (n not in names):
                names[n] = k

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
    dates = {"^January$|^February$|^March$|^April$|^May$|^June$|^July$|^August$|^September$|^October$|^November$|^December$|^Jan.$|^Feb.$|^Mar.$|^Jun.$|^Jul.$|^Aug.$|^Sept.$|^Oct.$|^Nov.$|^Dec.$\s+[\d]{1,}+,\s+[\d]{1,}"}
    for match in re.finditer(" "):
         parts = match.group().split()
         addToDict(match.group(),dates)
   

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;


#if __name__=="__main__":
#    findNames(book)


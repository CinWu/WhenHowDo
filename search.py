#Takes FOREVER to search.

import google
from bs4 import BeautifulSoup
from urllib import urlopen

import regex


results = {}

def find(q):
    for url in google.search(q, num = 5, stop = 10):
        
        u = urlopen(url)
        txt = BeautifulSoup(u.read())
        
        #reads text in body tags
        txt = txt.body
        if (txt != None):
            txt = txt.prettify().encode('UTF-8')

            if "who" in q.lower():
                names = regex.findNames(txt)
                print names
                addVals(names)
            elif "when" in q.lower():
                addVals(regex.findDates(txt))

    strresults = ""
    for i in narrow(results):
        #Why breaks no work
        strresults += i + ", "
    return strresults
    results.clear()
    #print url

#To put together the top searches
def addVals(dict):
    for k,v in dict.items():
        if (k not in results):
            results[k] = v
        else:
            results[k] += v

#narrows down the top searches formed by addVals
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
    return dict.keys()
 
#find("when is columbus day")       
#find("Who is batman")
#find("who is sheik")

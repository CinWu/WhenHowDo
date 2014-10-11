import google
from bs4 import BeautifulSoup
from urllib import urlopen

import regex

def find(q): 
    for url in google.search(q, num = 5, stop = 10):
        
        u = urlopen(url)
        txt = BeautifulSoup(u.read())
        
        #reads text in body tags
        txt = txt.body

        txt = txt.prettify().encode('UTF-8')
        
        regex.findNames(txt)
    
        #print url

find("Who is batman")

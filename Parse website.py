# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:12:52 2015

@author: robin.bajracharya
"""

from bs4 import BeautifulSoup
import urllib2

print 
print
print
print
print
links = ["https://en.wikipedia.org/wiki/Dividend","http://www.investopedia.com/terms/d/dividend.asp","http://www.dividend.com/","http://www.kiplinger.com/slideshow/investing/T018-S013-12-stocks-to-earn-dividends-every-month/index.html","http://www.reuters.com/finance/markets/dividends/"]
linksnumber = len(links)
#print linksnumber
searchword = "dividends";


def all_occurences(file, str):
        initial = 0
        while True:
            initial = file.find(str, initial)
            if initial == -1: return
            yield initial
            initial += len(str)
     

       
#for lol in range(0,linksnumber-1):
lol=0;   
#print links[lol];
print

for lol in range(0,linksnumber):   
    print lol+1, "<-----------*******************************************"
    print    
    print links[lol]
    print
    request = urllib2.Request(links[lol])
    
    html_doc = urllib2.urlopen(request)
    soup = BeautifulSoup(html_doc)
    text =[''.join(s.findAll(text=True))for s in soup.findAll('p')]
    print (len(text))
    #string conversion
    bodytext=""
    for i in range(0,len(text)-1):
        bodytext = bodytext+text[i] 
        
        print bodytext;    
     #iasbdhasbdhasbd 
    all_index = list(all_occurences(bodytext,searchword));
    print all_index
    textrange = len(all_index)
    wordlength = len(searchword)
    #uydsauisdfihlsdfihsdf
    for j in  range(0,textrange):
        beg = all_index[j]-10;
        if (all_index[j]-10) < 0:
            beg = 0
        print j+1, bodytext[beg:beg+20+wordlength];
    print "Count:", textrange;

    

    
   
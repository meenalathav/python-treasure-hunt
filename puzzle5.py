#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:16:20 2020

@author: Meenalatha Vaithilingam
"""

import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read().decode()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve anchor tags
tags = soup('a')
newlink = tags[0].get('href', None)  # linkedlist.php?nothing=12345
param = re.findall("[0-9]+", newlink)[0]

crawlCount = 0 

while True:
    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(param)).read().decode()
    print(html)
    
    # Look only for a match to "the next nothing is" followed by a number to avoid misleading numbers
    paramLst = re.findall("the next nothing is ([0-9]+)", html)
    
    # No matches to numbers
    if len(paramLst) == 0:
        # To keep loop flowing through the "Divide by two." break
        if re.search("Divide by two", html):
            param = int(param)//2
            print("New param after dividing by 2:", param)
            continue
        else:
            break
    
    param = paramLst[0]   
    
    crawlCount += 1
    print("Pages crawled so far:", crawlCount)
    print("Number extracted from page: ", param)
 
       
print("Finally reached the page: ", html)  # completion of puzzle at peak.html
      



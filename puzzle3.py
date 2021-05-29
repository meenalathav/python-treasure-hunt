#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:13:38 2020

@author: Meenalatha Vaithilingam
"""

import re

# commented text from page source copied to hidden.txt
fhandle = open("hiddentext.txt", 'r')

freqChars = dict()

for line in fhandle:
    if re.search("<!--", line) or re.search("-->", line):
        continue
    
    lstChars = list(line)
    for char in lstChars:
        freqChars[char] = freqChars.get(char, 0) + 1


freqChars  # characters with lowest count of 1 spell out "equality"

puzzleTxt = ""
    
for key in freqChars :
    if freqChars[key] == 1:
        puzzleTxt += key

print(puzzleTxt)  # prints the word "equality"
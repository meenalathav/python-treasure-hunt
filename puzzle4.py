#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:47:11 2020

@author: Meenalatha Vaithilingam
"""

import re

# commented text from page source copied to hiddentext1.txt
fhandle = open("hiddentext1.txt", 'r')

lstChars = []

for line in fhandle:
    if re.search("<!--", line) or re.search("-->", line):
        continue
    
    lstReg = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", line)
    if len(lstReg) > 0:
        lstChars += lstReg

print(lstChars)  # characters of word "linkedlist"

puzzleText = ""
print(puzzleText.join(lstChars)) # prints word "linkedlist"

    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:44:16 2020

@author: Meenalatha Vaithilingam
"""


def charMap(char):
    
    num = ord(char) + 2 - ord('a')
    if num % 26 < 2:
        return chr( num % 26 + ord('a') )
    else:
        return chr(ord(char) + 2)
    

strObj = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newStr = ""

for character in strObj:
    if ord(character) >= 97 and ord(character) <= 122 :
        newStr += charMap(character)
    else: newStr += character

print(newStr)



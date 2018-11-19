#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:14:23 2018

@author: anikkengjeruldsen
"""
#%%

def isnumber(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def string_calculator(myString):
    if myString == "":
        return 0
    else:
        myList = myString.split(',')
        counter = 0
        for i in myList:
            if isnumber(i) == False:
                return "Input string not correct"
        else:
        	for number in myList:
        		counter += int(number)
    return counter


#%%


     
    
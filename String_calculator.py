#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:14:23 2018

@author: anikkengjeruldsen
"""
#%%

def string_calculator(myString):
	if myString == "":
		return 0;
	myList = myString.split(',')
	sum = 0
	for number in myList:
		sum = sum + (int)(number)
	return sum;


def main():
	myString = (str)(raw_input("Enter the desired string: "))
	print(string_calculator(myString))

main()

#%%



     
    
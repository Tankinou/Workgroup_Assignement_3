#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:21:31 2018

@author: flo
"""
#%%



def checkprime(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
    return True



def fizzbuzzwhiz(num):
   if checkprime(num) == True:
       return "Whiz"
   elif num % 3 == 0 and num % 5 == 0:
       return "FizzBuzz"
   elif num % 3 == 0:
       return "Fizz"
   elif num % 5 == 0:
       return "Buzz"
   else:
       return num
   
#%%    
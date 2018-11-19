#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:59:20 2018

@author: monicaalvarenga
"""
from fizzbuzzwhiz import fizzbuzzwhiz


def test_fizzbuzzwhiz_return_Whiz():
    values=[2,3,5,7]
    for case in values:
        assert fizzbuzzwhiz(case)=="Whiz"

def test_fizzbuzzwhiz_returns_Fizz(): #create assertions 
    values=[9,6,12342]
    
    for case in values:
        assert fizzbuzzwhiz(case)=="Fizz"
    

def test_fizzbuzzwhiz_returns_Buzz():
    values=[20,10,1000]
    
    for case in values:
        assert fizzbuzzwhiz(case)=="Buzz"
        
def test_fizzbuzzwhiz_returns_Fizzbuzz():
    values=[15,30]
    
    for case in values:
        assert fizzbuzzwhiz(case)=="FizzBuzz"



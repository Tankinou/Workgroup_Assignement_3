#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:43:22 2018

@author: flo
"""
#%%

from String_calculator import string_calculator
    

def test_stringcalc_return_sum():
    strings = [{"string":"1,2,3,4,5","value":15},{"string":"1,2,3,4","value":10},{"string":"1,-3","value":-2},
                {"string":"1,5","value":6},{"string":"100,2","value":102}]
    for case in strings:
       assert string_calculator(case["string"]) == case["value"]
        
def test_stringcalc_return_zero():
        assert string_calculator("") == 0   
        
def test_stringcalc_return_unusual():
    strings = [{"string":"1,2,3,,4,5","value":"Input string not correct"},{"string":"1,gll,4","value":"Input string not correct"},{"string":",,,","value":"Input string not correct"},
                {"string":",2,3","value":"Input string not correct"},{"string":"111,3,-2,"",","value":"Input string not correct"}]
    for case in strings:
       assert string_calculator(case["string"]) == case["value"]        
    




#%%
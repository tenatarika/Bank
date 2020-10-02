# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:55:06 2020

@author: Furcas
"""
from random import choice


class Salary:
    def __init__(self, *choice):
        self._choice = choice 
        
    def __get__(self, obj, owner):
        return choice(self._choice)
        
        

class People:
    
    student = Salary(250, 500, 700)
    prof = Salary(500, 1000, 2000, 100000)    
    
    
men = People()


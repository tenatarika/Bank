# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:55:06 2020

@author: Furcas
"""
from random import choice
from reader import Reader

class Salary:
    def __init__(self, *choice):
        self._choice = choice 
        
    def __get__(self, obj, owner):
        return choice(self._choice)
        
        
'''
class People:
    file = Reader('People_job.json')
    file.writeJson({'profession':'salaries'})
    new1_data = 'Student'
    new2_data = (250, 500, 700)
    file.addWord(new1_data, new2_data)
    student = Salary(250, 500, 700)
    data = file.readJson()
    print(data.items())
    prof = Salary(500, 1000, 2000, 100000)    
    
 '''   
#men = People()


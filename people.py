# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:55:06 2020

@author: Furcas
"""
from random import choice
from fileManager import FileInterface


class Salary:
    def __init__(self, *choice):
        self._choice = choice 
        
    def __get__(self, obj, owner):
        return choice(self._choice)
        
        

class People:
    def __init__(self, request):
        self.request = request
        self.fileName = 'People_job.json'
    def get(self):
        
        IJson = FileInterface(self.fileName, 'json')
        data = IJson.file.readJson()
        if self.request in data.keys():
            
            print('Job was found!')
            return choice(data[self.request])
        else:
            print('No such professions')
            
    #file.writeJson({'profession':'salaries'})
    #new1_data = 'student'
    #new2_data = (250, 500, 700, 900)
    #file.addWord(new1_data, new2_data)
    #student = Salary(250, 500, 700)
    #data = file.readJson()
    
    #print(data.items())
    #prof = Salary(500, 1000, 2000, 100000)    
    
   
men = People('student')

print(men.get())
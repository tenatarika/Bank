# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 01:47:16 2020

@author: Furcas
"""

import json

class Reader():        
    @classmethod
    def addWord(cls, word):
        data = cls.readJson()
        data.update({1 : word}) #нужно написать норм тип данных
        cls.writeJson(data)
        
    @classmethod    
    def writeJson(cls, data):
        
        with open('dataWords.json', 'w') as f:
            
            json.dump(data, f, indent = 4, ensure_ascii=False)
            
    @classmethod    
    def readJson(cls):
        try:
            data = json.load(open('test.json'))
            
        except:
            data = {}
            
        return data
    
    


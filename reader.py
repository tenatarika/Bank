# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 01:47:16 2020

@author: Furcas
"""

import json

class Reader():
    def __init__(self, file_name):
        self.file_name = file_name    
        
        
    
    def addWord(self, new1_data, new2_data):
        data = self.readJson()
        #n_list = len(data)
        data.update({new1_data : new2_data}) 
        self.writeJson(data)
        
      
    def writeJson(self, data):
        
        with open(self.file_name, 'w') as f:
            
            json.dump(data, f, indent = 4, ensure_ascii=False)
            
       
    def readJson(self):
        try:
            data = json.load(open(self.file_name))
            
        except:
            data = {}
            
        return data
    
    

#test = Reader('test.json')
#test.writeJson({12323: 'pub_key'})
#test.addWord('ojjibu')
#test.addWord('oiokhjungtrffr')
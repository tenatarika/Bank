# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 03:00:12 2020

@author: Furcas
"""


from json_master import Reader



class FileInterface:
    
    def __init__(self, filename, format_file):
        self.format_file = format_file
        self.filename = filename
        
        if self.format_file == 'json':
            self.file = Reader(filename)
            
        else:
            raise NameError
    
    
    
    
#man = FileInterface('mors.json', 'json')
         
    
        


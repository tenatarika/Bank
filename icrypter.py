# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 02:31:19 2020

@author: Furcas
"""

from create_keys import Create_keys
from encrypt import Encrypt_data
from decrypt import Decrypt


class Crypter(Create_keys, Decrypt):
    def __init__(self, data):
        self.data = data
        self.create_k = Create_keys()
        self.decrypt_data = Decrypt()
        self.encrypt_data = Encrypt_data(self.data)
        
        
    def get_keys(self):
        self.create_k.write_private_key()
        self.create_k.write_public_key()
        
        
    def encryption(self):
        self.encrypt_data.encrypt()
        print('done!')
        
    def decryption(self):
        
        return self.decrypt_data.decrypt()
    
   
test = Crypter(b'korn')
test.encryption()


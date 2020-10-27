# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 02:03:53 2020

@author: Furcas
"""

import rsa

class Decrypt:
    def __init__(self):
        self.prkey = open('privatekey.key', 'rb')
        self.efile = open('encrypted_file', 'rb')        
        
        
    def decrypt(self):
        
        pkey = self.prkey.read()
        edata = self.efile.read()
        
        
        private_key = rsa.PrivateKey.load_pkcs1(pkey)
        
        
        
        decrypted_data = rsa.decrypt(edata, private_key)
        
        return decrypted_data.decode('utf-8')
    
'''    
a = Decrypt()
print(a.decrypt())
'''

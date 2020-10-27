# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 01:31:52 2020

@author: Furcas
"""
import rsa

class Encrypt_data:
    
    def __init__(self, data):
        self.data = data
        self.pkey = open('publickey.key', 'rb')
        self.edata = open('encrypted_file', 'wb')
    
    
    def load_pkey(self):
        pkdata = self.pkey.read()
        
        pubkey = rsa.PublicKey.load_pkcs1(pkdata)
        return pubkey
        
        
    def encrypt(self):
        
        encrypted_data = rsa.encrypt(self.data, self.load_pkey())
        #print(encrypted_data)
        self.edata.write(encrypted_data)
        self.edata.close()
        
'''     
a = Encrypt_data(b'korn')
a.encrypt()
'''
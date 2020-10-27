# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 01:17:26 2020

@author: Furcas
"""

import rsa


class Create_keys:
    
    def __init__(self):
        (self.pubkey, self.privkey) = rsa.newkeys(2048)
        
    def write_public_key(self):
        pubkey_File = open('publickey.key', 'wb')
        pubkey_File.write(self.pubkey.save_pkcs1('PEM'))
        pubkey_File.close
        
    def write_private_key(self):
       prikey_File = open('privatekey.key', 'wb')
       prikey_File.write(self.privkey.save_pkcs1('PEM'))
       prikey_File.close 
       
       
       
'''
keys = Create_keys()
keys.write_public_key()
keys.write_private_key()
'''
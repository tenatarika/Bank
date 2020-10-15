# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:40:35 2020

@author: Furcas
"""

import unittest 

from account import Account


class TestAccont(unittest.TestCase):
    
    def setUp(self):
        name = 'Ivan'
        self.my_account = Account(name, 0)
        
        self.money = [1000, 2000, 3000, 4000, 100, 500]
        
        
    def test_store_single_deposit(self):
        self.my_account.deposit(self.money[0])
        
        self.assertIn(1000, self.my_account._history[0])
        
   
    def stress_test_of_history(self):
        self.my_account.deposit(2000)
        self.assertNotEqual(3000, self.my_account._balance)
    
        
     
        
if __name__ == '__main__':
    unittest.main()

    


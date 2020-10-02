# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:21:11 2020

@author: Furcas
"""

from account import Account
from people import People
class Bank(People):
    
    def __init__(self, name, job):
        self.name = name 
        self.job = job
        self._salary = 0
        self.user = Account(self.name, self._salary)
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value
    
        
    
    def get_job(self):
        if self.job.lower() == 'student':
            
            self.salary = People.student
            print(f'Hey, {self.name}! You can earn {self.salary} points!')
        else:
            
            self.salary = People.prof
            print(f'Hey, {self.name}! You can earn {self.salary} points!')
        
    def payday(self):
        self.user.deposit(self.salary)
        
    
    def balance(self):
        self.user.show_balance()
        
    def history(self):
        self.user.show_history()
        
    def withdraw (self, amount):
        self.user.withdraw(amount)
    
    def deposit(self, amount):
        self.user.deposit(amount)

#men1 = Bank('Boris', 'prof')
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:01:08 2020

@author: Furcas
"""



from datetime import datetime
import pytz


WHITE = '\033[00m'
GREEN = '\033[1;92m'
RED = '\033[1;31m'

class Account:
    def __init__(self, name, balance):
        self.name = name 
        self._balance = balance 
        self._history = []
        
    @staticmethod
    def _get_current_time():
        return  pytz.utc.localize(datetime.utcnow())
    
    def deposit(self, amount):
        self._balance+=amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])
        
    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print(f'You spent {amount} units')
            self._history.append([-amount, self._get_current_time()])
            self.show_balance()
        else:
            print('Not enoght money')
            self.show_balance()
        
    def show_balance(self):
        print (f'Balanse: {self._balance}')
        
    def show_history(self):
        for amount, date in self._history:
            if amount > 0 :
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE}, {transaction} on {date.astimezone()} ')
        
a = Account('sl', 0)
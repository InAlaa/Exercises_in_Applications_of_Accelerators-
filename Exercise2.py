# -*- coding: utf-8 -*-
"""Ex2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_7AA1oqqVQn2lq-Gv652WpLrqZfdpdt3
"""

class neu:
    
    def __init__(self, x, y):
        self.x = x
        
        self.y = y
        
        self.n = self.x - self.y
    
    def Print(self):
      print('\n\nNeutrons = ',self.n)

t1=neu(x=int(input('Mass number = ')) ,y=int(input('Number of protons = ')))
t1.Print()

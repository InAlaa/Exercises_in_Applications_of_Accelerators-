# -*- coding: utf-8 -*-
"""Matrix Random Multiply 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pePmGnhHZWGo-rys72kCeAwOT_MabVPC
"""

import random
import numpy
 
matrix1 = []
matrix2 = []
answer = [[0]*3]*3


for i in range(3):
    a =[]
    for j in range(3):
         x=random.randint(0,9)
         a.append(int(x))
    matrix1.append(a)

print("matrix1 =")
for t in matrix1:
	print(t)



for i in range(3):
    b =[]
    for j in range(3):
         y=random.randint(0,9)
         b.append(int(y))
    matrix2.append(b)

print("\nmatrix2 =")
for s in matrix2:
	print(s)


answer = numpy.dot(matrix1,matrix2)

print("\n\nanswer =")
for r in answer:
	print(r)
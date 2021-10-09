'''
NumPy es una librería de Python.
NumPy es usado para trabajar con matrices (arrays de arrays).
NumPy es el nombre corto de "Numerical Python".
'''
from numpy import random as r

print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size=r.choice([1,2],p=[0.1,0.9]), p=[0.5,0.2,0.2,0.1], replace=False))

#--------------

import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

#--------------

import sys
import numpy as np
S= range(1000)
print(sys.getsizeof(5)*len(S))
#28000 bytes --> 28 kilobytes
D= np.arange(1000)
print(D.size*D.itemsize)
#8000 bytes --> 8 kilobytes

#--------------

import sys
import numpy as np
import time
SIZE = 1000000

L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2= np.arange(SIZE)

start= time.time()
result=[(x,y) for x,y in zip(L1,L2)] #listas
print((time.time()-start)*1000)

start=time.time()
result= A1+A2 #arreglos
print((time.time()-start)*1000)

#--------------------------

import numpy as np
a = np.array([34, 25, 7])

print(type(a))

print(a[0]) # imprime 34
print(a[1]) # imprime 25
print(a[2]) # imprime 7
#print(a[3]) # Genera un error teniendo en cuenta que la posición o índice (index) 3 no existe en el arreglo o matriz de rango 1

a[0] = 5

print(a)

#-----------------------------------

# Matrices

# Matrices
import numpy as np

b = np.array([[0, 1, 2], [3, 4, 5]]) # matriz 2 x 3

print(b)

print(b.ndim)

print(b.shape)

print(b[0, 1])

'''
import numpy as np

b = np.array([[[0, 1, 2], [3, 4, 5]], 
            [[8, 19, 32], [45, 10,2]],
            [[3, 9, 2], [5, 1, 12]]]) # matriz 2 x 3

print(b)

print(b.ndim)

print(b.shape)

print(b[0, 1, 1])

print(b[1, 1, 0])

'''

import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
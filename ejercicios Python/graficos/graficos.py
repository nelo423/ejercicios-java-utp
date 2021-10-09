import math
import numpy as np
from matplotlib import pyplot as plt

x = np.array(range(500)) * 0.1
y = np.zeros(len(x)) # zeros devuelve un array del tamaño indicado

for i in range (len(x)):
    y[i] = math.sin(x[i])
plt.plot(x,y)    
plt.title(" Grafica de la funcion seno")
plt.xlabel("Datos coordenada x ")
plt.ylabel("Datos coordenada y ")
plt.grid(color = 'r' , linestyle = 'dotted', linewidth = 1)# Muestra la grilla
plt.show() # La funcion show me permite mostrar la gráfica

 #Recorridos (Unidad 3)
'''
x = 4
y = 3
print(x**2)
print(y)
'''
'''
mi_lista = []
for x in range(4, 31, 2):
   if x%3 == 0:
    mi_lista.append(x**2)
print(mi_lista)
'''
# Cree un diccionario en el que las llaves sean una tupla entre los números del 3 al 10 y su respectivo cubo. Y dónde los valores sean las listas con los cuadrados de los números de dos en dos, entre el 4 y el 30, que son divisibles enteros con el primer elemento de su llave correspondiente.

'''
mi_diccionario = dict()

for y in range(3, 11):
    mi_diccionario[(y, y**3)] = []
    for x in range(4, 31, 2):
     if x%y == 0:
        mi_diccionario[(y, y**3)].append(x**2)
print(mi_diccionario)
'''
#######PROGRAMACION FUNCIONAL#####################

cadena = "Programación"
# Se convierte la variable cadena que contiene una cadena de caracteres,
# a lista
cad = list(cadena)

#print(cadena)

#print(cad)

#print(''.join(cad))

#Diccionarios

plantaciones = {"01": "Plátano", "02": "Café"}

print(plantaciones)
print(list(plantaciones))
print(list(plantaciones.keys()))
print(list(plantaciones.values()))
print("**************")
print(plantaciones.items())
print(list(plantaciones.items()))
print(list(plantaciones.items())[0])
print(list(plantaciones.items())[1])

print(list(list(plantaciones.items())[1]))
print(''.join(list(list(plantaciones.items())[1])))
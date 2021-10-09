# Problema #1:
# Utilizar la función incorporada map() para crear una función que retorne una lista con la longitud de cada palabra separadas por espacios) de una frase. La función recibe una cadena de texto y retornará una lista.
'''
def long_word(frase):  # Función
    caracteres = list(map(len,frase.split())) # Longitud de cada palabra
    return caracteres  # Retornar resultado
long_word('Soy tripulante MisionTic2022') # Prueba de la función
'''
#--------------------------------------

#Problema #2:
# Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
# Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función reduce.
'''
from functools import reduce
def calcular (numero):
    return reduce(lambda x,y:x*10 + y,numero) 
calcular ([4,3,2,1])   
'''    
#--------------------------------------- 

# Problema #3:
# Crear una función que retorne las palabras de una lista de palabras que comience con una letra en específico. #Utilizar la función filter.

#def palabra(listas,filtro):
#  return list(filter(lambda word:word[0]==filtro,listas))
#palabra(['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie'], 'J')
'''
def filtro_palabras(lista_palabras,letra):
  return list(filter(lambda word:word[0]==letra,lista_palabras))
filtro_palabras(['Perro','Gato','Pelota','Manzana','Libro','Python'], 'P')
'''

#----------------------------------------

# Problema #4:
# Realizar una función que tome una lista de comprensión para devolver una lista de la misma longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre ellas. Ejemplo: Listas: ['A', 'a'] ['B','b'] Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función zip.
'''
L1 = ['A', 'a']
L2 = ['B', 'b']
connector = '_'
def concatenacion(L1, L2,connector):
  return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]
concatenacion(L1,L2,'-')
'''

#---------------------------------------

#Problema #5:
# Realizar una función que tome una lista y retorne un diccionario que contenga los valores de la lista como clave y el índice como el valor. Utilizar la función enumerate.
'''
def d_lista(L):
  return{key:value for value,key in enumerate(L)}
d_lista(['a','b','c','d','e'])
'''

#--------------------------------------

#Problema #6:
# Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo valor es igual a su índice. Utilizar la función enumerate.

def count_match_index(L):
  return len([num for count,num in enumerate(L)if num==count])
count_match_index([0,2,2,1,5,5,6,1,0])

#------------------------------------------------------------------------------
lista1 = [3, 1, 8, 10, 4, 9, 2, 7]
lista2 = [0, 2, 2, 1, 5, 5, 6, 1, 0]


def validarIndice(lista: list):
    contador = 0
    for i in enumerate(lista):
        validar = list(i)
        if validar[0] == validar[1]:
            contador += 1
    print(f"La cantidad de elementos igual a su índice es {contador}")

def count_match_index(L):
    return len([num for count,num in enumerate(L) if num==count])

validarIndice(lista2)
print(count_match_index(lista2))
#-----------------------------------------------------------------------------------
lista1 = [3, 1, 8, 10, 4, 9, 2, 7]
lista2 = [0, 2, 2, 1, 5, 5, 6, 1, 0]

contador = 0
for i in enumerate(lista1):
    validar = list(i)
    if validar[0] == validar[1]:
        print(f"índice {validar[0]} --> {validar[1]}")

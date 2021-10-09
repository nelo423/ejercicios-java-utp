'''
# Ejemplo Función Filter
def mayor_a_cinco(elemento):
    return elemento > 5
tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado =tuple(filter(mayor_a_cinco,tupla))
resultado = len(resultado)
print(resultado)
'\n'
#Ejemplo Función Filter Lambda
resultado = tuple(filter(lambda elemento: elemento > 5, tupla))
resultado = len(resultado)
print(resultado)
'''
#Ejemplo Acumulador FunciónReduce
'''
lista =[1,2,3,4]
acumulador = 0;

for elemento in list:
    acumulador += elemento
print(acumulador)    
'''

# Ejemplo Función Zip
'''
nombres = ['Raul' , 'Pedro' , 'Sofia']
apellidos =['Lopez Briega' ,  'Perez' , 'Gonzales']
#zip une cada nombre con su apellido en una lista de tuplas
nombre_apellido = (zip(nombres,apellidos))
print(nombre_apellido)
'''
'''
# map
# Creamos la lista

lista_numeros: list = [2, 3, 4, 5, 6, 7, 8, 9]
#map(funcion_a_aplicar, un_iterable)
elevar_al_cubo = lambda n: n**3
print(list(map(elevar_al_cubo, lista_numeros)))

def filtrar(dato):
    if dato=="á":
        return "a"
    elif dato=="é":
        return "e"
    elif dato=="í":
        return 'i'
    elif dato=='ó':
        return 'o'
    elif dato=='ú':
        return 'u'
    else: return dato
#Función anónima
caracteres = lambda letras : list( map(filtrar,letras) )
#Palabra a procesar
palabra = "olímpica"
palabra_2 = str(input('Ingrease palabra : '))
#Llama la función lambda con la palabra casteada a lista
#Y obtiene una nueva lista con los caracteres sin tilde
result = caracteres( list(palabra) )
result_2 =caracteres( list(palabra_2))
print( ''.join(result))
print( ''.join(result_2))


# Diccionario
fruit = {"01":"pple", "02":"Orange", "03":"pricot"}
# Lista
#fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit.values())
lista = list(map_object)
print(lista)
#all
if all(lista):
    print("all->Todos son verdaderos")
else:
    print("all->Hubo alguno falso")
#any
if any(lista):
    print("any->tiene al menos uno verdadero")
else:
    print("any->todos son falsos")
'''
uids = ['B1CD102654' , 'B1CDEF2654']
for uid in uids:
    cond = []
#Por lo menos dos letras mayusculasen el alfabeto ingles
    cond.append(len(list(filter(lambda x: x.isupper(), list(uid)))) >= 2) 
#Por lo menos tres digitos
    cond.append(len(list(filter(lambda x: x.isdigit(), list(uid)))) >= 3)
#Solamente digitos alfanumericos
    cond.append(len(list(filter(lambda x: not(x.isalnum()) , list(uid)))) == 0)
#Que no existan repeticiones
    cond.append(len(uid)) == len(set(uid))
#Exactamente 10 caracteres
    cond.append(len(uid) ==10)
    print('valido' if all(cond) else print('Invalido'))
  # isupper comprueba si todos los caracteres esta en mayuscula, si es correcto devuelve true
  #  método isalnum () devuelve True si todos los caracteres de la cadena son alfanuméricos (ya sean alfabetos o números). Si no, devuelve False.



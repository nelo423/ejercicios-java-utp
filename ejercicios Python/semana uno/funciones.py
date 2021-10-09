# Max y Min
var1 = 10
var2 = 30
var3 = 120
var4 = 500

maximo = max(var1, var2, var3, var4)
print(maximo)

minimo =min(var1, var2, var3, var4)
print(minimo)

var1 = 10
var2 = 30
var3 = 120
var4 = 500

L = 38
A = L * L
P = L + L + L + L

#Funcion para obtener el area de un cuadrado*******se puede utilizar cualquiera de las dos formas****
def areaCuadrado(lado):
    return lado * lado

#Funcion para obtener el perimetro de un cuadrado****se puede utilizar cualquiera de las dos formas****
def perimetroCuadrado(lado):
    p = lado + lado + lado + lado
    return p


#Funcion para sumasr dos numeros****se puede utilizar cualquiera de las dos formas****
def suma(a,b):
    return a + b

#imprime cosas
def imprime_Cosas():
    print("La clase esta genial")
    print("Python es lo maximo")
imprime_Cosas()

print("El area del cuadrado es {}".format(areaCuadrado(38)))
print("El perimetro del cuadrado es {}".format(perimetroCuadrado(38)))
print("La suma del cuadrado es {}".format(suma(3,5)))

# una función que no hace nada (aun)
def consultar_nombre_genero(letra_genero): pass

type(consultar_nombre_genero)
consultar_nombre_genero("M")

#Sentencia return
def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    
resultado = otra_suma(5,6)
print(resultado)

def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2
    
resultado = otra_suma(5,6) 
print(resultado)

#funcion nombre y apellido
def mi_funcion(nombre, apellido): 
    nombre_completo = nombre, apellido 
    print(nombre_completo)

mi_funcion('David','Alvarez')

# Parámetros por omisión
def saludar(nombre, mensaje='Hola'): 
    print(mensaje, nombre)

saludar('Pepe Grillo') 

#Keywords como parámetros
def saludar(nombre, mensaje='Hola'): 
    print(mensaje, nombre)

saludar(mensaje="Buen día", nombre="Juancho")
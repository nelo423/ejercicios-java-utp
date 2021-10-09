'''
# 1. Leer un número entero y determinar si es un número terminado en 4. ok
num = int(input("Ingresa un numero: "))
contador = num % 10 # obtengo el último número del entero y lo guardo en la variable contador

if contador == 4:
   print("El último número del entero: "+str(num) +" Si es un número terminado en 4")
else:
   print("El ultimo número del entero: "+str(num) + " No es un número terminado en 4" )
'''
'''
###########################################ok
#  2. Leer un número entero y determinar si tiene 3 dígitos.
num = input('ingresa un numero: ')
contador = len(num)
if contador == 3:
    print('El numero ingresado tiene 3 digitos')
else:
    print('El numero ingresado no tiene 3 digitos')

'''
'''
##################################################
#3. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
numero = int(input('Ingrese un numero entero de dos digitos: '))
if  int(numero [0]) % 2 ==0 :
    if int(numero [1]) % 2 ==0 :
       print('Los digitos ingresados son pares')
    else:
         print('No todo los digitos son pares')
else:
     print('No todos los digitos son pares')    
 ''' 
'''    
#############################################3 ok
#  4 Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
numero_entero = int(input('Ingrese el numero a revisar: '))
if numero_entero <= 20: 
    contador = 0
    for i in range(1,numero_entero + 1): # con el for recorremos los numero enteros menores
                                         # que el numero ingresado + 1  
     if numero_entero % i == 0:          # si el resto de la division del numero desde 1 hasta el numero ingresado es = a 0
           contador += 1                 # aumento contador en 1                                       
    if contador == 2:
        print(str(numero_entero)+' Es primo ')
    else:
        print(str(numero_entero)+ ' No es primo')
else:
    print('debe ingresar un número menor a 20')
     
'''
'''
#############################################33
# 5. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.

es_primo = input('Ingrese el numero a revisar: ')
def es_primo(num):
    if num == 1:
       return False
       print('El numero ingresado es par')
    elif num == 2:
         return True
    else:
        for i in range(0,num):
            if num  % i == 0:
                return False
'''
'''########################################################3 ok
# 6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
n1 = input('Ingrese el primer numero de dos digitos: ')
n2 = input('Ingrese el segundo numero de dos digitos: ')
if (n1==n2):
    print("Los numeros ingresados son iguales")
else:
    print("Los numeros ingresados no son iguales")
'''
'''
#####################################################33 ok
#7. Leer dos números enteros y determinar cuál es el mayor.

n1:int = input('Ingrese el primer numero : ')
n2:int = input('Ingrese el segundo numero : ')
if (n1 > n2):
    print(f"El numero mayor es {n1} :")
else:
    print(f"El numero mayor es {n2}")
'''
'''
####################################################33
# 8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual
# la suma de todos los dígitos.
n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))
while n1 != 0:
      n2 != 0
      n1 // 10
      n2 // 10
      suma = n1 + n2 
      
      print("La suma de los digitos es {}".format(suma))
'''
#####################################################3
9. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.


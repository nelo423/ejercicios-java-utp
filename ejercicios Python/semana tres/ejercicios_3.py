#---------Ejercicios de aplicación estructura iterativa while:--------------
# Ejercicio No 1 ok
# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
'''
x = 0
cantidad1 = 0
cantidad2 = 0
while x < 10:
      nota = 0
      nota = float(input('Ingrese nota : '))
      if nota >= 7:
         cantidad1 = cantidad1 + 1
      else:
          cantidad2 = cantidad2 + 1
      x = x + 1
print('Notas mayores o iguales a  7: ' + str(cantidad1))
print('Notas menores a 7 : ' + str(cantidad2))
'''

# Ejercicio No 2
# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
'''
altura = 1
suma = 0
contador = 0

while altura != 0:
      altura = int(input('Ingrese la altura a promediar (Ingrese 0 para terminar) :'))
      if altura !=0:
         suma += altura
         contador += 1
if  contador == 0:
    print('No ha ingresado un ningun digito')
else:   
    promedio = round((suma / contador),0)
    print('El promedio de las alturas {} es igual a {} Mts'.format(contador, promedio))
'''
# Ejercicio  No 3 ok
#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar #un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados #cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá #informar el importe que gasta la empresa en sueldos al personal.
'''
x = 1
contador1 = 0
contador2 = 0
gastos = 0
sueldo = 0

n = int(input('Ingrese cantida de empleados de la empresa : '))

while x <= n :
    sueldo = int(input('Ingrese sueldo del empleado : '))
    if sueldo <= 300:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
    gastos = gastos + sueldo
    x = x + 1
    
print('Cantidad de empleados con sueldos entre $ 100 y $ 300 es :', contador1)
print('Cantidad de empleados con sueldo mayor a $ 300 es :', contador2 )
print(f'Gastos total de la empresa en sueldos es: $ {gastos}')
'''
 # Ejercicio  No 4 ok
 # Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado) 
'''
serie = 11
x= 1
while x <= 25:
    print(serie) 
    serie = serie + 11
    x = x + 1
'''
# Ejercicio  No 5 ok
# Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24,#
'''
m = 8
n = 1

while n <= 500:
      r = n * m
      n = n + 1
      if r <= 500:
         print('{} '.format(r))
'''       
# Ejercicio  No 6 ok
# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
'''
suma1 = 0
suma2=  0
x = 1

while x <= 15:
    valor= int(input('Ingrese un valor entero de la lista No 1 :'))
    suma1 = suma1 + valor
    x = x + 1
x = 1
print('        ')
while x <= 15:
    valor=int(input('Ingrese un valor entero de la lista No 2 :'))
    suma2 = suma2 + valor
    x = x + 1
x = 1
if suma1 > suma2:
    print('Lista 1 mayor ')
else:
    if suma2 > suma1:
        print('Lista 2 mayor ')
    else:
        if suma1 == suma2:
         print('Listas iguales ')
'''

# ejercicio 7
#7. Desarrollar un programa que permita cargar n números enteros y luego nos informe #cuántos valores fueron pares y cuántos impares. Emplear el operador “%” en la condición #de la estructura condicional (este operador retorna el resto de la división de dos #valores, por ejemplo 11%2 retorna un 1): if valor%2==0:

contadorPares = 0
contadorImpares = 0
valor = 0
n = int(input('Ingrese cantidad de valores a revisar :'))

x = 1
while x <= n :
    valor = int(input('Ingrese valor : '))
    if valor%2 == 0:
        contadorPares = contadorPares + 1
    else:
        contadorImpares = contadorImpares + 1
    
    x = x + 1

print(contadorPares)
print(contadorImpares)
    
print('La cantidad de valores par ,  son :', contadorPares)
print('La cantidad de valores inpar, son :', contadorImpares )


'''
frutas = ['Manzana', 'Pera', 'Mango', 'Fresa']
for i in frutas:
    print(i)
'''
'''
valores = {'a': 14 , 'e': 3, 'i' : 8, 'o' : 5}
for n in valores.values():
    print(n)
for k, v in valores.items():
    print('k =', k , ', v = ',v)
print('\n')    
for i in range(11):
    print(i)

numeros = [1, 2, 4, 7, 5, 8, 6]
for n in numeros:
    if n == 3:
       print('Si se encontró el elemento = ', n)
else:
    print('No se encontró el número 3')
    '''

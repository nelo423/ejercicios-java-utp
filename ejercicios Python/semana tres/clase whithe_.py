# ciclo white
'''n = 5
while n > 0:
      print(n)
      n = n - 1
print('Despegue !')

n = 1
while n <= 10:
      print(n)
      n = n + 1
'''
# 5 x 1 =5
# 5 x 2 = 10
# 5 x 3 = 15
while True:
      try:    
         a = input("Tabla de multiplicar? ")
         n = 1
         while n <= 10:
               r = int(a) * n
               print("{} X {} = {}".format(a,n,r))
               n = n + 1
         break
      except ValueError:

            print("Lo que se digitó no es un número, intentelo nuevamente")
# break

'''

x = 0
x = x + 11225
print(x)
'''
'''i = 1
while i != 10 and i <= 10:
     print(i)
     i = i+ 2
print("Terminé")
'''

#Bucle ‘while’ controlado por Evento
'''promedio, total, contar = 0.0, 0, 0
print("Introduzca la nota de un estudiante (-1 para salir): ")
grado = int(input())
while grado != -1:
      total = total + grado
      contar = contar + 1
      print("Introduzca la nota de un estudiante (-1 para salir): ")
      grado = int(input())
      promedio = total / contar
print("Promedio de notas del grado escolar es: " + str(promedio))
'''
# Bucle ‘while’ con ‘else’
'''promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "
grado = int(input(mensaje))
while grado != -1:
      total = total + grado
      contar += 1
      grado = int(input(mensaje))
else:
     promedio = total / contar
print("Promedio de notas del grado escolar: " + str(promedio))
'''
# Sentencia break
'''variable = 10
while variable > 0:
      print('Actual valor de variable:', variable)
      variable = variable -1
      if variable == 5:
       break
      '''
# Sentencia continue
'''variable = 10
while variable > 0:
      variable = variable -1
      if variable == 5:
         continue
print('Actual valor de variable:', variable) 
'''
'''
# Sucesión de Fibonacci   NO DIO RESULTADO ######REVISAR CON PROFESOR
a: int = 0
b: int = 1
while b:int < 100:
print(b)
print(a)
print(b = b)
print( a + b) 
'''
'''
#Los ciclos for
for x in range(0, 3):
      print("Estamos en la iteración " + str(x))

for j in range(0, 10, 2):
      print("Estamos en la iteración " + str(j))

for j in range(10, 0, -2):
      print("Estamos en la iteración " + str(j))

oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # convierte a una lista cada palabra
print("La oración analizada es:", oracion, ".\n")
for palabra in range(len(frases)):
            print("Palabra: {0}, en la frase su posición es: {1}".format(frases[palabra], palabra))
'''
'''
# Bucle ‘for’ con Diccionarios
datos_basicos = {
"nombres":"Leonardo Jose",
"apellidos":"Caballero Garcia",
"cedula":"26938401",
"fecha_nacimiento":"03/12/1980",
"lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
"nacionalidad":"Venezolana",
"estado_civil":"Soltero"
}
clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()
for clave, valor in cantidad_datos:
    print(clave + ": " + valor)


frutas = {'Fresa':'roja', 'Limon':'verde','Papaya':'naranja','Manzana':'amarilla', 'Guayaba':'rosa'}
for nombre, color in frutas.items():
                  print(nombre, "es de color", color)

frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for llave in frutas:
           print(llave, 'es de color', frutas[llave])
'''
'''
# Bucle ‘for’ con ‘else’
db_connection = "127.0.0.1","5432","root","nomina"
for parametro in db_connection:
               print(parametro)
else:
     print("""El comando PostgreSQL es:
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
server=db_connection[0], port=db_connection[1],
user=db_connection[2], db_name=db_connection[3])) 
'''
print("Juego MisionTic2022")

total_preguntas = 4 #Cantidad de preguntas que tiene el juego
puntaje = 0 #Variable que almacena las opciones correctas del juego

# Primera Pregunta
respuesta = input("1. Cual es el nombre de la plataforma de MisionTic2022?")
if respuesta.lower() == "imaster":
   print("Correcto")
   puntaje = puntaje + 1 #puntaje += 1
else:
    print("Incorrecto")

# Segunda Pregunta
respuesta = input("2. En que año estamos?")
if respuesta == "2021" or respuesta == "21":
    print("Correcto")
    puntaje = puntaje + 1
else:
    print("Incorrecto")      

# Tercera Pregunta
respuesta = input("Cuanto es 8 + 4 + 1 -4 - 2 ? ")
if respuesta == "7" or respuesta.lower() == "siete":
    print("Correcto")
    puntaje = puntaje + 1
else:
    print("Incorrecto")

# Cuarta Pregunta
respuesta = input("4. Cual es el mejor lenguaje de programacion?")
if respuesta.lower() == "python":
    print("Correcto")
    puntaje = puntaje + 1
else:
    print("Incorrecto")

#resultado almacena el porcentaje de acierto
resultado = (puntaje /total_preguntas) * 100
print("Resultado {} de {}  y porcentaje de {}%.".format(puntaje,total_preguntas,resultado))

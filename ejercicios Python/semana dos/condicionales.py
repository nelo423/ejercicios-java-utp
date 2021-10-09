# Entrada
# ----> Hora Militar
# Proceso
# ----> Teniendo en cuenta la hora militar, determinar si es AM o PM
# Salida
# ----> Según la hora militar mostrar AM o PM

def validar_hora_militar(hora):
    if hora >= 12:
        mensaje = "PM"
    else:
        mensaje = "AM"
    return mensaje

hora = int(input("Digite la hora militar :" ))

print("La franja horaria hora militar {} es {}".format(hora,validar_hora_militar(hora)))



# ------------------------
#sSe puede nombrar una variable y en el imput cambiarle el nombre
# el "num" debe ser igual en los argumentos
def validar_numero(num):
    if num > 0:
        mensaje = "El número " + str(num) + " es positivo"
    if num < 0:
        mensaje = "El número " + str(num) + " es negativo"
    if num == 0:
        mensaje = "El número " + str(num) + " es cero"

    return mensaje

n = int(input("Digite número: "))

print(validar_numero(n))
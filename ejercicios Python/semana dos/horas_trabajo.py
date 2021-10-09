def horario_Trabajo (tiempo):
    if tiempo >= 8:
        mensaje = "Cumple con el horario de trabajo"
    else:
        mensaje = "No cumple con el horario de trabajo "
    return mensaje
tiempo = int(input("Ingrese la hora de entrada : "))

print("La hora de ingreso de ingreso fue {} y {} ".format(tiempo,horario_Trabajo(tiempo)))

#-------------------------------------------------------

def num_entero (num):
    if num < 0:
        num = num * (-1) 
    if num >= 1 and num <= 9:
        mensaje = "El numero tiene 1 digito" 
    else:
        if num >= 10 and num <= 99:
            mensaje = "El numero tiene 2 digitos"  
        else:
            if num >= 100 and num <= 999:
                mensaje = "El numero tiene 3 digitos" 
            else:   
                 if num >= 1000 and num <= 9999:
                     mensaje = "El numero tiene 4 digitos"
                 else:    
                     mensaje = "Mas de 4 digitos"
    return mensaje
num = int(input("Por favor, ingrese el numero un entero: "))                 
print("El numero ingresado {} contiene {} ".format(num,num_entero(num)))

#----------------------------------------------------------------------
def num_entero (num):
    if num < 0:
        num = num * (-1) 
    if num >= 1 and num <= 9:
        mensaje = "El numero tiene 1 digito" 
    elif num >= 10 and num <= 99:
          mensaje = "El numero tiene 2 digitos"  
    elif num >= 100 and num <= 999:
          mensaje = "El numero tiene 3 digitos" 
    elif num >= 1000 and num <= 9999:
          mensaje = "El numero tiene 4 digitos"
    else:    
        mensaje = "Mas de 4 digitos"
    return mensaje
num = int(input("Por favor, ingrese el numero un entero: "))                 
print("El numero ingresado {} contiene {} ".format(num,num_entero(num)))

# Actividad:
# Consultar la estructura de casos o “switch” como aparece en algunos lenguajes de programación.
# ¿Estas estructuras se pueden anidar?
# ¿Se pueden mezclar con las estructuras de los condicionales?

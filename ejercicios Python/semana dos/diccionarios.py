#Diccionarios

telefonos = {
    "referencia": "MOTO6G",
    "modelo": "eclipse",
    "color": {
        "color1": "Negro",
        "color2": "Gris",
        "color3": "Azul"
    },
    "memoria": 4,
    "camara": 18
}

#print(telefonos["referencia"])
#print(telefonos["color"]["color1"])

#print(telefonos)
#print(telefonos["color"] + " " + str(telefonos["camara"]))

if telefonos["camara"] >= 28:
    recomendacion = {"ref": telefonos["referencia"], "item": "Alta Definición"}
else:
    recomendacion = {"ref": telefonos["referencia"], "item": "Baja Definición"}

print(recomendacion)
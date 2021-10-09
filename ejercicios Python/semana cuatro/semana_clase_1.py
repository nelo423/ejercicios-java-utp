#------list comprenhension-----
mi_lista = []
for x in range(4,31,2):
    mi_lista.append(x)
print(mi_lista)

print( [x for x in range(4, 31, 2)] )

print( [x**2 for x in range(4, 31, 2) if x%3 == 0] )


'''
# listas###
nombres = []
edades = []
for x in range(5):
    nom = input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed = int(input("Ingrese la edad de la persona: "))
    edades.append(ed)

    print("Nombres de las personas mayores de edad: ")

for x in range(5):
    if edades[x] >= 18:
        print(nombres[x])
'''
'''
def calcular_ingresos(datos: list) -> dict:
    total = 0
    # Estructura para recorrer la lista
    for item in datos:
        total = total + item["valor_a_pagar"]
        # total += item["valor_a_pagar"]

    respuesta: dict = {
        "total": total
    }

    return respuesta
'''

'''************ Datos Prueba *************'''
'''
datos: list = [
    {
        "salud": "prepagada",
        "valor_a_pagar": 20000
    },
    {
        "salud": "subsidiada",
        "valor_a_pagar": 25000
    },
    {
        "salud": "prepagada",
        "valor_a_pagar": 32000
    },
    {
        "salud": "prepagada",
        "valor_a_pagar": 3000
    },
    {
        "salud": "subsidiada",
        "valor_a_pagar": 25000
    },
    {
        "salud": "prepagada",
        "valor_a_pagar": 33000
    },
    {
        "salud": "subsidiada",
        "valor_a_pagar": 28000
    }
]
print(calcular_ingresos(datos))
'''
def calcular_ingresos(datos:list) -> dict:
    prepagada: str = "prepagada"
    subsidiada: str = "subsidiada"
    total: int = 0 
    total_salud_prepagada: int = 0
    total_salud_subsidiada: int = 0
    cont_salud_prepagada: int = 0
    cont_salud_subsidiada: int = 0

    for item in datos:
        total = total + item["valor_a_pagar"]
        if item["salud"] == prepagada:
            total_salud_prepagada = total_salud_prepagada + item["valor_a_pagar"] 
            cont_salud_prepagada = cont_salud_prepagada + 1
        elif item["salud"] == subsidiada:
             total_salud_subsidiada = total_salud_subsidiada + item["valor_a_pagar"]
             cont_salud_subsidiada = cont_salud_subsidiada + 1
    promedio_prepagada: float = 0
    promedio_subsidiada: float = 0
    if cont_salud_prepagada > 0:
        promedio_prepagada= round((total_salud_prepagada / cont_salud_prepagada),2)
    if cont_salud_subsidiada > 0:
        promedio_subsidiada= round((total_salud_subsidiada / cont_salud_subsidiada),2)
    respuesta : dict = {
        "total" : total,
        "promedio_salud_prepagada"  : promedio_prepagada,
        "promedio_salud_subsidiada" : promedio_subsidiada
    }
    return respuesta
    
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
        "valor_a_pagar": 38000
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
from functools import reduce

def max_transacciones_anuales(datos:dict)-> tuple:
    promedio_transacciones: list = []

    for clave, valor in datos.items():
        total_transacciones: int = 0
        cont: int = 0
        for transacciones in valor["transacciones"]:
            for mes, sedes in transacciones.items():
                for sede, ventas in sedes.items():
                    total_transacciones += ventas
                    cont += 1
        nit = list(valor["nit"])   
        pares = [int(x) for x in list(filter(lambda x: int(x)%2 == 0, nit))]
        impares = [int(x) for x in list(filter(lambda x: int(x)%2 == 1, nit))]
        codificacion = list(map(lambda n: n*(reduce(lambda acum=0, element=0: acum + element, impares)), pares))
        cod_nit = ''.join(map(str, codificacion))
        codigo = valor["empresa"][0:3] + cod_nit
        promedio = lambda totalventas, cont: total_transacciones / cont
        tupla: tuple = (codigo, valor["empresa"], promedio(total_transacciones, cont))
        promedio_transacciones.append(tupla)
    return obtener_promedio_mayor(transacciones)
def obtener_promedio_mayor(promedio_transacciones:list) -> tuple:
    mayor = 0
    tupla = tuple()
    for nit, empresa, promedio in promedio_transacciones:
        if promedio > mayor:
           mayor = promedio
           tupla = (nit, empresa, round(promedio,2))
    return tupla
  '''


#Se obtuvo
'''
***Error***↩
Traceback (most recent call last):↩
  File "__tester__.python3", line 276, in <module>↩
    print(max_transacciones_anuales(datos))↩
  File "__tester__.python3", line 23, in max_transacciones_anuales↩
    return obtener_promedio_mayor(transacciones)↩
  File "__tester__.python3", line 27, in obtener_promedio_mayor↩
    for nit, empresa, promedio in promedio_transacciones:↩
ValueError: too many values to unpack (expected 3)
'''


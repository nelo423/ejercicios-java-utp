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
    return obtener_promedio_mayor(promedio_transacciones)
def obtener_promedio_mayor(promedio_transacciones:list) -> tuple:
    mayor = 0
    tupla = tuple()
    for nit, empresa, promedio in promedio_transacciones:
        if promedio > mayor:
           mayor = promedio
           tupla = (nit, empresa, round(promedio,2))
    return tupla

datos  =  { 
    "01" :  { 
        "empresa" :  "Servientrega" , 
        "nit" :  "890345678" , 
        "ciudad" :  "Cali" , 
        "transacciones" :  [ 
            { 
                "enero" :  { 
                    "sede1" :  350 , 
                    " sede2 " :  1200 , 
                    " sede3 " :  220 , 
                    " sede4 " :  1500 
                } 
            }, 
            { 
                " febrero " :  { 
                    "sede1 " :  1050 , 
                    " sede2 " : 500 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "marzo" :  { 
                    "sede1" :  200 , 
                    "sede2" :  500 , 
                    "sede3" :  100 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                " abril " :  { 
                    " sede1 " :  200 , 
                    " sede2 " :  500 , 
                    " sede3 " :  400 , 
                    " sede4 " : 350 
                } 
            }, 
            {
                "mayo" :  { 
                    "sede1" :  300 , 
                    "sede2" :  500 , 
                    "sede3" :  300 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "junio" :  { 
                    "sede1" :  200 , 
                    "sede2" :  250 , 
                    " sede3 " :  1000 , 
                    " sede4 " :  150 
                } 
            }, 
            { 
                " julio " :  { 
                    " sede1 " :  1000 , 
                    "sede2 " :  500 ,
                    "sede3" :  1000 , 
                    "sede4" :  450 
                } 
            }, 
            { 
                "agosto" :  { 
                    "sede1" :  3000 , 
                    "sede2" :  250 , 
                    "sede3" :  2000 , 
                    "sede4" :  150 
                } 
            }, 
            { 
                "septiembre" :  { 
                    "sede1" :  1000 , 
                    "sede2" :  500 , 
                    "sede3" :  1000 , 
                    "sede4" : 450 
                } 
            }, 
            { 
                "octubre":  { 
                    "sede1" :  1000 , 
                    "sede2" :  500 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "noviembre" :  { 
                    "sede1" :  1000 , 
                    "sede2" :  500 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "diciembre" :  { 
                    "sede1" :  600 , 
                    "sede2" : 650 , 
                    "sede3":  500 , 
                    "sede4" :  550 
                } 
            } 
        ] 
    }, 
    "02" :  { 
        "empresa" :  "Envia" , 
        "nit" :  "890123112" , 
        "ciudad" :  "Cali" , 
        "transacciones" :  [ 
            { 
                "enero " :  { 
                    " sede1 " :  250 , 
                    " sede2 " :  1000 , 
                    " sede3 " :  200 , 
                    " sede4 " : 250 
                } 
            }, 
            { 
                "febrero" :  {
                    "sede1" :  400 , 
                    "sede2" :  500 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "marzo" :  { 
                    "sede1" :  300 , 
                    "sede2" :  500 , 
                    "sede3" :  300 , 
                    "sede4" :  150 
                } 
            }, 
            { 
                "abril" :  { 
                    "sede1" :  400 , 
                    "sede2" :  540 ,
                    "sede3" :  2600 ,
                    "sede4" :  280 
                } 
            }, 
            { 
                "mayo" :  { 
                    "sede1" :  1000 , 
                    "sede2" :  500 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "junio" :  { 
                    "sede1" :  400 , 
                    "sede2" :  500 , 
                    "sede3" :  200 , 
                    "sede4" :  450 
                } 
            }, 
            { 
                "julio" : { 
                    "sede1" :  100, 
                    "sede2" :  500 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "agosto" :  { 
                    "sede1" :  150 , 
                    "sede2" :  350 , 
                    "sede3" :  200 , 
                    "sede4" :  250 
                } 
            }, 
            { 
                "septiembre" :  { 
                    "sede1" :  300 , 
                    "sede2" :  500 , 
                    "sede3" : 300 , 
                    "sede4" : 350 
                } 
            }, 
            { 
                "octubre" :  { 
                    "sede1" :  400 , 
                    "sede2" :  400 , 
                    "sede3" :  400 , 
                    "sede4" :  450 
                } 
            }, 
            { 
                "noviembre" :  { 
                    "sede1" :  400 , 
                    "sede2 " :  550 , 
                    " sede3 " :  600 , 
                    " sede4 " :  750 
                } 
            }, 
            { 
                " diciembre " :  { 
                    " sede1 ":  1000 ,
                    "sede2" :  500 , 
                    "sede3" :  400 , 
                    "sede4" :  250 
                } 
            } 
        ] 
    } 
}
print(max_transacciones_anuales(datos))


# a continuacion definimos la funcion para calcular el promedio de trabajos subidos

def promedioTrabajos(nombre: str, a: int, b: int, c: int, d: int, e: int) -> str:
    # calculamos el factor de trabajos cargados
    factor = str((a + b + c + d + e ) * 0.25)
    # calculamos el promedio de los trabajos subidos
    promedio = ((a + b + c + d + e) / 5)
    # calculo del rodendonde de un decimal del promedio de los trabajos cargados
    promedioRedondeado = round(promedio, 1)
    # convertimos el promedio redondeado a una cadena
    promedioCadena = str(promedioRedondeado)
    return "El factor de trabajos subidos fue {} y el promedio de los trabajos subidos por semana de {} fue: {}".format(factor, nombre, promedioCadena)
print(promedioTrabajos("Felipe Perez", 2,1,3,5,10 ))



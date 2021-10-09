#diccionario
def notas(nota1, nota2, nota3):
    promedio =round((dicnotas['nota1']  + dicnotas['nota2'] + dicnotas['nota3']) /3,2)
    maximo = max(dicnotas['nota1'], dicnotas['nota2'], dicnotas['nota3'])
    minimo = min(dicnotas['nota1'], dicnotas['nota2'], dicnotas['nota3'])
    if promedio >= 0 and promedio < 3:
        rendimiento ='bajo'
    else:
        if promedio >= 3 and promedio < 4:
            rendimiento = 'medio'
        else:
            if promedio >= 4 and promedio < 5:
               rendimiento = 'alto'

    return f'El estudiante tiene una nota promedio de {promedio} ,su mayor nota fue {maximo} y su numer nota fue {minimo} y su rendimiento fue  {rendimiento}',
dicnotas ={'nota1':3.5, 'nota2':4, 'nota3': 4.6}

print(notas(3.5,4,4.6))
print(notas(4,5,5))
print(notas(3,2,1))

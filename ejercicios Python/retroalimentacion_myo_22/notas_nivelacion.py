def notas(nota1, nota2, nota3):
    promedio =round((nota1 +nota2 + nota3) /3,2)
    maximo = max(nota1,nota2,nota3)
    minimo = min(nota1,nota2,nota3)
    if promedio >= 0 and promedio < 3:
        rendimiento ='bajo'
    if promedio >= 3 and promedio < 4:
        rendimiento = 'medio'
    if promedio >= 4 and promedio < 5:
        rendimiento = 'alto'

    return f'El estudiante tiene una nota promedio de {promedio} ,su mayor nota fue {maximo} y su numer nota fue {minimo} y su rendimiento fue  {rendimiento}',
print(notas(3.5,4,4.6))
print(notas(4,5,5))
print(notas(3,2,1))

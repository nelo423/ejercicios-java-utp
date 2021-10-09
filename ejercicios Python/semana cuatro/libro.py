'''
import openpyxl 
book = openpyxl.load_workbook("catalogo.xlsx", data_only = True)
hoja = book.active
celdas = hoja['A2' : 'D4']
for fila in celdas: 
    print ([celdas.value for celda in fila])
'''
# https://www.youtube.com/watch?v=1xjgY5Wpwto
#  libreria para cargar archivos de excel en python     pip instalar openpyxl
# para cargar la libreria pip install matplotlib por medio de la terminal de visual studio code

# ejemplo programacion estructurada
def notas_quices(codigo:str, nota1:int, nota2:int, nota3:int, nota4:int, nota5:int) -> str:
    nota1 =100
    nota2 = 50
    nota3 = 40
    nota4 = 50
    nota5 = 50
    codigo = (input('Ingrese codigo estudiante :'))
    medicion_maxima_promedio = 5
    max_nota = 100
    total_nota_sin_menor = 4
    calcular = 0
    if(nota1 < nota2 and nota1 < nota3 and nota1 < nota4 and nota1 < nota4 ):
       calcular = (nota2+nota3+nota4+nota5)/total_nota_sin_menor
       calcular = (calcular * 5)/100
    elif(nota2 <= nota1 and nota2 <= nota3 and nota2 <= nota4 and nota2 <=nota5):
        calcular =(nota1+nota3+nota4+nota5)/total_nota_sin_menor
        calcular =(calcular * 5)/100
    elif(nota3 <= nota1 and nota3 <= nota2 and nota3 <= nota4 and nota3 <= nota5):
        calcular = (nota1+nota2+nota4+nota5)/total_nota_sin_menor
        calcular = (calcular * 5)/100
    elif(nota4 <= nota1 and nota4 <= nota2 and nota4 <= nota3 and nota4 <= nota5):
        calcular = (nota1+nota2+nota3+nota5)/max_nota
        calcular = (calcular * 5)/100
    elif(nota5 <= nota1 and nota5 <= nota2 and nota5 <= nota3 and nota5 <= nota4):
        calcular = (nota1+nota2+nota3+nota4)/max_nota
        calcular = (calcular * 5)/100
    calcular = round(calcular, 2)
    return f"El promedio ajsutado del estudiante {codigo} es: {calcular}  "


    






x = 1
contador1 = 0
contador2 = 0
gastos = 0
sueldo = 0.0

n = int(input('Ingrese cantida de empleados de la empresa :'))

while x <= n :
    sueldo = float(input('Ingrese sueldo del empleado :'))
    if sueldo <= 300:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
    gastos = gastos + sueldo
    x = x + 1
print('Cantidad de empleados con sueldos entre 100 y 300 es :', contador1)
print('Cantidad de empleados con sueldo mayor a 300 es :', contador2 )
print('Gastos total de la empresa en sueldos es : ', gastos)



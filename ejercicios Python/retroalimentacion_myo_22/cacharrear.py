'''
while True:
    try:
        edad = int(input("Escribe tu edad: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if edad < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break
pass
'''

print('ingrese valor')
ret=int(input())
if ret%2==0:
    print('El numero digitdo es par')
else:
    print('El numero digitado no es par')

if ret%2!=0:
    print('El numero digitado es impar')
else:
    
    print('El numero digitado es par')


#x = 1
#while x <= 10:
#    print(x)
#    x = x + 1

#for x in range(10):
#    print(x+1)

#for x in range(1,11):
#    print(x)

#for x in range(1,11,1):
#    print(x)
lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] 

for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
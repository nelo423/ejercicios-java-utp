# reto 1 nivelacion
def promedio_salarial(laura:int , juan:int , andres:int , sara: int ,natalia:int)->str:
    promedio= (round(((laura*3600) + (juan) + (andres) + (sara*3600) + (natalia*3600))/5),2)
    return f'El promedio salarial es: {promedio}  pesos colombianos'
    
print(promedio_salarial(1500,180000,2750000,2100,3500))


print(max(12,24,36,48))

print(min(12,24,36,48))

#print(sum(1,2))

print(range(1,1,5))



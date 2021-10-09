'''
import pandas as pd

ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
print(ventas)

print(ventas[0])

print(ventas["Ene"])

print(ventas.index)
print(ventas.values)

ventas.name = "Ventas 2021"
print(ventas.name)
print(ventas)

ventas.index.name = "Meses"
print(ventas)

#-----------------------------

import pandas as pd
datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }

compras = pd.DataFrame( datos )

print(compras)

compras = pd.DataFrame( datos , index = [ 'Juno' , 'Robert' , 'Lily' , 'David' ])  

print(compras)

print(compras.index)

print(compras.columns)


compras.index.name = "Clientes"
compras.columns.name = "Frutas"

print(compras)
'''
'''import pandas as pd
df = pd.read_csv("titanic3.csv", header=0)
print(df.to_string()) 

print('-------------------------------------------------------')
import pandas as pd
datos = pd.read_csv('example.csv', header=0)
print(df.to_string())
'''
import pandas as pd
datos = pd.read_csv("https://misiontic.000webhostapp.com/casos_covid.csv", header=0)
print(pd.to_string())
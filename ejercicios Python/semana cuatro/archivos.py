import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

datosDataFrame = pd.DataFrame(data)

print(datosDataFrame)

#Acaba la implementacion

datosDataFrame.to_csv('example.csv')

datosDataFrame.to_csv('nombre_salida.csv', sep=';')

df = pd.read_csv('example.csv')

print(df)


import pandas  as pd
datos = pd.read_csv("https://misiontic.000webhostapp.com/casos_covid.csv", header=0)

def informes_covid(datos:str)->dict:
    if datos.endswith('.csv'):
        try:
            df = pd.read_csv(datos)
        except:
            return "Error al obtener los datos"
        # Obtiene el valor que más se repite
        mas_contagios = df["Edad"].mode()
        mas_contagios = mas_contagios[0]
        # Filtra los registros que sean del departamento con más contagios
        filtro = df.loc[:,"Edad"] == mas_contagios
        contagios = df[filtro]
        # Cuenta los registros (numeros de contagios)
        # Número de fallecidos
        filtro_fallecidos = contagios.loc[:,"atención"] == "Fallecido"
        fallecidos = contagios[filtro_fallecidos]
        #Número de recuperados
        filtro_recuperados = contagios.loc[:,"atención"] == "Recuperado"
        recuperados = contagios[filtro_recuperados]

        # Crea el diccionario respuesta
        respuesta: dict = {
            "mayor_contagio": mas_contagios,
            "cantidad_contagios": contagios["Edad"].count(),
            "fallecidos": fallecidos["atención"].count(),
            "recuperados": recuperados["atención"].count()
        }
    else:
        return "Extensión de archivo inválida"
    
    return respuesta


print(informes_covid("https://misiontic.000webhostapp.com/casos_covid.csv"))



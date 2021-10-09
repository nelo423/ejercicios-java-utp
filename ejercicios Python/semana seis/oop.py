class FocoDeLuz:
    #__estaEncendido = False
    tamano = 0; voltaje = 0; intensidad ='' ; potencia = 0; tipoFoco = '' # cms, voltios, watts, lumens

    def __init__ (self,tamano,voltaje,intensidad,potencia,tipoFoco):
        self.tamano = tamano
        self.voltaje = voltaje
        self.intensidad = intensidad
        self.potencia = potencia
        self.tipoFoco = tipoFoco
        self.__estaEncendido = False
        
    def Prender(self):
        print('El foco se encendio')
        self.__estaEncendido = True
    def Apagar(self):
        print('El foco se apago')
        self.__estaEncendido = False
    def mostrarPrpiedades(self):
        self.tamano
        print('--------------------------')
        print('El tamaño del foco es : ' + str(self.tamano))
        print('El voltaje del foco es : ' + str(self.voltaje))
        print('La intensidad del foco es : ' + str(self.intensidad))
        print('La potencia del foco es : ' + str(self.potencia))
        print('El tipo de foco es : ' + str(self.tipoFoco))
        msn = 'Encendido' if self.__estaEncendido else 'Apagado'
        print('-------------------------- El foco esta :' + msn )

objetoFocoLuz1 = FocoDeLuz(5,120,' 1900 lumens',15,'Ahorrador')
objetoFocoLuz2 = FocoDeLuz(10,100,' 2500 lumens',12,'Incandecente')

#print(objetoFocoLuz1)
#print(objetoFocoLuz2)
objetoFocoLuz1.Prender()
objetoFocoLuz1.mostrarPrpiedades()
objetoFocoLuz2.mostrarPrpiedades()
#objetoFocoLuz.Apagar()
#print(objetoFocoLuz.voltaje)
#objetoFocoLuz.mostrarPrpiedades()
#print(objetoFocoLuz.intensidad)


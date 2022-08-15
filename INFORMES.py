from numpy import DataSource
from mondb import *
import matplotlib.pyplot as pl

class GraficaInforme():
    '''Clase GraficaInforme, que contiene el proceso para poder dibujar grafica de pastel gracias a matplolib.
    
    Atributo.
    ----
    - Kery: El cual es un kery para el  diccionario que recibimos del mogndb. 
    
    Metodos.
    ------------
    - Graficar(): Metodo para poder graficar a patir de las cantidades de datos que nos pasa un metodo del modulo mondb. '''
    def __init__(self, kery):
        '''Metodo constructor donde estan los atributos de la clase. 
        
        Parámetros. 
        ----
        - kery: De tipo str.
                El cual para el kery del diccionario y el con el simbolo $.
                
        Atributo: 
        --------
        - self.kery: Para poder tener el kery del diccionario. '''
        self.kery = kery

    def Graficar(self):
        '''Metodo Graficar, que sirve para hacer le dibujo de la grafica en pastel de los datos obtenidos, una lista de lacantidad y una lista de los nombre de los datos. 
        
        Recibe. 
        -------
        - Objeto: mensajesPrint, instancia de la clase BuscarEnBaseDato. 
                El cual pasamos los datos del mongodb.
                
        Función.
        -------
        - pie: Para hecer el grafico de pastel. '''
        mensajesPrint = BuscarEnBaseDato( coleccion="COL_CiudadanosEcuadorCNE" ,db="DB_Ciudadanos_Ecuador_CNE_ITIN")
        dato = mensajesPrint.BUscarTodo(self.kery)
        dato2 = mensajesPrint.BUscarTodo(self.kery)
        lista = []
        palabras = []
        for diccionario in dato: 
            lista.append(diccionario['total'])
        
        for diccionario in dato2:
            palabras.append(diccionario['_id'])

        for diccopnario in lista:
            print(diccopnario)
        pl.pie(lista, labels=palabras, autopct=('%1.f%%'))
        pl.show()

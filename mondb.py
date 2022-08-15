'''Modulo para trabajar con la o las bases de datos, que utilizaremos en el programa. El cual contiene clase o clases. 

Clase
-----
- BuscarEnBaseDato(): El cual nos conecta con el la base de datos y hace un busqueda en ella. '''
import pymongo

class BuscarEnBaseDato():
    '''Clase BuscarEnBaseDato, el cual hace la conección con el mongoDB y todos los datos en la que agamos la busqueda. 
    
    Atributos
    ---
    - self.apellido: El cual es de la persona el apellido. 
    - self.nombre: El cual es de la persona el nombre
    - self.datoRestriccion: El cual contiene el dato  buscar en la base de datos.
    - self.coleccion: La colección.  
    - self.cedula: Para conseguir y pasar el numero de cédula. 
    - self.DB: La base de datos. 
    - miCliente: el cual es estatico, que contiene la conección al mongoDB. 

    Metodos
    -----
    def __init__(self,  coleccion, db): Este es el constructor. 
    def recibirDatoBusqueda(self, dato): El cual recibe datos la un atributo en específico.
    def RecibirNombre(self, nombre, apellido): El cual pasa los valores que recibe a el atributo nombre y apellido.  
    def __ConeccionDB(self): Este sirve para hacer la coneccion con el mongoDB. 
    def BuscaRestriccion(self): El cual hace una busqueda de los datos a buscar en una  base de datos. 
    def Buscar(self, dato): Este sirve para buscar en la base de datos. 
    def BUscarTodo(self, dato): El cual hace un conteo de los datos repetidos en mongoDB. 
    '''
    miCliente=pymongo.MongoClient("mongodb://localhost:27017/")
    def __init__(self, coleccion, db):
        '''Metodo constructor, el cual contiene los atributos de la clase BuscarEnBaseDato.
        
        Atributos.
        -----
        - apellido: De tipo inicial None. De tipo str. \n 
        - nombre: De tipo inicial None. De tipo str. \n 
        - datoRestriccion: De tipo inicial None, alberga str. 
        - coleccion: De tipo str. \n 
        - cedula: De tipo str. \n
        - db: De tipo str. \n 

        Parametros.
        ------
        - coleccion: De tipo str. \n 
        - db: De tipo str. \n
        '''
        self.apellido = None
        self.nombre =None
        self.datoRestriccion = None
        self.cedula = None
        self.coleccion = coleccion
        self.DB = db
    def recibirDatoBusqueda(self, dato):
        '''Metodo recibirDatoBusqueda de la clase BuscarEnBaseDato, el cual se encarga de cargar el dato que recibe a un atributo llamdo self.datoRestriccion. 
        
        Parametro.
        ------
        - dato: Tipo str. 
                El cual sirve de puente para pasar los datos al atributo datoRestriccion. '''
        self.datoRestriccion = dato
    
    def RecibirNombre(self, nombre, apellido, cedula):
        '''Metodo RecibirNombre de la clase BuscarEnBaseDato, el cual se encarga de cargar los datos a los atributos de nombre y apellido.
        
        Parametros.
        ----
        - nombre: Tipo str.\n
                    Ingresaria el nombre que tenga relacion en la base de datos de los ciudadanos.  
        - apellido: Tipo str.\n
                    Ingresaria el apellido que tenga relacion en la base de datos de los ciudadanos. '''
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
    def __ConeccionDB(self):
        '''Metodo pribado __ConeccionDB, el cual contiene la coneccion de la base de datos. 
        
        Retorna 
        ---
        - myCollection: El cual es la coneccion de la base de datos del mongoDB, obteniendo la coleccion a buscar los documentos. '''
        mydb=self.miCliente[self.DB]
        myCollection=mydb[self.coleccion]
        return myCollection
        
    def BuscaRestriccion(self):
        '''Metodo BuscaRestriccion, de la clase BuscarEnBaseDato, el cual hace una busqueda en la base de datos y retornaese valor. 
        
        Retorna.
        ------
        - return datoEncontrado['dato'], el cual rescata de una base de datos en tipo diccionarion el dato de una sección. '''
        coleccion =self.__ConeccionDB()
        datoEncontrado = coleccion.find_one({'descripcion':self.datoRestriccion})
        dato = datoEncontrado
        return datoEncontrado['dato']

    def BUscarTodo(self, dato):
        '''Metodo BUscarTodo, de la clase BuscarEnBaseDato, el cual retorna un diccionario con el total de datos repetidos en una colección. 
        
        Parametros. 
        -------
        - dato: El cual es en que tipo de dato buscara en la clección. 
        
        Retorna. 
        -----------
        - return  agg_result: El cual retorna un diccionario. '''
        coleccion =self.__ConeccionDB()
        datos = coleccion.count_documents({})
        agg_result= coleccion.aggregate( 
    [{ 
    "$group" :  
        {"_id" : dato,   
         "total" : {"$sum" : 1} 
         }} 
    ])
        return  agg_result
        
    

    def Buscar(self, dato):
        '''Metodo Buscar de la clase BuscarEnBaseDato, el cual retorna los datos de un ciudadano. 
        
        Parametros. 
        -----
        - dato: De tipo str.
                ES la cualidad de una persona segun eso retornara algo. \n

        Condicion. 
        ----
        - if self.cedula == 'Ingrese cedula': Si ingresa por numero de cedula con ejecutar la busqueda por nombre y apellido. 
                
        -----
        Ejemplo de dato. 
        -----
        -  id: 000,  nombre: Mateo, apellido: Lopez,
        numeroCedula  :  1724564985   ,  ocupacion:Estudiante Superior,
         Residencia: Cuenca,    Nacionalidad : Ecuatoriano
         
        -----
        Retorna:
        ----
        - return datoEncontrado['nombre']:\n
                 Nos reotorna el --   nombre     ---- del ciudadano. \n
        - return datoEncontrado['apellido']:\n
                 Nos reotorna el --   apellido     ---- del ciudadano. \n
        - return datoEncontrado['numeroCedula']:\n
                 Nos reotorna el --   numero de cedula     ---- del ciudadano. \n
        - return datoEncontrado['ocupacion']:\n
                 Nos reotorna el --   ocupacion     ---- del ciudadano. \n
        - return datoEncontrado['Residencia']:\n
                 Nos reotorna el --    recidencia    ---- del ciudadano. \n
        - return datoEncontrado['fecha de nacimiento']:\n
                 Nos reotorna el --    fecha de nacimiento    ---- del ciudadano. \n
        - return datoEncontrado['discapacidad']:\n
                 Nos reotorna el --    discapacidad    ---- del ciudadano. \n
        - return datoEncontrado['Nacionalidad']:\n
                 Nos reotorna el --    nacionalidad    ---- del ciudadano.   \n
'''
        coleccion =self.__ConeccionDB()
        self.datoEncontrado =None
        if self.cedula == 'Ingrese cedula':
            self.datoEncontrado = coleccion.find_one({'nombre':self.nombre, 'apellido':self.apellido})
        else:
            self.datoEncontrado = coleccion.find_one({'cedula_de_identidad': self.cedula})
        if dato == 'nombre':
            return self.datoEncontrado['nombre']
        elif dato == 'apellido':
            return self.datoEncontrado['apellido']
        elif dato == 'cedula de identidad':
            return self.datoEncontrado['cedula_de_identidad']
        elif dato == 'ocupacion':
            return self.datoEncontrado['ocupacion']
        elif dato == 'residencia ':
            return self.datoEncontrado['residencia']
        elif dato == 'fecha de nacimiento':
            return self.datoEncontrado['fecha_de_nacimiento']
        elif dato == 'nacionalidad':
            return self.datoEncontrado['nacionalidad']
        elif dato == 'discapacidad':
            return self.datoEncontrado['discapacidad']



import unittest
from mondb import BuscarEnBaseDato as dbBusca
class pruebaUnitariaMetodoBusquedaPersona(unittest.TestCase):
    '''CLase pruebaUnitariaMetodoBusquedaPersona, que hereda de unittest.TestCase, para poder comprobar los pases de datos. 
    
    Atributos Estaticos.. 
    -------
    - dato: Conccionamongo db de la coleccion ciudadano. 
    - dato1: Conccionamongo db de la coleccion ciudadano por cedula.
    
    Metodos.
    --------
    - test1(self): Comprueba si pasa del ciudadano el nombre .
    - test2(self): Comprueba si pasa del ciudadano el apellido.
    - test3(self): Comprueba si pasa del ciudadano el cedula de identidad.
    - test4(self): Comprueba si pasa del ciudadano el ocupacion.
    - test5(self): Comprueba si pasa del ciudadano el residencia.
    - test6(self): Comprueba si pasa del ciudadano el fecha de nacimiento.
    - test7(self): Comprueba si pasa del ciudadano el nacionalidad.
    - test8(self): Comprueba si pasa del ciudadano el discapacidad.
     '''
    dato = dbBusca('COL_PERSONA_USUARIO', 'DB_CNE_CIUDADANOS')
    dato.RecibirNombre('Amancio Sebastian','Pereira Morales', 'Ingrese cedula' )
    dato1 = dbBusca('COL_PERSONA_USUARIO', 'DB_CNE_CIUDADANOS')
    dato1.RecibirNombre('','', '7493118337' )
    
    def test1(self):
        '''test1(self): Comprueba si pasa del ciudadano el nombre .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato.Buscar('nombre'), 'Amancio Sebastian')

    def test2(self):
        '''test2(self): Comprueba si pasa del ciudadano el apellido .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato.Buscar('apellido'), 'Pereira Morales')

    def test3(self):
        '''test3(self): Comprueba si pasa del ciudadano el cedula de identidad .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato.Buscar('cedula de identidad'), '7493118337')

    def test4(self):
        '''test4(self): Comprueba si pasa del ciudadano el ocupacion .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato.Buscar('ocupacion'), 'Policia')
    
    def test5(self):
        '''test5(self): Comprueba si pasa del ciudadano el residencia .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato.Buscar('residencia '), 'Bolivar/Guaranda')
    def test6(self):
        '''test6(self): Comprueba si pasa del ciudadano el fecha de nacimiento .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato1.Buscar('fecha de nacimiento'), '1999-01-27')

    def test7(self):
        '''test7(self): Comprueba si pasa del ciudadano el nacionalidad .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato1.Buscar('nacionalidad'), 'Ecuatoriano')

    def test8(self):
        '''test8(self): Comprueba si pasa del ciudadano el discapacidad .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato1.Buscar('discapacidad'), False)

class busquedaRestriciones(unittest.TestCase):
    '''CLase busquedaRestriciones, que hereda de unittest.TestCase, para poder comprobar los pases de datos de las confuguraciones para el programa. 
    
    Atributos Estaticos.. 
    -------

    - dato2: Conccionamongo db de la coleccion configuracion.
    
    Metodo.
    ------
    - def test01(self): Metodo para poder verificar si pasa los datos. '''
    
    dato2 = dbBusca('COL_CONFIGURACION_PROGRAMA', 'DB_CNE_CIUDADANOS')
    dato2.recibirDatoBusqueda('Mensaje_Votante_Facultativo')
  
    def test01(self):
        '''test01(self): Comprueba si pasa del ciudadano el nombre .
        
        Funcion:
        -----
        - assertEqual: (valor, comprueba)'''
        self.assertEqual(self.dato2.BuscaRestriccion(), "¿Usted es considerado para un voto facultativo? ")

class contarDocumetos(unittest.TestCase):
    '''Clase contarDocumetos, elcual hereda de unittest.TestCase, elcual verifica si no pasa un valor nulo. 
    
    Metodo. 
    ------
    - def testA(self): El verifica con assertIsNotNone. '''
    def testA(self):
        '''testA(self): Comprueba si no pasa un valor nulo la busqueda.
        
        Funcion:
        -----
        - assertIsNotNone: (valor, mensaje)'''
        dato = dbBusca('COL_PERSONA_USUARIO', 'DB_CNE_CIUDADANOS')
        self.assertIsNotNone(dato.BUscarTodo('$residencia'), msg= 'No se encontro la referencia a buscar. ')


    
        


if __name__== '__main__':
    unittest.main()
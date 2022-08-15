import tkinter as tk
from modulo3_Interfaz_Labels import labelNombre

STYLE = {
    "font": ("Arial", 16),
    "bg": "#363636",
    "fg": "#84C9FB"
}


MODES = {
    "NOMBRE": 'LETRA',
    "CEDULA": 'NUMERO',
   
}

class FramePrincipal(tk.Frame):
    def __init__(self, contenedor, objeto ):
        super().__init__(contenedor)
        self.controller = objeto
        self.opcion = tk.StringVar()
        self.widgets()

    def regresarAlSigiente(self):
        self.controller.opcion = self.opcion.get()
        self.controller.connectarOtroFrame(self.controller.modulo2)

    def widgets(self):
        tk.Label(
            self,
            text = "Bienvenido al sistema del reguistro civil.",
            justify = tk.CENTER,
            **STYLE
        ).pack(side = tk.TOP,fill = tk.BOTH,expand = True,padx = 22,pady = 11)
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background ="#363636")
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionsFrame,
            text = "Opcion de busqueda.",
            justify = tk.CENTER,
            **STYLE
        ).pack(side = tk.TOP,fill = tk.X,padx = 22,pady = 11)
        for (key, valor) in MODES.items():
            tk.Radiobutton(
                optionsFrame, 
                text = key , 
                variable = self.opcion,
                value = valor,
                activebackground = "#121212",
                activeforeground = "#84C9FB",
                **STYLE).pack(
                    side = tk.LEFT,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 5,
                    pady = 5
                )
        tk.Button(
            self, 
            text = "Aceptar",
            command = self.regresarAlSigiente,
            **STYLE,
            relief = tk.FLAT,
            activebackground = "#121212",
            activeforeground = "#84C9FB",
            ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )

    
class IngresaDatos(tk.Frame):

    def __init__(self, parametros, objeto):
        super().__init__(parametros)
        self.configure(background = "#363636")
        self.controller = objeto
        #   Última función a llamar
        self.datosCiudadano = tk.StringVar(self, value = "ingrese aquí.")
        self.fichero = None
        self.widgets()
        
    

    def widgets(self):
        self.opcion = self.controller.opcion
        if self.opcion =='NUMERO':
            labelNombre(self)
        tk.Button(
            self, 
            text = "Aceptar",
            **STYLE,
            relief = tk.FLAT,
            activebackground = "#363636",
            activeforeground = "#84C9FB",
            ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Button(
            self, 
            text = "Regresar",
            command = lambda: self.controller.connectarOtroFrame(self.controller.modulo1),
            **STYLE,
            relief = tk.FLAT,
            activebackground = "#121212",
            activeforeground = "#84C9FB",
            ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

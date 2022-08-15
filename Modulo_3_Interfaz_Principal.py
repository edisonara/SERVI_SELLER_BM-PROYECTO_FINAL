import tkinter as tk
from modulo3_Interfaz_secundaria1 import FramePrincipal, IngresaDatos

class VentanaPrincipal(tk.Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('VERIFICACIÓN DE VOTACIÓN DE CIUDADANOS')
        self.opcion = "LETRA"
        self.modulo1 = FramePrincipal
        self.modulo2 = IngresaDatos
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP, 
            fill = tk.BOTH, 
            expand = True
            )
        container.configure(background = "#121212")
        #   Índice de la fila/columna y lo que ocupa respecto
        #   a las demás. Una columna con weight 2 es el doble 
        #   de ancha que una con weight 1. 
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(0, weight = 1)
        self.frames = {}
        for framSec in (FramePrincipal, IngresaDatos):
            frame = framSec(container, self)
            self.frames[framSec] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.connectarOtroFrame(FramePrincipal)

    def connectarOtroFrame(self, container):
        frame = self.frames[container]
        #   Manda el frame al frente de todo
        frame.tkraise()
    


ventana = VentanaPrincipal()
ventana.mainloop()

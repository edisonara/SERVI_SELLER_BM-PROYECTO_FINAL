import tkinter as tk
STYLE = {
    "font": ("Arial", 16),
    "bg": "#363636",
    "fg": "#84C9FB"
}


MODES = {
    "NOMBRE": "LETRA",
    "CEDULA": "NUMERO",
   
}


def labelNombre(objeto):
    tk.Label(
        objeto,
        text = "Ingreso de datos. ",
        justify = tk.CENTER,
        **STYLE
    ).pack(
        side = tk.TOP,
        fill = tk.BOTH,
        expand = True,
        padx = 22,
        pady = 11
    )

    tk.Entry(
        objeto,
        textvar = objeto.datosCiudadano,
        justify = tk.CENTER,
        **STYLE
    ).pack(
        side = tk.TOP,
        fill = tk.BOTH,
        expand = True,
        padx = 22,
        pady = 11
    )

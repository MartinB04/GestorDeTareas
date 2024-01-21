import tkinter as tk
from ConexionMySQL import *

HOST = "localhost"
USER = "root"
PASSWORD = "Kazooie10"
DATABASE = "gestordetareas"


class Ventana:
    _root = None
    _label_principal = None
    _frame = None
    _frame_contenedor_etiquetas = None
        
    _boton = None

    
    def __init__(self,):
        self._root = tk.Tk()
        self._root.title("Bv")
        self._root.geometry("400x250")    
        self._root.resizable (False, False)
        
        self._frame = tk.Frame(self._root)
        self._frame.pack(padx=10, pady=10)


        
        
        #self._root.mainloop()

    
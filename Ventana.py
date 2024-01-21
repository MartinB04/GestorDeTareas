import tkinter as tk
from ConexionMySQL import *

HOST = "localhost"
USER = "root"
PASSWORD = "Kazooie10"
DATABASE = "gestordetareas"


class Ventana:
    _root = None
    _label_principal = None
    _label_nombre_usuario = None
    _entry_nombre_usuario = None
    _label_contraseña = None
    _entry_contraseña = None
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


        self._labelPrincipal = tk.Label(self._frame, text="Gestor de Tareas")
        self._labelPrincipal.pack()

        self._frame_contenedor_etiquetas = tk.Frame(self._frame)
        self._frame_contenedor_etiquetas.pack()


        self._label_nombre_usuario = tk.Label(self._frame_contenedor_etiquetas, text="Username")
        self._label_nombre_usuario.grid(row=0, column=0)
        self._entry_nombre_usuario = tk.Entry(self._frame_contenedor_etiquetas)
        self._entry_nombre_usuario.grid(row=0,column=1)

        self._label_contraseña = tk.Label(self._frame_contenedor_etiquetas, text="Password")
        self._label_contraseña.grid(row=1, column=0)
        self._entry_contraseña = tk.Entry(self._frame_contenedor_etiquetas, show="*")
        self._entry_contraseña.grid(row=1,column=1)
        
        self._boton = tk.Button(self._frame)
        self._boton.config(text="Iniciar sesion", command=self.IniciarSesion)
        self._boton.pack()
        
        self._root.mainloop()

    def IniciarSesion(self,):
        conexion = ConexionMySQL(HOST, USER, PASSWORD, DATABASE)
        consulta_select = f"SELECT * FROM Usuario WHERE `username` = '{self._entry_nombre_usuario.get()}' AND `userpassword` = '{self._entry_contraseña.get()}' ;"
        resultados = conexion.ejecutar_consulta(consulta_select)
        if resultados:
            print("Si jalo Bv")
        else:
            print("NO JALO BVBv")
            conexion.desconectar()
        
        print(f"datos ingresados {self._entry_nombre_usuario.get()} y {self._entry_contraseña.get()}")

    



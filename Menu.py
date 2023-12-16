from Usuario import *

class Menu:
    _opc = None

    def __init__(self) -> None:
        pass

    def MenuPrincipal(self):
        print("<----- Gestor de Tareas ----->")
        print("<----- Menu Principal ----->")

        print("1. Iniciar sesion")
        print("2. Buscar usuario")
        print("3. Registrar usuario")
        print("0. Salir")
        self.opc = int(input("Opc -> "))

    def MenuModificacion(self):
        print("<---- Modificar atributos ---->\n")
        print("1. User")
        print("2. Nombre")
        print("3. Password")

        self._opc = int(input("Opc -> "))
        
    def MenuSesionIniciada(self):
        print("<----Sesion iniciada----->\n")
        print("1. Agregar nueva tarea")
        print("2. Mostrar tareas")
        print("3. Editar una tarea")
        print("4. Eliminar una tarea")
        print("0. Cerrar sesion")
        
        self._opc = int(input("Opc -> "))
        
        
        

        
        print("<----Sesion iniciada----->")

    @property
    def Opc(self):
        return self.opc
from Usuario import *

class Menu:
    _opc = None

    def __init__(self) -> None:
        pass

    def MenuPrincipal(self):
        print("<----- Gestor de Tareas ----->")
        print("<----- Menu Principal ----->")

        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Modificar usuario")
        self.opc = int(input("Opc -> "))

    def MenuModificacion(self):
        print("<---- Modificar atributos ---->\n")
        print("1. User")
        print("2. Nombre")
        print("3. Password")

        self._opc = int(input("Opc -> "))
        

    @property
    def Opc(self):
        return self.opc
from Usuario import *
from ConexionMySQL import *
from Menu import *
import sys

opc = None

usuarios = []

menu = Menu()

def AgregarUsuario():
    user = input("User -> ")
    nombre = input("Nombre -> ")
    password = input("Password -> ")

    conexion = ConexionMySQL(host="localhost", user="root", password="Kazooie10", database="gestor")
    consulta_insert = "INSERT INTO Usuario (user, nombre, password) VALUES (%s, %s, %s);"
    datos_insert = (user, nombre, password)
    conexion.ejecutar_insercion(consulta_insert, datos_insert)        
    
def BuscarUsuario():
    user = input("User a buscar -> ")
    conexion = ConexionMySQL(host="localhost", user="root", password="Kazooie10", database="gestor")
    consulta_select = f"SELECT * FROM Usuario WHERE `user` = '{user}';"
    resultados = conexion.ejecutar_consulta(consulta_select)
    for fila in resultados:
        print(fila)

while opc != 0:
    
    menu.MenuPrincipal()
    opc = menu.Opc

    match opc:
        case 1: 
            AgregarUsuario()
        case 2:
            BuscarUsuario()
            
        case 3 : 
            user = input("User a buscar -> ")
            if len(usuarios) > 0:
                for u in usuarios:
                    if(user == u.User):
                        menu.MenuModificacion()
                        opc2 = menu.Opc
                        atributo = None
                        
                        match opc2:
                            case 1:
                                atributo = input("User -> ")
                                u.User(atributo)
                            case 2:
                                atributo = input("Nombre -> ")
                                u.Nombre(atributo)
                            case 3:
                                atributo = input("Password -> ")
                                u.Password(atributo)
                    else:
                        print("No >v")
            else:
                print("vacia Bv")

    
            
sys.exit()



from Usuario import *
from ConexionMySQL import *
from Menu import *
import sys

opc = None

HOST = "localhost"
USER = "root"
PASSWORD = "Kazooie10"
DATABASE = "gestordetareas"

usuarios = []

menu = Menu()

def IniciarSesion():
    user = input("User a buscar -> ")
    password = input("Password -> ")
    conexion = ConexionMySQL(HOST, USER, PASSWORD, DATABASE)
    consulta_select = f"SELECT * FROM Usuario WHERE `username` = '{user}' AND `userpassword` = '{password}' ;"
    resultados = conexion.ejecutar_consulta(consulta_select)
    if resultados:
        menu.MenuSesionIniciada()
    else:
        print("Bv")
    
    
def RegistrarUsuario():
    user = input("User -> ")
    nombre = input("Nombre -> ")
    password = input("Password -> ")

    conexion = ConexionMySQL(HOST, USER, PASSWORD, DATABASE)
    consulta_insert = "INSERT INTO Usuario (username, nombre, userpassword) VALUES (%s, %s, %s);"
    datos_insert = (user, nombre, password)
    conexion.ejecutar_insercion(consulta_insert, datos_insert)        
    
def BuscarUsuario():
    user = input("User a buscar -> ")
    conexion = ConexionMySQL(HOST, USER, PASSWORD, DATABASE)
    consulta_select = f"SELECT * FROM Usuario WHERE `username` = '{user}';"
    resultados = conexion.ejecutar_consulta(consulta_select)
    for fila in resultados:
        print(fila)

while opc != 0:
    
    menu.MenuPrincipal()
    opc = menu.Opc

    match opc:
        case 1: 
            IniciarSesion()
        case 2:
            BuscarUsuario()
            
        case 3 : 
            RegistrarUsuario()

    
            
sys.exit()



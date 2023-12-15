from Usuario import *
import sys

opc = None

usuarios = []

while opc != 0:
    print("<----- Gestor de Tareas ----->")
    print("<----- Menu Principal ----->")

    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Modificar usuario")
    opc = int(input("Opc -> "))

    match opc:
        case 1: 
            user = input("User -> ")
            nombre = input("Nombre -> ")
            password = input("Password -> ")

            usuario = Usuario(user, nombre, password)
            print(str(usuario))
            usuarios.append(usuario)
            

        case 2:
            user = input("User a buscar -> ")
            if len(usuarios) > 0:
                for u in usuarios:
                    if(user == u.user):
                        print(str(u))
                    else:
                        print("No >v")
            else:
                print("vacia Bv")
            
sys.exit()
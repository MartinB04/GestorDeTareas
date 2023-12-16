from Usuario import *
from Menu import *
import sys

opc = None

usuarios = []

menu = Menu()

while opc != 0:
    
    menu.MenuPrincipal()
    opc = menu.Opc

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
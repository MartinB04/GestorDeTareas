class Usuario:
    user = ""
    nombre = ""
    password = ""

    def __init__(self, user, nombre, password) -> None:
        self.user = user
        self.nombre = nombre
        self.password = password

    def buscarUsuario(self):
        pass

    def __str__(self) -> str:
        return f"{self.user}\n{self.nombre}\n{self.password}\n"

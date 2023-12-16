class Usuario:
    user = ""
    nombre = ""
    password = ""

    def __init__(self, user, nombre, password) -> None:
        self.user = user
        self.nombre = nombre
        self.password = password

    def buscarUsuario(self,):
        pass

    @property
    def user(self):
        return self.user
    
    @user.setter
    def user(self, user):
        self.user = user

    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, password):
        self.password = password

    def __str__(self) -> str:
        return f"{self.user}\n{self.nombre}\n{self.password}\n"

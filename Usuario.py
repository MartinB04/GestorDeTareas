class Usuario:
    user = ""
    nombre = ""
    password = ""

    def __init__(self, user, nombre, password) -> None:
        self._user = user
        self._nombre = nombre
        self._password = password

    @property
    def User(self):
        return self._user
    
    @User.setter
    def User(self, user):
        self._user = user

    @property
    def Nombre(self):
        return self._nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Password(self):
        return self._password
    
    @Password.setter
    def Password(self, password):
        self._password = password

    def __str__(self) -> str:
        return f"{self._user}\n{self._nombre}\n{self._password}\n"

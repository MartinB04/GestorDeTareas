import mysql.connector

class ConexionMySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None
        self.cursor = None

    def conectar(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexion.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def ejecutar_consulta(self, consulta, parametros=None):
        try:
            self.conectar()
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)

            resultados = self.cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            self.desconectar()

    def ejecutar_insercion(self, consulta, datos):
        try:
            self.conectar()
            self.cursor.execute(consulta, datos)
            self.conexion.commit()
            print("Inserción exitosa.")
        except Exception as e:
            print(f"Error al insertar datos: {e}")
        finally:
            self.desconectar()
'''
# Ejemplo de uso
conexion = ConexionMySQL(host="tu_host", user="tu_usuario", password="tu_contraseña", database="tu_base_de_datos")

# Ejemplo de consulta
consulta_select = "SELECT * FROM Usuario;"
resultados = conexion.ejecutar_consulta(consulta_select)
for fila in resultados:
    print(fila)

# Ejemplo de inserción
consulta_insert = "INSERT INTO tu_tabla (columna1, columna2, columna3) VALUES (%s, %s, %s);"
datos_insert = ("valor1", "valor2", "valor3")
conexion.ejecutar_insercion(consulta_insert, datos_insert)
'''
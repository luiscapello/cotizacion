import datetime
import hashlib
from sqlite3 import connect
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self, idEmpleado, nombre, apellidos, email, password):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password


    def registrar(self):
        fecha = datetime.datetime.now()

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(%s, %s, %s, %s, %s, %s)"
        usuario = (self.idEmpleado, self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    def identificar(self):
        return self.nombre
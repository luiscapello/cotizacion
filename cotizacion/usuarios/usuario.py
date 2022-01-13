import mysql.connector
import datetime
import hashlib

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cotizacion",
    port="3306"
)

cursor = database.cursor(buffered = True)


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
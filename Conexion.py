
import mysql.connector

class CConexion:
    @staticmethod
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',
                                               password='123456',
                                               host='127.0.0.1',
                                               database='controlescolar',
                                               port='3306')
            print("Conexion correcta")

            return conexion
        except mysql.connector.Error as error:
            print("Error en la conexion {}".format(error))
            return None

# Llamar al método de la clase para probar la conexión
CConexion.ConexionBaseDeDatos()

